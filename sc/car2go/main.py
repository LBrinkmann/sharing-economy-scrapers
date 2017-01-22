from .. io import store_request, get_request

req = {
    'url': 'https://www.car2go.com/api/v2.1/vehicles?oauth_consumer_key=car2gowebsite&format=json&loc=berlin',
    'headers': {
        'Accept': '*/*',
        'Accept-Encoding': 'gzip, deflate, sdch, br',
        'Accept-Language': 'en-US,en;q=0.8,de;q=0.6',
        'Connection': 'keep-alive',
        'Cookie': 'optimizelyEndUserId=oeu1482362385607r0.7557060374801756; car2go.cookie.allowed=true; _ga=GA1.2.344656077.1482363012; gapv_cid=c2g_ola_de_ber_cpa_PerformanceCampaign2016_accado_accado-prospecting_micropage_CarOwnership_skyscraper_none_none_none_none_none; LtpaToken2=8AFFEXftaIVrNWB/Ds9R+bZhx9qqDAvSv3xHM/5zeyJwtIjPPzYUU66pZ+28+y9uSv/AwnsT5BmAlBp4cKSIRPxSFYNUtB/XVPAqdfuAm1UZv+5/QzmYzKxFwzvnDQQ+t3jbFooJw5p/IVg8nmZPEnsMZTciMBaoLnui5aNgE13OCFgNLvzlic8voXMrfbzxY589Nx8W6fPbiYtzBY01uxSAKqGLZnGl4CJFrRo1v5iCsvFv27IrxxFsfDc+Hp3Aoe2PD6BLV5ntNIk9QhbT6sYZGddjMGYRlzmqYp452USABNmuWV/FqmfTzLYcs4Yg; s_sess=%20s_runr_gapv_c16%3Dc2g_ppc_de_ber_cpc_PerformanceCampaign2016_google_car2goBrandBerlin_micropage_car2go_adword_e_car2gobrand_none_none_none%3B%20s_runr_gvo_v0%3Dc2g_ppc_de_ber_cpc_PerformanceCampaign2016_google_car2goBrandBerlin_micropage_car2go_adword_e_car2gobrand_none_none_none%3B%20s_cc%3Dtrue%3B%20s_sq%3Ddms-car2go-na-prd%253D%252526c.%252526a.%252526activitymap.%252526page%25253Dna%2525253Aus%2525253Anone%2525253Aen%2525253A%252526link%25253DBerlin%252526region%25253DBODY%252526pageIDType%25253D1%252526.activitymap%252526.a%252526.c%252526pid%25253Dna%2525253Aus%2525253Anone%2525253Aen%2525253A%252526pidt%25253D1%252526oid%25253Dhttps%2525253A%2525252F%2525252Fwww.car2go.com%2525252FDE%2525252Fen%2525252Fberlin%252526ot%25253DA%3B; s_pers=%20s_vnum%3D1483225200491%2526vn%253D1%7C1483225200491%3B%20s_fid%3D1E73366374299EE9-22AD7A41479135A2%7C1545435128296%3B%20s_gnr%3D1482363128302-New%7C1545435128302%3B%20s_lv%3D1482363128305%7C1576971128305%3B%20s_lv_s%3DFirst%2520Visit%7C1482364928305%3B%20s_invisit%3Dtrue%7C1482364928310%3B; car2go.cookie.location=/DE/de/berlin; car2go.cookie.customer.context=own; JSESSIONID=0000CyVV8ybnEn8L9JEPWFU0Mtb:1a48crj16; s_sq=%5B%5BB%5D%5D; optimizelySegments=%7B%226094790303%22%3A%22none%22%2C%226092582505%22%3A%22search%22%2C%226088441276%22%3A%22false%22%2C%226103140381%22%3A%22gc%22%2C%227726456222%22%3A%22true%22%2C%227810540055%22%3A%22true%22%7D; optimizelyBuckets=%7B%228020581225%22%3A%227977246502%22%7D; optimizelyPendingLogEvents=%5B%5D; s_fid=4D7871041F9FF8D5-128B64D46D3D6FE1; s_cc=true',
        'Host': 'www.car2go.com',
        'Referer': 'https://www.car2go.com/DE/de/berlin/where/',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.95 Safari/537.36'
    }
}


def main():
    rj = get_request(req)
    store_request(rj, 'car2go')
