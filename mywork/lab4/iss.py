#!/usr/bin/env python

import requests
import json
import pandas as pd
import sys
import logging

formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
console_handler = logging.StreamHandler()
console_handler.setFormatter(formatter)
logging.basicConfig(handlers=[console_handler])


def get_output_file():
    
    try:
        output_file = sys.argv[1]
    
    except IndexError:
        logging.error(f"Usage: python {sys.argv[0]} <json_file>")
        sys.exit(1)
    
    return output_file

def extract():

    url = 'http://api.open-notify.org/iss-now.json'

    logging.info(f"Getting data from {url}")
        
    try:
        response = requests.get(url)
        iss_data = response.json()
            
        with open('iss_data', 'w') as f:
            json.dump(iss_data, f, indent=2)
        logging.info(f"Extracted raw data and saved to {iss_data}")
                     
    except requests.exceptions.HTTPError as e:
        logging.error("HTTP error occurred:", e)
    except requests.exceptions.RequestException as e:
        logging.error("A request error occurred:", e)
    except Exception as e:
        logging.error("An unexpected error occurred:", e)






