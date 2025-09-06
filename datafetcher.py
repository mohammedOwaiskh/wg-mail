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


def transform_data(df: pd.DataFrame):
    rename_cols = {
        "Privatzimmer_ID": "room_id",
        "PrivatzimmerArt": "room_type_code",
        "PrivatzimmerArtName": "room_type",
        "Status": "status",
        "FreiVon": "available_from",
        "WG": "is_share_apartment",
        "Miete": "cold_rent",
        "Nebenkosten": "ancillary_costs",
        "Kaution": "deposit",
        "Paare": "couple_allowed",
        "Maenner": "male_only",
        "Frauen": "female_only",
        "Auslaender": "foreigner_allowed",
        "AnzahlZimmer": "no_of_rooms",
        "Qm": "size_in_sq_mtrs",
        "Strasse": "street",
        "Plz": "postal_code",
        "Ort": "city",
        "EinrichtungsartName": "furnishing",
        "VermieterName": "landlord_last_name",
        "VermieterVorname": "landlord_first_name",
        "VermieterTelefon": "mobile_number",
        "VermieterEMail": "email_id",
    }
    keep_cols = list(rename_cols.keys())

    new_df = df.drop(df.columns.difference(keep_cols), axis=1).rename(
        columns=rename_cols
    )

    new_df.replace(
        ["leer", "teilmöbliert", "möbliert", "möbl. oder leer"],
        ["Unfurnished", "Partially Furnished", "Furnished", "Furnished or Unfurnished"],
    )

    new_df = new_df.replace(
        ["leer", "teilmöbliert", "möbliert", "möbl. oder leer"],
        ["Unfurnished", "Partially Furnished", "Furnished", "Furnished or Unfurnished"],
    )

    return new_df


def get_owner_data():

    data = make_request()
    if data:
        owner_df = pd.DataFrame(data)
        owner_df = transform_data(owner_df)

        print(owner_df)


if __name__ == "__main__":
    get_owner_data()
