import os
from dotenv import load_dotenv
from supabase import create_client, Client
import json

load_dotenv()

def initialize_supabase():
    url: str = os.environ.get("SUPABASE_URL")   
    key: str = os.environ.get("SUPABASE_KEY")
    supabase: Client = create_client(url, key)

    return supabase