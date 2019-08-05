import json
import requests
from uber_rides.auth import AuthorizationCodeGrant
from uber_rides.session import Session
from uber_rides.client import UberRidesClient

client_id = 'V4XWn0beV4JnKHHANILZdPXSMwPgh5-Y'
scopes = 'partner.accounts'
client_secret = 'v0RvnHN-EmCD0uG_1ybPwaFGQ2_VP9Z7UORf-oTn'
redirect_url = 'http://localhost:7000/submit'

auth_flow = AuthorizationCodeGrant(client_id, scopes, client_secret, redirect_url)
api_url = auth_flow.get_authorization_url()

print('Please go to %s and authorize access.' % api_url)
authorization_response = input('Enter the full callback URL: ')

session = auth_flow.get_session(authorization_response)
client = UberRidesClient(session, sandbox_mode=True)
credentials = session.oauth2credential

response = client.get_driver_trips()
trips = response.json

print(history)
