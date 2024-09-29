from openai import OpenAI
import os
import requests
from dotenv import load_dotenv
from src.services.create_training.training_plan import create_training_plan


# Getting Keys

load_dotenv()

OPEN_AI_KEY=os.getenv("OPENAI_API_KEY")

ASSISTANT_ID = os.getenv("ASSISTANT_ID")

# Creating Training Plan

print(create_training_plan(ASSISTANT_ID, OPEN_AI_KEY, 1))


