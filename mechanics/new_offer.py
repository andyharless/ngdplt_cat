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

from time import sleep
from local_data import cert_path

urllib3.disable_warnings()

WALLET_PORT = 9256

cert = (cert_path + '/private_wallet.crt', 
        cert_path + '/private_wallet.key')


def make_url(verb, host='localhost', port=WALLET_PORT):

    url = f'https://{host}'
    
    if port is not None:
        url += f':{port}'
    
    return url + f'/{verb}'
    

def buy_offer(amount=1, price=None, buying='NGDPLT', selling='XCH'):

    if price is None:
        os.getenv(buying + '_PRICE')

    sell_amt = price * amount

    return post_offer(sell_amt, selling, amount, buying)


def sell_offer(amount=1, price=None, selling='NGDPLT', buying='XCH'):

    if price is None:
        os.getenv(selling + '_PRICE')

    buy_amt = price * amount

    return post_offer(amount, selling, buy_amt, buying)


def post_offer(sell_amt, selling, buy_amt, buying):

    sell_factor = 1000000000000 if selling == 'XCH' else 1000
    buy_factor = 1000000000000 if buying == 'XCH' else 1000

    sell_id = os.getenv(selling)
    buy_id = os.getenv(buying)

    offer_dict = {
                  buy_id: int(buy_amt * buy_factor), 
                  sell_id: -int(sell_amt * sell_factor)
                 }
    req = {}
    req['offer'] = offer_dict

    answer = requests.post(
                make_url('create_offer_for_ids'),
                data=json.dumps(req), 
                headers={'Content-Type': 'application/json'}, 
                cert=cert, verify=False
            )

    offer = json.loads(answer.text)
    offer_text = offer['offer']
    offer_id =  offer['trade_record']['trade_id']

    req = {}
    req['offer'] = offer_text
    upload = requests.post(
            make_url('v1/offers', host='api.dexie.space', port=None),
            data=json.dumps(req),
            headers={'Content-Type': 'application/json'},
            verify=False
            )
#   TODO: Check upload response and raise exception if it failed
#   TODO: Vefity that data from upload response is consistent with offer
#   TODO: Add data from upload & offer responses to a CSV file of offers
            
    return offer_id
    
       
def cancel_offer(offer_id, fee=10000, secure=True):
    d = {}
    d['trade_id'] = offer_id
    d['fee'] = fee
    d['secure'] = secure
    answer = requests.post(
                make_url('cancel_offer'),
                data=json.dumps(d), 
                headers={'Content-Type': 'application/json'}, 
                cert=cert, verify=False
            )
    return answer

