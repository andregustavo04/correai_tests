from crewai import Task
from src.models.output_models import Workout



def generate_workouts(agent):
    task = Task(
        description="""

        Com base na descrição de treino a seguir, estruture o treino com os exercícios corretos, com as unidades de medida e quantidades corretas. 
        Quando for necessário, utilize combinações de exercícios (combinations), e obedeça a hierarquia das partes do treino e dos exercícios.
        Para utilizar os dados corretos, aqui estão as informações de que necessita para estruturar os treinos:

        - Lista de definições de exercícios (exercise definitions): {exercises_definitions}
        - Lista de de tipos de treino (workout types): {workout_types}
        - Lista de tipos de treino de corrida (running workout types): {running_workout_types}
        - Lista de unidades de medida (measure unities available): {measure_unities}
        - Lista de status de treinos (workout statuses): {workout_statuses}

        Descrição do treino: {workout_description}



    """,
        expected_output="""

        O formato do treino deve ser um JSON, que deve seguir a seguinte validação do Pydantic:

        class ExerciseStructure(BaseModel):
            workout_part_id: Optional[int]  # null é tratado como None em Python
            exercise_id: int
            measure_unit_id: int
            quantity: float
            observations: str
            order_number: int

        class CombinationStructure(BaseModel):
            measure_unit_id: int
            quantity: float
            observations: str
            exercises_structures: List[ExerciseStructure]


        class Exercises(BaseModel):
            is_combination: bool
            exercise_structure: Optional[ExerciseStructure]
            combination_structure: Optional[CombinationStructure]

        class WorkoutPart(BaseModel):
            name: str
            exercises: List[Exercises]


        class Workout(BaseModel):
            title: str
            goal: str
            status_id: int
            is_base: bool
            is_test: bool
            date: str
            workout_type_id: int
            running_workout_type_id: int
            workout_parts: List[WorkoutPart]

        Um exemplo: {{
            "title": "Treino Lindo",
            "goal": "Começar",
            "status_id": 1,
            "is_base": false,
            "is_test": false,
            "date": "2024-08-28T15:30:00",
            "workout_type_id": 1,
            "running_workout_type_id": 2,
            "workout_parts": [
                {{
                "name": "Aquecimento",
                "exercises": [
                    {{
                    "is_combination": true,
                    "exercise_structure": null,
                    "combination_structure": {{
                        "measure_unit_id": 2,
                        "quantity": 20.3,
                        "observations": "Nenhuma",
                        "exercise_structures": [
                        {{
                            "workout_part_id": null,
                            "exercise_id": 1,
                            "measure_unit_id": 2,
                            "quantity": 20.4,
                            "observations": "Nenhuma",
                            "order_number": 1
                        }},
                        {{
                            "workout_part_id": null,
                            "exercise_id": 1,
                            "measure_unit_id": 2,
                            "quantity": 20.4,
                            "observations": "Nenhuma",
                            "order_number": 2
                        }}
                        ]
                    }},
                    "order_number": 1
                    }}
                ]
                }}
            ]
        }}  

    """,
        output_json=Workout,
        agent=agent
    )

    return task









def check_workout_json_structure(agent, context: list):
    task = Task(
        description="Corrigir a estrutura do JSON",
        expected_output="""O formato do treino deve ser um JSON, que deve seguir a seguinte validação do Pydantic:

        class ExerciseStructure(BaseModel):
            workout_part_id: Optional[int]  # null é tratado como None em Python
            exercise_id: int
            measure_unit_id: int
            quantity: float
            observations: str
            order_number: int

        class CombinationStructure(BaseModel):
            measure_unit_id: int
            quantity: float
            observations: str
            exercises_structures: List[ExerciseStructure]


        class Exercises(BaseModel):
            is_combination: bool
            exercise_structure: Optional[ExerciseStructure]
            combination_structure: Optional[CombinationStructure]

        class WorkoutPart(BaseModel):
            name: str
            exercises: List[Exercises]


        class Workout(BaseModel):
            title: str
            goal: str
            status_id: int
            is_base: bool
            is_test: bool
            date: str
            workout_type_id: int
            running_workout_type_id: int
            workout_parts: List[WorkoutPart]

        Um exemplo: {{
            "title": "Treino Lindo",
            "goal": "Começar",
            "status_id": 1,
            "is_base": false,
            "is_test": false,
            "date": "2024-08-28T15:30:00",
            "workout_type_id": 1,
            "running_workout_type_id": 2,
            "workout_parts": [
                {{
                "name": "Aquecimento",
                "exercises": [
                    {{
                    "is_combination": true,
                    "exercise_structure": null,
                    "combination_structure": {{
                        "measure_unit_id": 2,
                        "quantity": 20.3,
                        "observations": "Nenhuma",
                        "exercise_structures": [
                        {{
                            "workout_part_id": null,
                            "exercise_id": 1,
                            "measure_unit_id": 2,
                            "quantity": 20.4,
                            "observations": "Nenhuma",
                            "order_number": 1
                        }},
                        {{
                            "workout_part_id": null,
                            "exercise_id": 1,
                            "measure_unit_id": 2,
                            "quantity": 20.4,
                            "observations": "Nenhuma",
                            "order_number": 2
                        }}
                        ]
                    }},
                    "order_number": 1
                    }}
                ]
                }}
            ]
        }}
                    
                    """,
        context=context,
        output_json=Workout,
        agent=agent
    )

    return task