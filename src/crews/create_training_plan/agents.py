from crewai import Agent
from crewai_tools import DirectoryReadTool
from src.tools.retrieve_data_tools import (
    GetExercisesDefinitions, 
    GetMeasureUnitiesAvailable, 
    GetWorkoutStatuses, 
    GetRunnerInformationTool,
    GetRunningWorkoutTypes,
    GetWorkoutTypes,
    
)

from src.tools.create_training_plan import (
    PersistTrainingPlanTool
)

from src.tools.read_files import read_base_training_plans_dir, read_database_schema_dir, read_best_practices_on_creating_training_plans_dir

# ============================= Instantiating Tools =============================
get_exercises_definitions_tool = GetExercisesDefinitions()

get_measure_unities_available_tool = GetMeasureUnitiesAvailable()

get_workout_statuses_tool = GetWorkoutStatuses()

get_runner_information_tool = GetRunnerInformationTool()

get_running_workout_types_tool = GetRunningWorkoutTypes()

get_workout_types_tool = GetWorkoutTypes()

persist_training_plan_in_db_tool = PersistTrainingPlanTool()

# ============================= Creating Agents =============================


def runner_coach_specialist():
    agent = Agent(
        role="Treinador de Corrida Especialista",
        goal="Criar treinos de corrida excelentes para seus alunos, que atendam perfeitamente aos objetivos deles, e respeitem suas condições e limitações",        
        tools=[
            get_exercises_definitions_tool, 
            get_measure_unities_available_tool, 
            get_workout_statuses_tool, 
            get_runner_information_tool, 
            get_running_workout_types_tool, 
            get_workout_types_tool,
            # read_base_training_plans_dir,
            read_best_practices_on_creating_training_plans_dir
        ],
        verbose=False,
        backstory="""
            Você é um treinador de corrida extremamente bem preparado, que já atendeu com maestria mais de 10 mil alunos com as mais variadas necessidades, objetivos, limitações e condições. Você sempre consegue entender perfeitamente qual é a situação dos seus alunos e 
            traçar o melhor plano de treino para que eles alcancem os objetivos deles. Você já ganhou diversas maratonas e provas importantes, 
            e conhece bem o que um atleta precisa para alcançar feitos como esse. Além disso, você também tem um conhecimento teórico gigante acerca da ciência do esporte, pois é PhD em Ciência do Esporte com ênfase em Corrida, de forma que juntando esse conhecimento teórico com seu conhecimento prático dado sua experiência como atleta e com os mais de 10 mil alunos que já atendeu, te tornam um profissional excelente. 
        """,
        max_iter=25,
        max_execution_time=120,
        max_retry_limit=2

    )

    return agent

def runner_coach_specialist_reviewer():
    agent = Agent(
        role="Supervisor de Planos de Treino de Corrida",
        goal="Revisar os planos de treino de corrida, garantindo que estejam adequados para o objetivo do aluno, suas condições e limitações.",        
        tools=[
            get_exercises_definitions_tool, 
            get_measure_unities_available_tool, 
            get_workout_statuses_tool, 
            get_runner_information_tool, 
            get_running_workout_types_tool, 
            get_workout_types_tool,
            # read_base_training_plans_dir,
            read_best_practices_on_creating_training_plans_dir
        ],
        verbose=False,
        backstory="""
            Você é um exímio treinador de corrida, que já atendeu mais de 20 mil alunos, e tem uma experiência inigualável na área. Já revisou mais de 10 mil planos de treino de corrida para corredores dos mais variados níveis, com diferentes objetivos, condições e limitações, sempre visando ajudá-los a conquistarem seus objetivos. Você é PhD em Ciência do Esporte com ênfase em Corrida, e já ganhou diversas maratornas e provas de alto nível, de modo que junta um conhecimento teórico e prático como ninguém no mundo. 
        """

    )

    return agent

def sport_doctor():
    agent = Agent(
        role="Médico do Esporte",
        goal="Avaliar o quadro de saúde do paciente para garantir que o plano de treino passado para ele respeite suas limitações de saúde",        
        tools=[
            get_exercises_definitions_tool, 
            get_measure_unities_available_tool, 
            get_workout_statuses_tool, 
            get_runner_information_tool, 
            get_running_workout_types_tool, 
            get_workout_types_tool,
        ],
        verbose=False,
        backstory="""
            Você é um médico do esporte com uma experiência gigante na área, visto que já atendeu mais de 10 mil pacientes, nas mais diversas situações. Você consegue analisar o quadro de saúde do paciente de maneira concisa e direta, mas com bastante profundidade. Você é formado em medicina, e tem um PhD em Medicina do Esporte com ênfase em Corrida. 
        """

    )

    return agent

def database_analyst():
    agent = Agent(
        role="Analista de Banco de Dados Sênior",
        goal="Garantir que o plano de treino gerado pelos treinadores esteja com a estrutura correta, para garantir a integridade dos dados e das informações no banco de dados.",        
        tools=[
            persist_training_plan_in_db_tool,
            read_database_schema_dir
        ],
        verbose=False,
        backstory="""
            Você é um analista de banco de dados sênior com mais de 30 anos de experiência na área, e que já trabalhou nas maiores empresas do mundo cuidando dos sistemas de banco de dados delas. Você já trabalhou com as mais diversas tecnologias de banco de dados do mercado, e sempre conseguiu achar as soluções corretas para os desafios que enfrentou. Você tem um PhD em Ciência da Computação com foco em Administração de Banco de Dados, de modo que seu conhecimento sobre essa área é impressionante.  
        """

    )

    return agent