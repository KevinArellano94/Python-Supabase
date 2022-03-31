import os
import sys
from supabase import create_client, Client
import dotenv

def main():
    menu()

    try:
        selection = int(input(f'Type the number to select: '))
        if selection > 0 and selection < 2:
            if selection == 1: select_all()
            if selection == 0: exit()
        else:
            print(f'invalid number range ( 1 - 4 )\n')
    except Exception as e:
        print(e, '\n')

def menu():
    print(f'1. SELECT *')
    print(f'0. EXIT')

def select_all():
    data = supabase.table("table_name").select("*").execute()
    assert len(data.data) > 0
    # print(data.data[1])

    # print(data.data[1]['id'])
    print_data(data.data)

def select_custom():
    data = supabase.table("table_name").select("*").eq('plate_number', '123 ABC').execute()
    assert len(data.data) > 0
    # print(data.data[1])

    # print(data.data[1]['id'])
    print_data(data.data)

def print_data(n):
    for x in range(len(n)):
        print(n[x])

def exit():
    sys.exit(0)

if __name__ == '__main__':
    dotenv.load_dotenv('variable.env')

    url: str = os.environ.get("SUPABASE_URL")
    key: str = os.environ.get("SUPABASE_KEY")
    supabase: Client = create_client(url, key)

    try:
        main()
    except KeyboardInterrupt:
        sys.exit()