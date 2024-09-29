from crewai_tools import BaseTool
from src.utils.database import initialize_supabase
from datetime import datetime
import inspect
import os
from dotenv import load_dotenv

load_dotenv()
server_name = os.environ.get('SERVER_NAME')


# jsonData = dict(id="oi")


# ============================= Functios to interact with database =============================

def create_training_plan_in_db(
        title: str,
        description: str,
        start_date: str,
        end_date: str,
        is_base : bool,
        runner_goal_id: int,
        user_id: int
):
    supabase = initialize_supabase()
    table_name = "training_plans"
    data = {
        "title": title,
        "description": description,
        "start_date": start_date,
        "end_date": end_date,
        "is_base": is_base,
        "runner_goal_id": runner_goal_id,
        "user_id": user_id
    }

    try:
        response = dict(supabase.table(table_name).insert(data).execute())
        training_plan_id = response.get('data')[0].get('id')
        return training_plan_id
    
    except Exception as e:
        error_log = {
            "error_code": e,
            "table": table_name,
            "data": data,
            "date": str(datetime.now()),
            "server": f"{server_name}",
            "block": f"{inspect.currentframe().f_code.co_name}"
        }
        print(error_log)
        return error_log

def create_workout(
        title: str, 
        goal: str, 
        status_id: int,
        is_base: bool,
        is_test: bool,
        date: str,
        workout_type_id: int,
        running_workout_type_id: int,
        training_plan_id: int
    ):

    supabase = initialize_supabase()
    table_name = "workouts"
    data = {
        "title": title, 
        "goal": goal, 
        "status_id": status_id,
        "is_base": is_base,
        "is_test": is_test,
        "date": date,
        "workout_type_id": workout_type_id,
        "running_workout_type_id": running_workout_type_id,
        "training_plan_id": training_plan_id
    }

    try:
        response = dict(supabase.table(table_name).insert(data).execute())
        workout_id = response.get('data')[0].get('id')
        return workout_id
  
    except Exception as e:
        error_log = {
            "error_code": e,
            "table": table_name,
            "data": data,
            "date": str(datetime.now()),
            "server": f"{server_name}",
            "block": f"{inspect.currentframe().f_code.co_name}"
        }
        print(error_log)
        return error_log

def create_workout_part(
        name: str,
        order_number: int,
        workout_id: int
):
    supabase = initialize_supabase()
    table_name = "workout_parts"
    data = {
        "name": name,
        "order_number": order_number,
        "workout_id": workout_id
    }

    try:
        response = dict(supabase.table(table_name).insert(data).execute())
        workout_id = response.get('data')[0].get('id')
        return workout_id
    
    except Exception as e:
        error_log = {
            "error_code": e,
            "table": table_name,
            "data": data,
            "date": str(datetime.now()),
            "server": f"{server_name}",
            "block": f"{inspect.currentframe().f_code.co_name}"
        }
        print(error_log)
        return error_log

def create_workout_part_exercise_relation(
        workout_part_id: int,
        is_combination: bool,
        combination_structure_id: int | None,
        exercise_structure_id: int | None,
        order_number: int
):

    supabase = initialize_supabase()
    table_name = "workout_parts_exercises_relation"
    data = {
        "workout_part_id": workout_part_id,
        "is_combination": is_combination,
        "combination_structure_id": combination_structure_id,
        "exercise_structure_id": exercise_structure_id,
        "order_number": order_number
    }

    try:
        response = dict(supabase.table(table_name).insert(data).execute())
        relation_id = response.get('data')[0].get('id')
        return relation_id
    
    except Exception as e:
        error_log = {
            "error_code": e,
            "table": table_name,
            "data": data,
            "date": str(datetime.now()),
            "server": f"{server_name}",
            "block": f"{inspect.currentframe().f_code.co_name}"
        }
        print(error_log)
        return error_log


def create_combination_structure(
        workout_part_id: int,
        measure_unit_id: int,
        quantity: float,
        observations: str
):
    supabase = initialize_supabase()
    table_name = "combinations_structures"
    data = {
        "workout_part_id": workout_part_id,
        "measure_unit_id": measure_unit_id,
        "quantity": quantity,
        "observations": observations
    }

    try:
        response = dict(supabase.table(table_name).insert(data).execute())
        combination_structure_id = response.get('data')[0].get('id')
        return combination_structure_id
    
    except Exception as e:
        error_log = {
            "error_code": e,
            "table": table_name,
            "data": data,
            "date": str(datetime.now()),
            "server": f"{server_name}",
            "block": f"{inspect.currentframe().f_code.co_name}"
        }
        print(error_log)
        return error_log

def create_exercise_structure(
        workout_part_id: int,
        exercise_id: int,
        measure_unit_id: int,
        quantity: float,
        observations: str
):
    supabase = initialize_supabase()
    table_name = "exercises_structures"
    data = {
        "workout_part_id": workout_part_id,
        "measure_unit_id": measure_unit_id,
        "quantity": quantity,
        "observations": observations
    }

    try:
        response = dict(supabase.table(table_name).insert(data).execute())
        exercise_structure_id = response.get('data')[0].get('id')
        return exercise_structure_id
    
    except Exception as e:
        error_log = {
            "error_code": e,
            "table": table_name,
            "data": data,
            "date": str(datetime.now()),
            "server": f"{server_name}",
            "block": f"{inspect.currentframe().f_code.co_name}"
        }
        print(error_log)
        return error_log


def create_combination_exercise_relation(
        combination_structure_id: int,
        exercise_structure_id: int,
        order_number: int
):
    supabase = initialize_supabase()
    table_name = "combination_exercise_relation"
    data = {
        "combination_structure_id": combination_structure_id,
        "exercise_structure_id": exercise_structure_id,
        "order_number": order_number
    }

    try:
        response = dict(supabase.table(table_name).insert(data).execute())
        relation_id = response.get('data')[0].get('id')
        return relation_id
    
    except Exception as e:
        error_log = {
            "error_code": e,
            "table": table_name,
            "data": data,
            "date": str(datetime.now()),
            "server": f"{server_name}",
            "block": f"{inspect.currentframe().f_code.co_name}"
        }
        print(error_log)
        return error_log


# This function is gonna create all the records in all the tables to structure the entire training plan
def create_all_training_plan(jsonData: dict, user_id: int):

    training_plan_structure = jsonData.get('training_plan')

    training_plan_id = create_training_plan_in_db(
        title= training_plan_structure.get('title'),
        description= training_plan_structure.get('description'),
        start_date= training_plan_structure.get('start_date'),
        end_date= training_plan_structure.get('end_date'),
        is_base = training_plan_structure.get('is_base'),
        runner_goal_id= jsonData.get('goal_id'),
        user_id= user_id
    )

    if type(training_plan_id) != int:
        return "Erro ao criar training_plan"

    # --------------- Loop to create the workouts and their underlying structures ------------
    for workout in training_plan_structure.get('workouts'):
        workout_id = create_workout(
            title= workout.get("title"), 
            goal= workout.get("goal"), 
            status_id= workout.get("status_id"),
            is_base= workout.get("is_base"),
            is_test= workout.get("is_test"),
            date= workout.get("date"),
            workout_type_id= workout.get("workout_type_id"),
            running_workout_type_id= workout.get("running_workout_type_id"),
            training_plan_id= training_plan_id
        )

        for workout_part in workout.get('workout_parts'):
            workout_part_id = create_workout_part(
                name= workout_part.get('name'),
                order_number= workout_part.get('order_number'),
                workout_id= workout_id
            )

            for exercise in workout_part.get('exercises'):
                if exercise.get('is_combination') == True:

                    combination_structure = exercise.get('combination_structure')
                    
                    combination_structure_id = create_combination_structure(
                        workout_part_id= workout_part_id,
                        measure_unit_id= combination_structure.get('measure_unit_id'),
                        quantity= combination_structure.get('quantity'),
                        observations= combination_structure.get('observations')
                    )

                    workout_part_exercise_relation_id = create_workout_part_exercise_relation(
                        workout_part_id= workout_part_id,
                        is_combination= True,
                        combination_structure_id= combination_structure_id,
                        exercise_structure_id= None,
                        order_number= exercise.get('order_number')
                    )

                    for exercise_structure in combination_structure.get('exercise_structures'):
                        exercise_structure_id = create_exercise_structure(
                            workout_part_id= exercise_structure.get('workout_part_id'),
                            exercise_id= exercise_structure.get('exercise_id'),
                            measure_unit_id= exercise_structure.get('measure_unit_id'),
                            quantity= exercise_structure.get('quantity'),
                            observations= exercise_structure.get('observations')
                        )
                        
                        combination_exercise_relation_id = create_combination_exercise_relation(
                            combination_structure_id= combination_structure_id,
                            exercise_structure_id= exercise_structure_id,
                            order_number= exercise_structure.get('order_number')
                        )


                else:
                    exercise_structure = exercise.get('exercise_structure')

                    exercise_structure_id = create_exercise_structure(
                        workout_part_id= workout_part_id,
                        exercise_id= exercise_structure.get('exercise_id'),
                        measure_unit_id= exercise_structure.get('measure_unit_id'),
                        quantity= exercise_structure.get('quantity'),
                        observations= exercise_structure.get('observations')
                    )

                    workout_part_exercise_relation_id = create_workout_part_exercise_relation(
                        workout_part_id= workout_part_id,
                        is_combination= False,
                        combination_structure_id= None,
                        exercise_structure_id= exercise_structure_id,
                        order_number= exercise_structure.get('order_number')
                    )
    
    return "Success"


# ============================= CrewAI Tool =============================

class PersistTrainingPlanTool(BaseTool):
    name: str = "Criar Plano de Treino do Corredor"
    description: str = """
            Essa ferramenta é responsável por persistir o plano de treino do atleta
            no banco de dados. É necessário que se tenha o plano de treino em formato
            de json (ou dicionário python) (jsonData) e o id do usuário (user_id), para que possamos
            persistir os dados de maneira correta no banco de dados, garantindo a integridade dos 
            dados e das informações. É importante que o plano de treino seja passado integralmente, e não em partes.
            """

    def _run(self, jsonData: dict, user_id: str) -> dict:
        response = create_all_training_plan(jsonData=jsonData, user_id=user_id)

        return response