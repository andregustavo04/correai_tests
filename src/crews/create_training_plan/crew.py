from crewai import Crew, Process

from crews.create_training_plan.agents import (
    sport_doctor, 
    runner_coach_specialist, 
    runner_coach_specialist_reviewer, 
    database_analyst
)

from crews.create_training_plan.tasks import (
    get_informations_about_runner, 
    understand_limitations_of_runner, 
    create_training_plan_for_runner, 
    check_quality_of_training_plan, 
    check_training_plan_structure, 
    persist_training_plan_in_database, 
    create_response_message
) 

# ====================== Getting Agents Set Up ======================
sport_doctor_agent = sport_doctor()
runner_coach_specialist_agent = runner_coach_specialist()
runner_coach_specialist_reviewer_agent = runner_coach_specialist_reviewer()
database_analyst_agent = database_analyst()

# ====================== Getting Tasks Set Up ======================
task_01 = get_informations_about_runner(agent=runner_coach_specialist_agent) 
    
task_02 = understand_limitations_of_runner(agent=sport_doctor_agent, context=[task_01]) 

task_03 = create_training_plan_for_runner(agent=runner_coach_specialist_agent, context=[task_01, task_02]) 
    
task_04 = check_quality_of_training_plan(agent=runner_coach_specialist_reviewer_agent, context=[task_01, task_02, task_03])

task_05 = check_training_plan_structure(agent=database_analyst_agent, context=[task_04])

task_06 = persist_training_plan_in_database(agent=database_analyst_agent, context=[task_04, task_05]) 

task_07 = create_response_message(agent=runner_coach_specialist_agent)

# ====================== Create Crew ======================
create_training_plan_crew = Crew(
    agents=[sport_doctor_agent, runner_coach_specialist_agent, runner_coach_specialist_reviewer_agent, database_analyst_agent],
    tasks=[task_01, task_02, task_03, task_04, task_06, task_07],
    process=Process.sequential,
    verbose=True,
    full_output=True,
    cache=True
)