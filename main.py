import logging

from dotenv import load_dotenv

load_dotenv()

logging.basicConfig(
    level=logging.DEBUG, format="%(asctime)s | %(levelname)s | %(name)s : %(message)s"
)

from fetcher import get_owner_data
from mailer import send_email

logger = logging.getLogger(__name__)

if __name__ == "__main__":

    logger.info("Starting WG-Mailer")

    data = get_owner_data()

    filter_data = data[~data["email_id"].isna()]

    for _, row in filter_data.iterrows():
        send_email(row)
