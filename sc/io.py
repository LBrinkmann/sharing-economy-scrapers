import simplejson
import datetime
import os
import requests


def store_request(requst_obj, rtype):
    now = datetime.datetime.now()
    nowiso = datetime.datetime.now().isoformat()
    dayiso = now.date().isoformat()
    filename = '{}_{}.json'.format(rtype, nowiso)
    if 'SC_DATA_DIR' not in os.environ:
        cwd = os.getcwd()
        path = os.path.join(cwd, "data", dayiso)
    else:
        pathbase = os.environ['SC_DATA_DIR']
        path = os.path.join(pathbase, dayiso)
    data = {
        'meta':
        {
            'type': rtype,
            'timestamp': nowiso
        },
        'data': requst_obj
    }
    if not os.path.exists(path):
        os.makedirs(path)
    file_path = os.path.join(path, filename)
    with open(file_path, 'w') as o:
        simplejson.dump(data, o)


def get_request(req):
    r = requests.get(**req)
    rj = r.json()
    return rj
