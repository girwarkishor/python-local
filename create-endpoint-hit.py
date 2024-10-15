import json
import logging

import requests
from socket import timeout

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")


def fetch_data_api(url):
    try:
        # set timeout for the request
        response = requests.get(url, timeout=5)

        # log the request status
        logging.info(f"Fetching data from {url}")

        # Check if the request was successful
        if response.status_code == 200:
            # Parse the JSON response
            data = response.json()

            # log the success
            logging.info(f"Data fetching successfully, Total records: {len(data)}")

            # Pretty-print the data
            print(json.dumps(data, indent=1))
        else:
            logging.error(f"Failed to fetch data. Status code: {response.status_code}")

    except requests.exceptions.Timeout:
        # Handle timeout error
        logging.error("The request timed out. Please try again later.")

    except requests.exceptions.RequestException as e:
        # Handle any other request errors
        logging.error(f"An error occurred: {e}")


# URL of the dummy API
url = "https://jsonplaceholder.typicode.com/photos"

# Call the function to fetch data
fetch_data_api(url)
