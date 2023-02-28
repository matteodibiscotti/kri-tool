import requests
import pandas as pd
import os

API_KEY = os.getenv('NVD_API_KEY')
PRODUCTS_FILE = 'products.csv'
URL = 'https://services.nvd.nist.gov/rest/json/cpes/2.0'
HEADERS = {'apiKey': API_KEY}

def get_cpe_names():
    products = pd.read_csv(PRODUCTS_FILE)
    product_data = {}
    

    for index, row in products.iterrows():
        cpeNames = []
        owner = row['owner']
        product = row['product']
        version = row['version']

        cpe_string = f'cpe:2.3:*:{owner}:{product}:{version}:*:*:*:*:*:*:*'
        key = f'{product}{version}'
        
        parameters = {
            'cpeMatchString': cpe_string
        }

        response = requests.get(url=URL, params=parameters, headers=HEADERS)
        response.raise_for_status()
        data = response.json()['products']  # list of dictionaries

        for i in range(len(data)):
            cpeNames.append(data[i]['cpe']['cpeName'])
        
        product_data[key] = cpeNames
        
    return product_data
