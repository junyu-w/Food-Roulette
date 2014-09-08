import json
import oauth2
import urllib
import urllib2
import argparse
import sys


API_HOST = 'api.yelp.com'
DEFAULT_TERM = 'dinner'
DEFAULT_CLL = '37.7833,-122.4167'
SEARCH_LIMIT = 3
SEARCH_PATH = '/v2/search/'
BUSINESS_PATH = '/v2/business/'


CONSUMER_KEY = '4XuQCNLuix3IJzy9pliQDw'
CONSUMER_SECRET = 'O4CtE6Fh-r17r1tfzm7djGPnyDc'
TOKEN = 'DTnRLARVHS8M_AD35xBnSomkwAvYHote'
TOKEN_SECRET = 'N8Z0LQ3Jlaus7Uk2l5gYTYqOqAs'

def request(host, path, url_params=None):
    url_params = url_params or {}                                   #url_params examples: {"term":"restaurant", "location":"San Francisco"}
    encoded_params = urllib.urlencode(url_params)                   #encoded_params example: "term=restaurant&location=San+Francisco"
    print encoded_params
    
    url = "http://%s%s?%s"%(host, path, encoded_params)
    print url#here we got the last part of our REQUEST url
    
    consumer = oauth2.Consumer(CONSUMER_KEY, CONSUMER_SECRET)       #create consumer
    token = oauth2.Token(TOKEN, TOKEN_SECRET)
    
    oauth_request = oauth2.Request("GET",url, {})
    oauth_request.update(
        {
            'oauth_nonce': oauth2.generate_nonce(),
            'oauth_timestamp': oauth2.generate_timestamp(),
            'oauth_token': TOKEN,
            'oauth_consumer_key': CONSUMER_KEY
        }
    )
    
    oauth_request.sign_request(oauth2.SignatureMethod_HMAC_SHA1(), consumer, token)
    signed_url = oauth_request.to_url()
    
    print "Query:%s"%(url)
    print signed_url
    
    conn = urllib2.urlopen(signed_url, None)
    try:
        response = json.loads(conn.read())
    finally:
        conn.close()

    print response
    
    return response

def search(term, cll_info):
    url_params = {
        "term": term,
        "cll": cll_info, #get latitude and longitude info   WE WILL USE GPS TO LOCATE
        "limit": SEARCH_LIMIT
    }
    return request(API_HOST, SEARCH_PATH, url_params=url_params)

def query_api(term, cll):
    response = search(term, cll)
    print response



def main():
    parser = argparse.ArgumentParser();
    parser.add_argument('-q', '--term', dest='term', default=DEFAULT_TERM, type=str, help='Search term (default: %(default)s)')
    parser.add_argument('-l', '--cll', dest='cll', default=DEFAULT_CLL, type=str, help='Search cll (default: %(default)s)')
    input_values = parser.parse_args()
    
    search_term = input_values.term
    search_cll = input_values.cll
    try:
        query_api(search_term, search_cll)
    except urllib2.HTTPError as error:
        sys.exit('Encountered HTTP error {0}. Abort program.'.format(error.code))
    
    
    
    
if __name__ == '__main__':
    main()
    
    
    
    
    
    
    