from supabase import create_client
import os
from dotenv import load_dotenv

load_dotenv()

url = os.getenv("PROJECT_URL")
key = os.getenv("API_KEY")



supabase = create_client(url, key)