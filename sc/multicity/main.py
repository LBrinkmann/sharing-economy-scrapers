import pandas as pd
import datetime
from collections import OrderedDict
from .. io import store_request, get_request, get_json, save_to_csv

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


def scrap():
    rj = get_request(req)
    store_request(rj, 'multicity')


def get_cars(d):
    for c in d['data']:
        yield c, d['meta']


def car_to_row(d, meta):
    split_model = d['value']['vehicle']['name'].split(' ')
    o = OrderedDict([
        ('gid', "{}_{}".format(meta['type'], d['value']['vehicle']['uid'])),
        ('id', d['value']['vehicle']['uid']),
        ('licensePlate', d['value']['vehicle']['license']),
        ('timestamp', meta['timestamp']),
        ('provider', meta['type']),
        ('latitude', d['location']['latitude']),
        ('longitude', d['location']['longitude']),
        ('manufactor', 'PSA'),
        ('brand', split_model[0]),
        ('model', split_model[1]),
        ('fuelType', d['value']['vehicle']['powerType']),
        ('fuelLevel', d['value']['vehicle']['fillLevel'])
    ])
    return o


def parse(dayiso=None):
    if dayiso is None:
        dayiso = datetime.date.today().isoformat()
    rec = [car_to_row(d, m) for j in get_json(dayiso, 'multicity')
           for d, m in get_cars(j)]
    df = pd.DataFrame.from_records(rec)
    save_to_csv(df, 'raw_rec', dayiso, 'multicity')
