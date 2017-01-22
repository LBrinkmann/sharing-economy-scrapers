from .. io import store_request, get_request

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


def main():
    rj = get_request(req)
    store_request(rj, 'multicity')
