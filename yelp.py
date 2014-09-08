#!/usr/bin/env python

# -*- coding: utf-8 -*-

import argparse
import json
import pprint
import sys
import urllib
import urllib2

import oauth2


API_HOST = 'api.yelp.com'
DEFAULT_TERM = 'food'
DEFAULT_LOCATION = 'Berkeley, CA'
SEARCH_LIMIT = 20
SEARCH_PATH = '/v2/search/'
BUSINESS_PATH = '/v2/business/'

# OAuth credential placeholders that must be filled in by users.
CONSUMER_KEY = '4XuQCNLuix3IJzy9pliQDw'
CONSUMER_SECRET = 'O4CtE6Fh-r17r1tfzm7djGPnyDc'
TOKEN = 'DTnRLARVHS8M_AD35xBnSomkwAvYHote'
TOKEN_SECRET = 'N8Z0LQ3Jlaus7Uk2l5gYTYqOqAs'

def request(host, path, url_params=None):
    """Prepares OAuth authentication and sends the request to the API.

    Args:
        host (str): The domain host of the API.
        path (str): The path of the API after the domain.
        url_params (dict): An optional set of query parameters in the request.

    Returns:
        dict: The JSON response from the request.

    Raises:
        urllib2.HTTPError: An error occurs from the HTTP request.
    """
    url_params = url_params or {}
    encoded_params = urllib.urlencode(url_params)

    url = 'http://{0}{1}?{2}'.format(host, path, encoded_params)

    consumer = oauth2.Consumer(CONSUMER_KEY, CONSUMER_SECRET)
    oauth_request = oauth2.Request('GET', url, {})
    oauth_request.update(
        {
            'oauth_nonce': oauth2.generate_nonce(),
            'oauth_timestamp': oauth2.generate_timestamp(),
            'oauth_token': TOKEN,
            'oauth_consumer_key': CONSUMER_KEY
        }
    )
    token = oauth2.Token(TOKEN, TOKEN_SECRET)
    oauth_request.sign_request(oauth2.SignatureMethod_HMAC_SHA1(), consumer, token)
    signed_url = oauth_request.to_url()

    #print 'Querying {0} ...'.format(url)

    conn = urllib2.urlopen(signed_url, None)
    try:
        response = json.loads(conn.read())
    finally:
        conn.close()

    return response

def search(term, location):
    """Query the Search API by a search term and location.

    Args:
        term (str): The search term passed to the API.
        location (str): The search location passed to the API.

    Returns:
        dict: The JSON response from the request.
    """
    url_params = {
        'term': term,
        'location': location,
        'limit': SEARCH_LIMIT
    }

    return request(API_HOST, SEARCH_PATH, url_params=url_params)



def query_api(term, location):
    """Queries the API by the input values from the user.
    Args:
        term (str): The search term to query.
        location (str): The location of the business to query.
    """
    response = search(term, location)
   
    return response
    #pprint.pprint(response, indent=2)


def main():
    parser = argparse.ArgumentParser()

    parser.add_argument('-q', '--term', dest='term', default=DEFAULT_TERM, type=str, help='Search term (default: %(default)s)')
    parser.add_argument('-l', '--location', dest='location', default=DEFAULT_LOCATION, type=str, help='Search location (default: %(default)s)')

    input_values = parser.parse_args()

    try:
        query_api(input_values.term, input_values.location)
    except urllib2.HTTPError as error:
        sys.exit('Encountered HTTP error {0}. Abort program.'.format(error.code))


if __name__ == '__main__':
    main()