import requests
import pandas as pd

PRODUCTS_FILE = 'products.csv'
URL = 'https://services.nvd.nist.gov/rest/json/cpematch/2.0'

products = pd.read_csv(PRODUCTS_FILE)

for index, row in products.iterrows():
    owner = row['owner']
    product = row['product']
    version = row['version']

    cpe_string = f'cpe:2.3:*:{owner}:{product}:{version}:*:*:*:*:*:*:*'

    parameters = {
        'matchStringSearch': cpe_string
    }

    response = requests.get(url=URL, params=parameters)
    data = str(response.json())
    
    with open('output.txt', 'a', encoding='utf-8') as file:
        file.write(data)