import requests
import pandas as pd
import cpe_name
from time import sleep
import os

API_KEY = os.getenv('NVD_API_KEY')
URL = 'https://services.nvd.nist.gov/rest/json/cves/2.0'
product_data = cpe_name.get_cpe_names()
HEADERS = {'apiKey': API_KEY}

def main():
    product_ids = list(product_data.keys())

    col_headers = ['product', 'version', 'type', 'cve_id', 'description', 'baseScore', 'baseSeverity']
    output_df = pd.DataFrame(columns=col_headers)

    count = 0

    for product in product_ids:
        
        for sub_product in product_data[product]:

            split_id = sub_product.split(':')

            parameters = {
                'cpeName': sub_product
            }   

            response = requests.get(url=URL, params=parameters, headers=HEADERS)
            response.raise_for_status()

            cve_id = response.json()['vulnerabilities'][0]['cve']['id']
            description = response.json()['vulnerabilities'][0]['cve']['descriptions'][0]['value']
            base_score = response.json()['vulnerabilities'][0]['cve']['metrics']['cvssMetricV2'][0]['cvssData']['baseScore']
            base_severity = response.json()['vulnerabilities'][0]['cve']['metrics']['cvssMetricV2'][0]['baseSeverity']
            product = sub_product.split(":")[4]
            version = sub_product.split(":")[5]
            sub_category = ':'.join(split_id[6:])

            if base_score >= 8:
                output_df.loc[len(output_df.index)] = [product, version, sub_category, cve_id, description, 
                                                    base_score, base_severity]

            count += 1

            print(f"COMPLETED {count}: {product} {version}: Type: {sub_category}")

    output_df.to_csv('results.csv', index=False)

if __name__ == "__main__":
    main()
