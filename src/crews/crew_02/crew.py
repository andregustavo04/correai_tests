from crewai import Crew
from crews.crew_02 import agents, tasks

# =============== Instantiating Agents ===============

agent_runner_coach = agents.runner_coach_specialist()
agent_database_specialist = agents.database_analyst()

# =============== Instantiating Tasks ===============
# task_01 = tasks.calculate_number_of_workouts(agent=agent_runner_coach)
task_01 = tasks.generate_workouts(agent=agent_runner_coach)
task_02 = tasks.check_workout_json_structure(agent=agent_database_specialist, context=[task_01])



# =============== Creating Crew ===============
crew_create_workout = Crew(
    agents=[agent_runner_coach, agent_database_specialist],
    tasks=[task_01, task_02],
    verbose=True,
    full_output=True,
    cache=True,
    memory=True
)