# Find the total number of different-different Aircraft
import requests
import json
import logging
from socket import timeout

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")


def air_craft(url):
    try:
        response = requests.get(url, timeout=5)
        logging.info(f"Fetching data from {url}")
        # print(response.json())
        if response.status_code == 200:
            data = response.json()
            logging.info(f"Data fetching successful, total number of records {len(data)}")
            print(json.dumps(data, indent=1))
            totalIss = []
            totalTiangong = []
            for i in data["people"]:
                if i["craft"] == "ISS":
                    totalIss.append(i["craft"])
                else:
                    totalTiangong.append(i["craft"])
            print(f"Total number of ISS Aircraft = {len(totalIss)}")
            print(f"Total number of Tiangong Aircraft = {len(totalTiangong)}")
        else:
            logging.error(f"Failed to fetch the data {response.status_code}")
    except requests.exceptions.Timeout:
        logging.info("The request timeout, please try again later")
    except requests.exceptions.RequestException as e:
        logging.info(f"An error occurred: {e}")


astor_url = "http://api.open-notify.org/astros.json"

air_craft(astor_url)
