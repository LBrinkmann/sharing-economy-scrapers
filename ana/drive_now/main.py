import pandas as pd
import numpy as np
import simplejson
import os
from collections import OrderedDict


def give_json():
    cwd = os.getcwd()
    path = os.path.join(cwd, "data")
    for f in os.listdir(path):
        if f.startswith("drive_now"):
            pf = os.path.join(path, f)
            with open(pf, 'r') as o:
                d = simplejson.load(o)
            yield d


def get_cars(d):
    i = 0
    for c in d['data']['cars']['items']:
        yield c, d['meta']

def car_to_row(d, meta):
    o = OrderedDict([
        ('id', d['id']),
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

def main():
    rec = [car_to_row(d, m) for j in give_json() for d, m in get_cars(j)]
    df = pd.DataFrame.from_records(rec)
    return df
