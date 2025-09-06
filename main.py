from dotenv import load_dotenv

from datafetcher import get_owner_data

load_dotenv()

if __name__ == "__main__":

    data = get_owner_data()
