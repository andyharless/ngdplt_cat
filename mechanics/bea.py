import requests
import urllib3
import json
import os
import sys

REPO_ROOT = '..'
coderoot = os.getenv("CHIA_CODE_ROOT")
if coderoot is None:
    coderoot = '../..'
sys.path.append(coderoot)
sys.path.append(REPO_ROOT)

urllib3.disable_warnings()

def make_url(verb, host='localhost', params=None, port=None):

    url = f'https://{host}'
    
    if port is not None:
        url += f':{port}'
    
    url += f'/{verb}'

    if params is not None:
        url += '?'
        for p in params:
            url += f'&{p}={params[p]}'
            
    return url
    
def get_ngdp(year=2023, quarter=3):

    host = 'apps.bea.gov/API'
    verb = 'data'
    ps = {}
    ps['UserID'] = os.getenv('BEA_KEY')
    ps['method'] = 'GetData'
    ps['datasetname'] = 'NIPA'
    ps['TableName'] = 'T10105'
    ps['Frequency'] = 'Q'
    ps['Year'] = str(year)
    ps['ResultFormat']='JSON'


    url = make_url(host=host, verb=verb, params=ps)
    
    answer = requests.post(
                url,
                headers={'Content-Type': 'application/json'}, 
                verify=False
            )
            
    result = json.loads(answer.text)
    data = result['BEAAPI']['Results']['Data']
    qtr = f'{year}Q{quarter}'
    
    ngdp = int([d for d in data if 
                d['LineNumber'] == '1' and d['TimePeriod'] == qtr
               ][0]['DataValue'].replace(',',''))
    
    return ngdp
