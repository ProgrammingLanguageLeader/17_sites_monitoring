import whois
import whois.parser
import requests
import requests.exceptions
import argparse
from datetime import datetime
from datetime import timedelta


def load_urls(path):
    try:
        urls = []
        with open(path, 'r', encoding='utf-8') as file:
            for line in file.readlines():
                urls.append(line.strip())
        return urls
    except IOError:
        return None


def get_server_status(url):
    try:
        return requests.get(url).status_code
    except requests.exceptions.RequestException:
        return None


def get_domain_expiration_date(domain_name):
    try:
        response = whois.whois(domain_name)
    except whois.parser.PywhoisError:
        return None
    try:
        return response.expiration_date[0]
    except TypeError:
        return response.expiration_date


def parse_args():
    parser = argparse.ArgumentParser(
        description='A script enabling you to check sites health. Site is '
                    'healthy if it responses HTTP status 200 and its domain '
                    'name expires in more than 1 month'
    )
    parser.add_argument(
        'urls_path',
        help='A path to the file which contains urls to check'
    )
    return parser.parse_args()


def check_health(url):
    days_minimum = 31
    ok_status = 200
    expiration_date = get_domain_expiration_date(url)
    if not expiration_date:
        return '{}: unable to fetch expiration date'.format(url)
    days_to_expiration = expiration_date - datetime.today()
    server_status = get_server_status(url)
    if not server_status:
        return '{}: unable to connect to the server. ' \
               'Check the URL, please'.format(url)
    expiration_date_is_ok = days_to_expiration >= timedelta(days_minimum)
    if server_status == ok_status and expiration_date_is_ok:
        return '{} is healthy'.format(url)
    if server_status != ok_status:
        return '{} server does not response 200 HTTP code'.format(url)
    if not expiration_date_is_ok:
        return '{} domain expires in less than 1 month'.format(url)


if __name__ == '__main__':
    args = parse_args()
    urls = load_urls(args.urls_path)
    if not urls:
        exit('Unable to read {}'.format(args.urls_path))
    for url in urls:
        print(check_health(url))
