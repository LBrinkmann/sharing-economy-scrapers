import pandas as pd
import simplejson
import datetime
import os
import requests


def save_to_csv(df, subfolder, dayiso, rtype):
    path = get_data_path(subfolder, dayiso)
    filename = '{}_{}.csv'.format(rtype, dayiso)
    file_path = os.path.join(path, filename)
    df.to_csv(file_path)


def load_csv(subfolder, dayiso, rtype):
    path = get_data_path(subfolder, dayiso)
    filename = '{}_{}.csv'.format(rtype, dayiso)
    file_path = os.path.join(path, filename)
    pd.DataFrame.read_csv(file_path)


def get_data_path_alldays(subfolder):
    if 'SC_DATA_DIR' not in os.environ:
        cwd = os.getcwd()
        path = os.path.join(cwd, "data", subfolder)
    else:
        pathbase = os.environ['SC_DATA_DIR']
        path = os.path.join(pathbase, subfolder)
    for f in os.listdir(path):
        yield f


def get_data_path(subfolder=None, dayiso=None, makeifnotexist=True):
    if 'SC_DATA_DIR' not in os.environ:
        cwd = os.getcwd()
        path = os.path.join(cwd, "data")
    else:
        path = os.environ['SC_DATA_DIR']
    if subfolder is not None:
        path = os.path.join(path, subfolder)
    if dayiso is not None:
        path = os.path.join(path, dayiso)
    if not os.path.exists(path) and makeifnotexist:
        os.makedirs(path)
    return path


def store_request(requst_obj, rtype):
    now = datetime.datetime.now()
    nowiso = datetime.datetime.now().isoformat()
    dayiso = now.date().isoformat()
    filename = '{}_{}.json'.format(rtype, nowiso)
    path = get_data_path('raw', dayiso)
    data = {
        'meta':
        {
            'type': rtype,
            'timestamp': nowiso
        },
        'data': requst_obj
    }
    file_path = os.path.join(path, filename)
    with open(file_path, 'w') as o:
        simplejson.dump(data, o)


def get_request(req):
    r = requests.get(**req)
    rj = r.json()
    return rj


def get_json(dayiso, startswith=''):
    path = get_data_path('raw', dayiso)
    for f in os.listdir(path):
        if f.startswith(startswith):
            pf = os.path.join(path, f)
            with open(pf, 'r') as o:
                d = simplejson.load(o)
            yield d
