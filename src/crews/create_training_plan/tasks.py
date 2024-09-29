from crewai import Task
from src.models.workout_model import Goal
from src.tools.create_training_plan import (
    PersistTrainingPlanTool
)

# ======================== Instantiating Tools ========================

persist_training_plan_in_database_tool = PersistTrainingPlanTool()


# ======================== Defining Tasks ========================


def get_informations_about_runner(agent):
    task = Task(
        description="Coletar as informações do usuário (corredor), cujo id é {user_id} para poder conhecer suas condições, seus objetivos e suas limitações.",
        expected_output="Um texto descrevendo as informações do usuário.",
        agent=agent
    )

    return task


def understand_limitations_of_runner(agent, context: list):

    task = Task(
        description="Entender as limitações físicas do usuário (corredor), para poder montar um plano de treino de corrida personalizado que respeite suas limitações",
        expected_output="Uma análise das limitações físicas do usuário",
        context=context,
        agent=agent
    )

    return task

def create_training_plan_for_runner(agent, context: list):

    task = Task(
        description="Criar o plano de treino de corrida personalizado para o usuário (corredor)",
        expected_output="O plano de treino de corrida completo personalizado para o usuário (corredor), com todas as informações necessárias, e respeitando a estrutura de dados correta de um plano de treino. Estrutura de exemplo esperada: {jsonDataTrainingPlan}",
        context=context,
        # output_json=Goal,
        agent=agent
    )

    return task

def check_quality_of_training_plan(agent, context: list):
    task = Task(
        description="Checar a qualidade do plano de treino de corrida personalizado gerado para o usuário (corredor) e fazer as devidas correções, se necessário.",
        expected_output="O plano de treino de corrida personalizado corrigido, em formato de dicionário python. Estrutura de exemplo esperada: {jsonDataTrainingPlan}",
        context=context,
        # output_json=Goal,
        agent=agent
    )

    return task

def check_training_plan_structure(agent, context: list):
    task = Task(
        description="Checar a estrutura de dados do plano de treino de corrida personalizado gerado para o usuário (corredor), e fazer as devidas modificações somente se for necessário, para garantir a integridade dos dados e das informações.",
        expected_output="O plano de treino de corrida personalizado gerado para o usuário (corredor), com a estrutura de dados correta. Estrutura de exemplo esperada: {jsonDataTrainingPlan}",
        context=context,
        # output_json=Goal,
        agent=agent
    )

    return task


def persist_training_plan_in_database(agent, context: list):
    task = Task(
        description="Persistir no banco de dados da aplicação o plano de treino de corrida personalizado gerado para o usuário (corredor). É necessário passar a estrutura inteira do plano de treino, e não é permitido passar apenas partes do treino.",
        expected_output="Status de sucesso ou erro da operação.",
        context=context,
        agent=agent,
        tools=[persist_training_plan_in_database_tool]
    )

    return task

def create_response_message(agent):
    task = Task(
        description="Criar uma mensagem de texto como resposta à solicitação do usuário de um plano de treino de corrida personalizado para ele",
        expected_output="Uma mensagem de texto de resposta para o usuário, com linguagem amigável. Use emojis para deixar a mensagem mais próxima do tom de comunicação do usuário.",
        agent=agent
    )

    return task