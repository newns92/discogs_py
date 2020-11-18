import os
import sys
# import discogs_client
# from discogs_client.exceptions import HTTPError
import oauth2 as oauth

from urllib import request
from urllib.parse import parse_qsl
from urllib.parse import urlparse




def read_keys():
    print(os.getcwd())
    file = open('..\discogs_keys.txt', 'r')
    lines = file.readlines()
    # for line in file:
    consumer_key = lines[0].split(":")[1]
    consumer_secret = lines[1].split(":")[1]
    print(consumer_key)
    print(consumer_secret)

    """https://github.com/jesseward/discogs-oauth-example/blob/master/discogs_client_example.py"""
    # A user-agent is required with Discogs API requests. Be sure to make your
    # user-agent unique, or you may get a bad response.
    user_agent = 'snewns_discogs_api_example/2.0'

    # # instantiate client object
    # d = discogs_client.Client(user_agent)
    # # d = discogs_client.Client('ExampleApplication/0.1')
    #
    # # specify key + secret
    # d.set_consumer_key(consumer_key, consumer_secret)
    # print(d.get_authorize_url())

    # create oauth Consumer and Client objects using
    consumer = oauth.Consumer(consumer_key, consumer_secret)
    client = oauth.Client(consumer)

    """defined by discogs API docs"""
    request_token_url = 'https://api.discogs.com/oauth/request_token'
    authorize_url = 'https://www.discogs.com/oauth/authorize'
    access_token_url = 'https://api.discogs.com/oauth/access_token'

    # pass in your consumer key and secret to the token request URL. Discogs returns
    # an ouath_request_token as well as an oauth request_token secret.
    resp, content = client.request(request_token_url, 'POST', headers={'User-Agent': user_agent})

    if resp['status'] != '200':
        sys.exit('Invalid response {0}.'.format(resp['status']))

    request_token = dict(parse_qsl(content.decode('utf-8')))

    print(' == Request Token == ')
    print(f'    * oauth_token        = {request_token["oauth_token"]}')
    print(f'    * oauth_token_secret = {request_token["oauth_token_secret"]}')
    print()

if __name__ == '__main__':
    read_keys()
