import os
from crewai import Agent, Task, Crew
from utils.configs import get_openai_api_key
from tools.retrieve_data_tools import GetRunnerInformationTool

# ----------- Setting Environment Variables ----------------

openai_api_key = get_openai_api_key()
os.environ["OPENAI_MODEL_NAME"] = 'gpt-3.5-turbo'


# ----------- Setting Custom Tools ------------------

get_runner_information_tool = GetRunnerInformationTool()


writer_agent = Agent(
    role="Escritor de Biografias",
    goal="Escrever uma história de como a pessoa conseguiu alcançar o objetivo dela dentro do tempo que ela queria, com a ajuda da CorreAI, uma IA que exerce o papel de personal trainer para essa pessoa. A história deve ter um tom de superação e de biografia.",
    tools=[get_runner_information_tool],
    verbose=True,
    backstory="Você é um escritor de biografias muito famoso e respeitado no mundo inteiro, por já ter escrito biografias de grandes personaagens da história com grande maestria. Você escreve de uma maneira única, com muita clareza e muitos detalhes, deixando a história envolvente."
)

get_runner_information_task = Task(
    description="Pegar informações do usuário cujo id é {user_id} para que você possa escrever a história com dados corretos, além de conhecê-lo melhor e poder melhorar o tom da história",
    expected_output="Uma descrição do usuário, com tudo o que for relevante para escrever uma história envolvente e cativante.",
    agent=writer_agent
)

write_story_task = Task(
    description="Escreva a história em tom de biografia e de superação, de como o usuário conseguiu alcançar o objetivo dele.",
    expected_output="Uma história envolvente e cativante de como o usuário conseguiuu conquistar o objetivo dele dentro do tempo que ele queria, com a ajuda da CorreAI, e de como isso mudou a vida dele para melhor.",
    agent=writer_agent
)

create_workout_crew = Crew(
    agents=[writer_agent],
    tasks=[get_runner_information_task, write_story_task],
    verbose=True
)