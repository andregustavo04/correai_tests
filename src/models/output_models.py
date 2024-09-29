from pydantic import BaseModel
from typing import List, Optional



# ============= Output for Crew 01 ==================
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



# ============= Output for Crew 02 ==================
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




