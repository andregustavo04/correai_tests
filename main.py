import json

from src.tools.retrieve_data_tools import (
    get_exercises_definitions, 
    get_measure_unities_available, 
    get_runner_information, 
    get_running_workout_types, 
    get_workout_statuses, 
    get_workout_types)

import os
from src.utils.configs import get_openai_api_key
# ----------- Setting Environment Variables ----------------

openai_api_key = get_openai_api_key()
os.environ["OPENAI_MODEL_NAME"] = 'gpt-3.5-turbo'

# from tools.create_training_plan import create_all_training_plan

# with open(r"trainin_plan_03.json", 'r', encoding='utf-8') as file:
#     jsonData = json.load(file)


# print(create_all_training_plan(jsonData, 1))

# =========================== Runnig First Crew ===========================

from crews.crew_01.crew import crew_create_training_plan

response = get_runner_information(1)


user_id = response.get('user_information').get('id')
first_name = response.get("user_information").get("first_name")
availability = response.get("user_information").get("availability")
exercise_history = response.get("user_historical_data").get("exercise_history")
health_history = response.get("user_historical_data").get("health_history")

goal = response.get("goals").get("description")
time_to_reach_goal = response.get("goals").get("time_to_reach_goal")


inputs = {
        "user_name": first_name,
        "user_id": user_id,
        "objetivo":goal,
        "tempo_para_atinigir_objetivo":time_to_reach_goal,
        "disponibilidade": availability,
        "data_inicio": "2024-09-04T21:22:14",
        "data_fim": "2024-10-16T21:22:14",
        "historico_exercicio": exercise_history,
        "historico_saude": health_history,
        "total_workouts": 18
}

result = crew_create_training_plan.kickoff(inputs)


print("#########  Criar estrutura do plano de treino  #########")
print(result.raw)
print(result.token_usage)
# print(type(result))

# print(result.to_dict())


# print(result.to_dict().get('workouts'))

workouts_list = result.to_dict().get('workouts')



# =========== Getting data from database ===========

exercises_definitions = get_exercises_definitions() 
measure_unities = get_measure_unities_available() 
running_workout_types = get_running_workout_types() 
workout_statuses = get_workout_statuses() 
workout_types = get_workout_types()

# =========== Assembling Inputs ===========

inputs_workouts = []

for w in workouts_list:
    content = {
        "exercises_definitions": exercises_definitions,
        "workout_types": workout_types,
        "running_workout_types": running_workout_types,
        "measure_unities": measure_unities,
        "workout_statuses": workout_statuses,
        "workout_description": w
    }

    inputs_workouts.append(content)



print("#########  Criar treinos  #########\n\n")

# for i in inputs_workouts:
#     print(i)
#     print('\n\n\n\n')

# =========== Running Crew ===========

from crews.crew_02.crew import crew_create_workout

results = crew_create_workout.kickoff_for_each(inputs_workouts)

for i in results:
    print(f"======== TREINO {results.index(i)} ========\n\n")
    print(i)
    





# from crews.create_training_plan.crew import create_training_plan_crew

# with open(r"training_plan_2.json", 'r', encoding='utf-8') as file:
#     jsonData = json.load(file)

# inputs = {
#     "user_id" : 1,
#     "jsonDataTrainingPlan": jsonData
# }

# result = create_training_plan_crew.kickoff(inputs)

# print(result.raw)
# print(result.token_usage)






