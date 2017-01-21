import requests
import simplejson
import datetime
import os

import pkg_resources

req = {
    'url': 'https://www.multicity-carsharing.de/_denker-mc.php',
    'headers': {
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Encoding': 'gzip, deflate, sdch, br',
        'Accept-Language': 'en-US,en;q=0.8,de;q=0.6',
        'Connection': 'keep-alive',
        'Cookie':
            '_gat_UA-33909870-1=1;'
            ' wpml_referer_url=https%3A%2F%2Fwww.multicity-carsharing.de%2F; '
            '_icl_current_language=de; _ga=GA1.2.671851371.1482362397',
        'Host': 'www.multicity-carsharing.de',
        'Referer': 'https://www.multicity-carsharing.de/',
        'User-Agent':
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) '
            'AppleWebKit/537.36 (KHTML, like Gecko) '
            'Chrome/55.0.2883.95 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest'
    }
}


def get_request():
    r = requests.get(**req)
    rj = r.json()
    return rj

def store_request(requst_obj, rtype):
    now = datetime.datetime.now().isoformat()
    filename = '{}_{}.json'.format(rtype, now)
    cwd = os.getcwd()
    path = os.path.join(cwd, "data", filename)
    data = {
        'meta':
        {
            'type': rtype,
            'timestamp': now
        },
        'data': requst_obj
    }
    with open(path, 'w') as o:
        simplejson.dump(data, o)

def main():
    rj = get_request()
    store_request(rj, 'multicity')
