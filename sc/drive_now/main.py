import pandas as pd
import datetime
from collections import OrderedDict
from .. io import store_request, get_request, get_json, save_to_csv

req = {
    'url': 'https://api2.drive-now.com/cities/6099?expand=full',
    'headers': {
        'Accept': 'application/json;v=1.8',
        'Accept-Encoding': 'gzip, deflate, sdch, br',
        'Accept-Language': 'en-US,en;q=0.8,de;q=0.6',
        'Connection': 'keep-alive',
        'Host': 'api2.drive-now.com',
        'Origin': 'https://de.drive-now.com',
        'Referer': 'https://de.drive-now.com/',
        'User-Agent':
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6)'
            ' AppleWebKit/537.36 (KHTML, like Gecko)'
            ' Chrome/55.0.2883.95 Safari/537.36',
        'X-Api-Key': 'adf51226795afbc4e7575ccc124face7',
        'X-Language': 'de'
    }
}


def scrap():
    rj = get_request(req)
    store_request(rj, 'drive_now')


def get_cars(d):
    for c in d['data']['cars']['items']:
        yield c, d['meta']


def car_to_row(d, meta):
    o = OrderedDict([
        ('gid', "{}_{}".format(meta['type'], d['id'])),
        ('id', d['id']),
        ('licensePlate', d['licensePlate']),
        ('timestamp', meta['timestamp']),
        ('provider', meta['type']),
        ('latitude', d['latitude']),
        ('longitude', d['longitude']),
        ('address0', d['address'][0] if len(d['address']) > 0 else None),
        ('address1', d['address'][1] if len(d['address']) > 1 else None),
        ('address2', d['address'][2] if len(d['address']) > 2 else None),
        ('manufactor', d['make']),
        ('brand', d['series']),
        ('model', d['modelName']),
        ('transmission', d['transmission']),
        ('fuelType', d['fuelType']),
        ('fuelLevel', d['fuelLevel']),
        ('estimatedRange', d['estimatedRange']),
        ('isCharging', d['isCharging']),
        ('innerCleanliness', d['innerCleanliness']),
    ])
    return o


def parse(dayiso=None):
    if dayiso is None:
        dayiso = datetime.date.today().isoformat()
    rec = [car_to_row(d, m) for j in get_json(dayiso, 'drive_now')
           for d, m in get_cars(j)]
    df = pd.DataFrame.from_records(rec)
    save_to_csv(df, 'raw_rec', dayiso, 'drive_now')
