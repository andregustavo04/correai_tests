from crewai_tools import BaseTool
from src.utils.database import initialize_supabase
import os
from dotenv import load_dotenv
import inspect
    


# ==================================== FUNCTIONS ====================================

def get_runner_information(user_id: int) -> dict:

    if not user_id:
        return KeyError

    supabase = initialize_supabase()


    user_information = dict(supabase.table("users").select("id, first_name, last_name, nickname, gender, birth_date, availability").eq("id", user_id).execute()).get('data')
    anamnese = dict(supabase.table("runner_anamnese").select("*").eq("user_id", user_id).execute()).get('data')
    goals = dict(supabase.table("runner_goals").select("*").eq("user_id", user_id).execute()).get('data')
    

    if len(user_information)> 0:
        user_information = user_information[0]

    if len(anamnese) > 0:
        anamnese = anamnese[0]
    
    if len(goals) > 0:
        goals = goals[0]

    response = {
        "user_information": user_information,
        "user_historical_data": anamnese,
        "goals": goals,
    }


    return response


def get_exercises_definitions() -> list: # Incompleto
    supabase = initialize_supabase()
    response = None

    result = dict(supabase.table('exercises_definitions').select('*').execute()).get('data')

    if len(result) > 0:
        response = result
    
    print(response)
    
    return response

def get_measure_unities_available() -> list:
    supabase = initialize_supabase()
    response = None

    result = dict(supabase.table('measure_unities').select('*').execute()).get('data')

    if len(result) > 0:
        response = result
    
    print(response)
    
    return response

def get_workout_types() -> list:
    supabase = initialize_supabase()
    response = None

    result = dict(supabase.table('workout_types').select('*').execute()).get('data')

    if len(result) > 0:
        response = result
    
    print(response)
    
    return response

def get_running_workout_types() -> list:
    supabase = initialize_supabase()
    response = None

    result = dict(supabase.table('running_workout_types').select('id, name').execute()).get('data')

    if len(result) > 0:
        response = result
    
    print(response)
    
    return response

def get_workout_statuses() -> list:
    supabase = initialize_supabase()
    response = None

    result = dict(supabase.table('workout_statuses').select('*').execute()).get('data')

    if len(result) > 0:
        response = result
    
    print(response)
    
    return response


# ==================================== TOOLS ====================================

class GetRunnerInformationTool(BaseTool):
    name: str = "Coletar Informações do Corredor"
    description: str = """
            Essa ferramenta é reponsável por fazer uma consulta ao banco de dados da aplicação 
            e retornar informações do corredor (também conhecido como usuário), tais como seu histórico de saúde, sua disponibilidade
            de treinos, histórico de atividades físicas, e objetivo de treino, para que se possa fazer
            um treino mais personalizado, de modo a atender suas circunstâncias. É necessário passar como
            parâmetro o id do usuário (user_id) para que possamos fazer a consulta no banco de dados de
            maneira correta.       
            """

    def _run(self, user_id: str) -> dict:
        response = get_runner_information(user_id)

        return response
    
class GetExercisesDefinitions(BaseTool):
    name: str = "Coletar Definições dos Exercícios"
    description: str = """
            Essa ferramenta é reponsável por fazer uma consulta ao banco de dados da aplicação 
            e retornar todas as definições de exercícios, como seu nome, sua descrição, seus benefícios, e suas limitações.
            Essas informações são importantes para que se possa montar os treinos do atleta da melhor maneira possível, com
            exercícios coerentes ao seus objetivos, limitações e características.
            ...    
            """

    def _run(self, user_id: str) -> dict:
        response = get_exercises_definitions()

        return response

class GetMeasureUnitiesAvailable(BaseTool):
    name: str = "Coletar as Unidaes de Medida Disponíveis"
    description: str = """
            Essa ferramenta é reponsável por fazer uma consulta ao banco de dados da aplicação 
            e retornar todas as unidades de medida disponíveis. As unidades de medida serão utilizadas
            na criação dos treinos do atleta para que, além de apenas saber a quantidade, ele também
            consiga saber qual a unidade de medida que está sendo utilizada e executar o exercício da
            melhor maneira possível. 
            """

    def _run(self, user_id: str) -> dict:
        response = get_measure_unities_available()

        return response
    

class GetWorkoutTypes(BaseTool):
    name: str = "Coletar Tipos de Treino"
    description: str = """
            Essa ferramenta é reponsável por fazer uma consulta ao banco de dados da aplicação 
            e retornar todos os tipos de treino disponíveis, para que se possa classificar os
            treinos criado de maneira adequada.
            """

    def _run(self, user_id: str) -> dict:
        response = get_workout_types()

        return response

class GetRunningWorkoutTypes(BaseTool):
    name: str = "Coletar Tipos de Treino de Corrida"
    description: str = """
            Essa ferramenta é reponsável por fazer uma consulta ao banco de dados da aplicação 
            e retornar todos os tipos de treino de corrida. Por serem treinos específicos (de corrida),
            eles também têm suas próprias classificações, portanto é necessário saber quais são os 
            possíveis tipos de treino de corrida para que se possa fazer a classificação de forma correta.
            """

    def _run(self, user_id: str) -> dict:
        response = get_running_workout_types() 

        return response
    

class GetWorkoutStatuses(BaseTool):
    name: str = "Coletar os Status Possíveis de um Treino (Workout)"
    description: str = """
            Essa ferramenta é reponsável por fazer uma consulta ao banco de dados da aplicação 
            e retornar todos os status de treinos disponíveis. Isso é importante para que possamos
            definir e acompanhar o status dos treinos dos atletas. Por padrão, o status padrão é 
            "Not Started".
            """

    def _run(self, user_id: str) -> dict:
        response = get_workout_statuses()

        return response