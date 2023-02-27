import requests
import pandas as pd
import cpe_name
import json
from time import sleep
import os

API_KEY = os.getenv('NVD_API_KEY')
URL = 'https://services.nvd.nist.gov/rest/json/cves/2.0'
product_data = cpe_name.get_cpe_names()
HEADERS = {'apiKey': API_KEY}

def main():
    product_ids = list(product_data.keys())

    for product in product_ids:
        for sub_product in product_data[product]:

            print(sub_product)
            # sleep(1)

            parameters = {
                'cpeName': sub_product
            }   

            response = requests.get(url=URL, params=parameters, headers=HEADERS)
            response.raise_for_status()

            cve_id = response.json()['vulnerabilities'][0]['cve']['id']
            description = response.json()['vulnerabilities'][0]['cve']['descriptions'][0]['value']
            base_score = response.json()['vulnerabilities'][0]['cve']['metrics']['cvssMetricV2'][0]['cvssData']['baseScore']
            base_severity = response.json()['vulnerabilities'][0]['cve']['metrics']['cvssMetricV2'][0]['baseSeverity']

            print(sub_product) # split string on colon and extract product name and version
            print(cve_id)
            print(description)
            print(base_score)
            print(base_severity)

    

    # data = json.dumps(response.json())


    # # print(json.dumps(data))
    # with open('output.json', 'a') as file:
    #     file.write(data)

    # print(product_ids)

if __name__ == "__main__":
    main()


'''
apache,http_server,2.4.54
f5,nginx,1.23.2
isc,bind,9.19.6

return a list of vulnerabilities with cvss of 8 or more for the past 30 days

https://services.nvd.nist.gov/rest/json/cves/2.0?cpeName=cpe:2.3:a:isc:bind:9.7.1:p1:*:*:*:*:*:*
'''

'''
cpe_name.py returns a dictionary of lists
in main.py, create a list of the keys
loop through the keys
each product may have multiple CPE names so in the loop get the len of the value and loop through that to get all the CVE info

we want to output it as a csv file so create 
'''