#!/usr/bin/env python

import requests
import json
import sys
import logging
import os
import mysql.connector
from mysql.connector import Error
import datetime

#initialize sql
DBHOST = os.environ.get('DBHOST')
DBUSER = os.environ.get('DBUSER')
DBPASS = os.environ.get('DBPASS')
DB = "iss"
db = mysql.connector.connect(host=DBHOST, user=DBUSER, password=DBPASS, database=DB)

logger = logging.getLogger()
logger.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)
console_handler.setFormatter(formatter)

logging.basicConfig(handlers=[console_handler])


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

        return iss_data
                     
    except requests.exceptions.HTTPError as e:
        logging.error("HTTP error occurred:", e)
    except requests.exceptions.RequestException as e:
        logging.error("A request error occurred:", e)
    except Exception as e:
        logging.error("An unexpected error occurred:", e)



def load(cursor, reporter_id): 

    data = extract()

    message = data.get("message")
    latitude = float(data["iss_position"]["latitude"])
    longitude = float(data["iss_position"]["longitude"])
    
    timestamp_unix = data.get("timestamp")
    timestamp = datetime.datetime.utcfromtimestamp(timestamp_unix).strftime("%Y-%m-%d %H:%M:%S")

    insert_query = """
        INSERT INTO locations (message, latitude, longitude, timestamp, reporter_id)
        VALUES (%s, %s, %s, %s, %s)
    """
    cursor.execute(insert_query, (message, latitude, longitude, timestamp, reporter_id))

    db.commit()

    logging.info(f"Loaded transformed data")

def register_reporter(cursor, table, reporter_id, reporter_name):

    select_query = f"SELECT reporter_id FROM {table} WHERE reporter_id = %s"
    cursor.execute(select_query, (reporter_id,))
    result = cursor.fetchone()

    try:
        if result is None:
            insert_query = f"INSERT INTO {table} (reporter_id, reporter_name) VALUES (%s, %s)"
            cursor.execute(insert_query, (reporter_id, reporter_name))
            logging.info(f"Inserted reporter {reporter_name} with ID {reporter_id}")
        
        else:
            logging.info(f"Reporter ID {reporter_id} already exists, skipping insertion")
    
    except Error as e:
        print("MySQL Error:", str(e))

     

def main():

    reporter_id = "dke5td"  
    reporter_name = "Claudia"
    cursor = db.cursor() 

    register_reporter(cursor, "reporters", reporter_id, reporter_name)
    db.commit()

    load(cursor, reporter_id)  
    
    cursor.close()   
    db.close()


if __name__ == "__main__":
    main()
    












