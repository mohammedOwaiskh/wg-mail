import requests
import logging
import pandas as pd


logging = logging.basicConfig(
    level=logging.DEBUG, format="%(asctime)s - %(levelname)s - %(message)s"
)


BASE_URL = "https://www.studibu.de/iPack3/ipack3/ajax/privroom/search"


QUERY_PARAMS = {
    "languageId": 2,  # 1 - German, 2 - English
    "s_Einzugsbereich": 1,  # Region/Catchment Area: -1 - any, 1 - Trier, 6 - Birkenfield,
    "s_ZimmerArt": -1,  # Room Type: -1 - All
    "s_Mietobergrenze": -1,  # Max rent: -1 - None
    "s_AnzahlZimmer": -1,  # No. of rooms: -1 - Any
}


def make_request() -> dict | None:

    response = requests.get(BASE_URL, QUERY_PARAMS)

    if response.status_code == 200:
        data = response.json()
        return data
    else:
        logging.error("Error Occured in fetching data")


def get_owner_data():

    data = make_request()
    if data:
        owner_df = pd.DataFrame(data)
        owner_df.set_index("Privatzimmer_ID")

        print(owner_df)


if __name__ == "__main__":
    get_owner_data()
