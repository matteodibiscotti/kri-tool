import requests
import pandas as pd
import json

PRODUCTS_FILE = 'products.csv'
URL = 'https://services.nvd.nist.gov/rest/json/cpes/2.0'

def get_cpe_names():
    products = pd.read_csv(PRODUCTS_FILE)
    product_data = {}
    cpeNames = []

    for index, row in products.iterrows():
        owner = row['owner']
        product = row['product']
        version = row['version']

        cpe_string = f'cpe:2.3:*:{owner}:{product}:{version}:*:*:*:*:*:*:*'
        key = f'{product}{version}'
        
        parameters = {
            'cpeMatchString': cpe_string
        }

        response = requests.get(url=URL, params=parameters)
        response.raise_for_status()
        data = response.json()['products']  # list of dictionaries

        for i in range(len(data)):
            cpeNames.append(data[i]['cpe']['cpeName'])
        
        product_data[key] = cpeNames
        
    return product_data
