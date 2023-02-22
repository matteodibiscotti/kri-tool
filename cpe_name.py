import requests
import pandas as pd
import json

PRODUCTS_FILE = 'products.csv'
URL = 'https://services.nvd.nist.gov/rest/json/cpes/2.0'

def get_cpe_names():
    products = pd.read_csv(PRODUCTS_FILE)

    for index, row in products.iterrows():
        owner = row['owner']
        product = row['product']
        version = row['version']

        cpe_string = f'cpe:2.3:*:{owner}:{product}:{version}:*:*:*:*:*:*:*'

        parameters = {
            'cpeMatchString': cpe_string
        }

        response = requests.get(url=URL, params=parameters)

        data = response.json()['products']  # list of dictionaries

        cpeNames = []

        for i in data:
            cpeNames.append(data[0]['cpe']['cpeName'])
        
        return cpeNames



# get len of data
# loop through and get the 

# print(data[0]['cpe']['cpeName'])

# with open('output.json', 'a') as file:
#     file.write(data)