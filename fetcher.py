import requests
import logging
import pandas as pd


logger = logging.getLogger("datafetcher.py")

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

    # Drop unncessary columns
    new_df = df.drop(df.columns.difference(keep_cols), axis=1).rename(
        columns=rename_cols
    )

    ## Converting Data types - To float
    new_df[["no_of_rooms", "cold_rent", "ancillary_costs", "deposit"]] = new_df[
        ["no_of_rooms", "cold_rent", "ancillary_costs", "deposit"]
    ].astype(float)

    # Converting Data type - To int
    new_df[["room_id", "room_type_code", "status", "size_in_sq_mtrs"]] = new_df[
        ["room_id", "room_type_code", "status", "size_in_sq_mtrs"]
    ].astype(int)

    # Converting Data type - To data
    new_df["available_from"] = pd.to_datetime(new_df["available_from"]).dt.date

    # Create Warm-rent column
    new_df["warm_rent"] = new_df["cold_rent"] + new_df["ancillary_costs"]

    # Replace German values to english
    new_df["furnishing"].replace(
        ["leer", "teilmöbliert", "möbliert", "möbl. oder leer"],
        ["Unfurnished", "Partially Furnished", "Furnished", "Furnished or Unfurnished"],
    )

    return new_df[
        [
            "room_id",
            "room_type_code",
            "room_type",
            "is_share_apartment",
            "no_of_rooms",
            "furnishing",
            "status",
            "available_from",
            "cold_rent",
            "ancillary_costs",
            "warm_rent",
            "deposit",
            "street",
            "postal_code",
            "city",
            "landlord_last_name",
            "landlord_first_name",
            "mobile_number",
            "email_id",
            "female_only",
            "male_only",
            "couple_allowed",
            "foreigner_allowed",
        ]
    ]


def get_owner_data(export_excel=True) -> pd.DataFrame:

    data = make_request()
    if data:
        owner_df = pd.DataFrame(data)
        owner_df = transform_data(owner_df)

        if export_excel:
            logger.info("Exporting data to Excel...")
            owner_df.to_excel("owner_details.xlsx", index=False)

        logger.info("Retrieve Owner's data successfully...")
        return owner_df
    else:
        raise Exception("No Data Found")
