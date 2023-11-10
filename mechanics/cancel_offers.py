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

from mechanics.new_offer import make_url

urllib3.disable_warnings()

WALLET_PORT = 9256
DEFAULT_FEE = 10000
WAIT_INTERVAL = 3
MAX_WAIT = 600

cert = (cert_path + '/private_wallet.crt', 
        cert_path + '/private_wallet.key')


def cancel_offers_by_id(id_list, fee=DEFAULT_FEE, secure=True, 
                                 host='localhost', port=WALLET_PORT):

    cancelled = []
    
    for id in id_list:
    
        # Cancel offer
        print(f'\nAttempting to cancel offer {id}')
        result = cancel_offer_by_id(offer_id=id, fee=fee, secure=secure, 
                                    host=host, port=port)
        if not (hasattr(result, 'text') and json.loads(result.text)['success']):
            raise Exception('Cancel failed')
        
        # Wait for confirmation
        status = None
        waited = 0
        while status != 'CANCELLED':
            if waited > MAX_WAIT:
                raise Exception('No confirmation')
            waited += WAIT_INTERVAL
            sleep(WAIT_INTERVAL)
            status = get_offer_status(id, host=host, port=port)
        cancelled.append(id)
        print(f'Cancel succeeded for offer {id}')

    assert cancelled == id_list
            
    return cancelled


def get_offer_status(offer_id, host='localhost', port=WALLET_PORT):
    d = {}
    d['trade_id'] = offer_id
    answer = requests.post(
                make_url('get_offer'),
                data=json.dumps(d), 
                headers={'Content-Type': 'application/json'}, 
                cert=cert, verify=False
            )
    return json.loads(answer.text)['trade_record']['status']


def cancel_offer_by_id(offer_id, fee=10000, secure=True, host='localhost',
                                 port=WALLET_PORT):
                                 
    if get_offer_status(offer_id, host=host, port=port) != 'PENDING_ACCEPT':
        raise Exception('Offer not outstanding')
    
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

