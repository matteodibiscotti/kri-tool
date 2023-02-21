import requests
import pandas as pd
import json

PRODUCTS_FILE = 'products.csv'
URL = 'https://services.nvd.nist.gov/rest/json/cpes/2.0'

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
    # data = json.dumps(response.json()['products'])

    data = response.json()['products']
    print(data[0]['cpe']['cpeName'])
    
    # with open('output.json', 'a') as file:
    #     file.write(data)