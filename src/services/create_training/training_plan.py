from openai import OpenAI
import os
import requests
from dotenv import load_dotenv
from CorreAI.src.tools.retrieve_data_tools import (
    get_exercises_definitions, 
    get_measure_unities_available, 
    get_runner_information, 
    get_running_workout_types, 
    get_workout_statuses, 
    get_workout_types
)

def create_training_plan(assistant_id, openai_api_key, user_id):

    print("Rodando task")

    # Gather Data from Database
    response = get_runner_information(user_id)


    # user_id = response.get('user_information').get('id')
    first_name = response.get("user_information").get("first_name")
    availability = response.get("user_information").get("availability")
    exercise_history = response.get("user_historical_data").get("exercise_history")
    health_history = response.get("user_historical_data").get("health_history")

    goal = response.get("goals").get("description")
    time_to_reach_goal = response.get("goals").get("time_to_reach_goal")

    data_inicio = "2024-09-04T21:22:14"
    data_fim = "2024-10-16T21:22:14"

    total_workouts = 18

    # Initialize OpenAI Cliente
    client = OpenAI(
        api_key=openai_api_key
    )

    # Initialize Assistant
    coach = client.beta.assistants.retrieve(
        assistant_id=assistant_id
    )

    # Create Thread
    thread = client.beta.threads.create()

    # Setup Instructions
    instructions_01 = f"""

        - You need to generate a run training plan for this patient: {first_name}, whose id is {user_id}. Below, you have some informations about it.
            
            - Goal:{goal}
            - Time to reach the goal: {time_to_reach_goal}
            - Availability to workout: {availability}
            - Start Date: {data_inicio}
            - End Date: {data_fim}
            - Exercise History: {exercise_history}
            - Health History: {health_history}

            This training plan has to have {total_workouts} workouts in total, respecting the start date, end date and the patient's availability of days and hours. 
    
 """
    
    instructions_02 = """
                        You have to answer with a json in the following format: 
                        
                        {
                                        "title": "str",
                                        "description": "str",
                                        "workouts": {
                                            "workout_description": "Descrição do treino",
                                            "date": "data do treino no formato ISO 8601",
                                            "type_of_workout": "Corrida ou Musculação, escolher apenas um",
                                            "type_running_workout": "Escolher entre: Fartlek, Intervalado, Longão, Regenerativo",
                                            "workout_parts": [
                                            "Aqueicmento: exercícios de aquecimento", "Parte principal: exercícios da parte principal do treino", "Desaquecimento: exercícios para desaquecer o corpo"
                                            ]

                                        }
                                    }

                    You must answer only with the json, nothing else. And your response must be in Portuguese-BR.
                """
        
    
    instructions = instructions_01 + instructions_02

    
    print("Instructions criadas")
    print(instructions)

    run = client.beta.threads.runs.create(
        thread_id=thread.id,
        assistant_id=coach.id,
        instructions=instructions,
        response_format={ "type": "json_object" }
    )   
    
    status = None
    counter = 0

    while status != "completed" and counter < 100:
        print(f"Checando run status -> {counter}")

        run_retrieved = client.beta.threads.runs.retrieve(
            thread_id=thread.id,
            run_id=run.id
        )
        
        status = run_retrieved.status
        counter+= 1

    
    if counter >= 100:
        return KeyError


    messages = client.beta.threads.messages.list(
        thread_id=thread.id
    )


    assistant_response = messages.data[0].content[0].text.value

    return assistant_response