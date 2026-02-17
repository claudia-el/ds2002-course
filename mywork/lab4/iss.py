#!/usr/bin/env python

import requests
import json
import pandas as pd
import sys
import logging
import os

logger = logging.getLogger()
logger.setLevel(logging.INFO)

formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)
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
        filename = "iss_data.json"
            
        with open(filename, 'w') as f:
            json.dump(iss_data, f, indent=2)
        logging.info(f"Extracted raw data and saved to {filename}")

        return filename
                     
    except requests.exceptions.HTTPError as e:
        logging.error("HTTP error occurred:", e)
    except requests.exceptions.RequestException as e:
        logging.error("A request error occurred:", e)
    except Exception as e:
        logging.error("An unexpected error occurred:", e)

    

def transform(json_file):

    logging.info("Cleaning and organizing data...")

    with open(json_file) as f:
        data = json.load(f)

    df = pd.json_normalize(data)
    
    if 'timestamp' in df.columns:
        df['timestamp'] = pd.to_datetime(df['timestamp'], unit='s')

    return df


def load(df):

    csv_file = get_output_file()

    if os.path.exists(csv_file):
        df.to_csv(csv_file, mode='a', header=False, index=False)
    else:
        df.to_csv(csv_file, index=False)
    
    logging.info(f"Loaded transformed data (saved to {csv_file})")

def main():
    json = extract()

    df = transform(json)

    load(df)

if __name__ == "__main__":
    main()
    












