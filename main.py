import os
from supabase import create_client, Client
import dotenv

dotenv.load_dotenv('variable.env')

url: str = os.environ.get("SUPABASE_URL")
key: str = os.environ.get("SUPABASE_KEY")
supabase: Client = create_client(url, key)
data = supabase.table("table_name").select("*").execute()
assert len(data.data) > 0

print(data)