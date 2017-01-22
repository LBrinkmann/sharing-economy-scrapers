from .. io import store_request, get_request


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


def main():
    rj = get_request(req)
    store_request(rj, 'drive_now')
