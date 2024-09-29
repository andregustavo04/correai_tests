from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import datetime

class ExerciseStructure(BaseModel):
    exercise_id: int
    measure_unit_id: int
    quantity: float
    observations: str
    order_number: int

class CombinationStructure(BaseModel):
    measure_unit_id: int
    quantity: float
    observations: str
    exercise_structures: List[ExerciseStructure]

class Exercise(BaseModel):
    is_combination: bool
    exercise_structure: Optional[ExerciseStructure]
    combination_structure: Optional[CombinationStructure]
    order_number: int

class WorkoutPart(BaseModel):
    name: str
    order_number: int
    exercises: List[Exercise]

class Workout(BaseModel):
    title: str
    goal: str
    status_id: int
    is_base: bool
    is_test: bool
    date: datetime
    workout_type_id: int
    running_workout_type_id: int
    workout_parts: List[WorkoutPart]

class TrainingPlan(BaseModel):
    title: str
    description: str
    start_date: datetime
    end_date: datetime
    is_base: bool
    user_id: int
    workouts: List[Workout]

class Goal(BaseModel):
    goal_id: int
    training_plan: TrainingPlan
