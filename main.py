import os
from supabase import create_client, Client
import dotenv

dotenv.load_dotenv('variable.env')

url: str = os.environ.get("SUPABASE_URL")
key: str = os.environ.get("SUPABASE_KEY")
supabase: Client = create_client(url, key)
# https://supabase.com/docs/guides/database/functions
data = supabase.table("table_name").select("*").execute()
# data = supabase.table("table_name").select("*").eq('plate_number', '123 ABC').execute()
assert len(data.data) > 0

print(data)