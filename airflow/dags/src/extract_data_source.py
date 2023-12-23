from airflow.models import Variable
from airflow.contrib.hooks.gcs_hook import GoogleCloudStorageHook

import requests
import json
from datetime import datetime
import os
import logging



def get_data(**kwargs):
    """
    Query openweathermap.com's API and to get the weather for
    Jakarta, ID and then dump the json to the /src/data/ directory
    with the file name "<today's date>.json"
    """

    # My API key is defined in my config.py file.
    key = "xxxxx"
    logging.info("API_KEY={}".format(key))
    return "textx"

   


if __name__ == "__main__":
    get_data()