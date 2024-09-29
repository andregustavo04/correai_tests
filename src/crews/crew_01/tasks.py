from crewai import Task
from src.models.output_models import Output01

# Criar plano de treino
def calculate_number_of_workouts(agent):
    task = Task(
        description = """ 
            Calcule a quantidade de treinos totais que um plano de treino de corrida deve ter para esse caso, respeitando o histórico do paciente, seu objetivo, o tempo para atingir o objetivo, a data de início e a data final, e a disponibilidade de tempo do paciente. 
            - Paciente: {user_name}
            - Objetivo:{objetivo}
            - Tempo para atingir o objetivo: {tempo_para_atinigir_objetivo}
            - Disponibilidade de tempo: {disponibilidade}
            - Data de Início: {data_inicio}
            - Data Final: {data_fim}
            - Histórico de Exercício Físico: {historico_exercicio}
            - Histórico de Saúde: {historico_saude}

        """,
        expected_output = "O número de treinos totais, sem ser prolixo. Exemplo: 18 treinos totais.",
        agent=agent
    )

    return task

def generate_training_plan(agent, context: list):
    task = Task(
        description="""
            - Gere um treino de corrida personalizado para esse usuário: {user_name}, cujo id é {user_id}, de acordo com as informações abaixo.
            
            - Objetivo:{objetivo}
            - Tempo para atingir o objetivo: {tempo_para_atinigir_objetivo}
            - Disponibilidade de tempo: {disponibilidade}
            - Data de Início: {data_inicio}
            - Data Final: {data_fim}
            - Histórico de Exercício Físico: {historico_exercicio}
            - Histórico de Saúde: {historico_saude}

            É necessário que o plano de treino tenha um total de {total_workouts} treinos, respeitando a data de início, data final, e a disponibilidade de dias e horários do paciente. 
        """,
        expected_output="""
            O output esperado é um plano de treino no seguinte formado json que deve respeitar a seguinte validação do Pydantic:
                    class WorkoutDescription(BaseModel):
                        workout_description: str
                        date: str
                        type_of_workout: str
                        type_running_workout: str
                        workout_parts: List[str]


                    class Output01(BaseModel):
                        title: str
                        description: str
                        start_date: str
                        end_data: str
                        workouts: List[WorkoutDescription]


        Um exemplo: {{
                        "title": "str",
                        "description": "str",
                        "workouts": {{
                            "workout_description": "Descrição do treino",
                            "date": "data do treino no formato ISO 8601",
                            "type_of_workout": "Corrida ou Musculação, escolher apenas um",
                            "type_running_workout": "Escolher entre: Fartlek, Intervalado, Longão, Regenerativo",
                            "workout_parts": [
                            "Aqueicmento: exercícios de aquecimento", "Parte principal: exercícios da parte principal do treino", "Desaquecimento: exercícios para desaquecer o corpo"
                            ]

                        }}
                    }}
        """,
        context=context,
        output_json=Output01,
        agent=agent,
    )

    return task

def check_training_plan_structure(agent, context: list):
    task = Task(
        description="Corrigir a estrutura do JSON",
        expected_output="""O JSON com sua estrutura corrigida, no seguinte formado json que deve respeitar a seguinte validação do Pydantic:
                   
        
                  class WorkoutDescription(BaseModel):
                        workout_description: str
                        date: str
                        type_of_workout: str
                        type_running_workout: str
                        workout_parts: List[str]


                    class Output01(BaseModel):
                        title: str
                        description: str
                        start_date: str
                        end_data: str
                        workouts: List[WorkoutDescription]
                    
                    Um exemplo: {{
                            "title": "str",
                            "description": "str",
                            "workouts": {{
                                "workout_description": "Descrição do treino",
                                "date": "data do treino no formato ISO 8601",
                                "type_of_workout": "Corrida ou Musculação, escolher apenas um",
                                "type_running_workout": "Escolher entre: Fartlek, Intervalado, Longão, Regenerativo",
                                "workout_parts": [
                                "Aqueicmento: exercícios de aquecimento", "Parte principal: exercícios da parte principal do treino", "Desaquecimento: exercícios para desaquecer o corpo"
                                ]

                            }}
                        }}
                    
                    """,
        context=context,
        output_json=Output01,
        agent=agent
    )

    return task