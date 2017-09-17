import os
import json
import threading
import requests
import json



ENDPOINT = 'https://sandbox.unbabel.com/tapi/v2/'

HEADERS = {
    'Authorization': 'ApiKey {0}:{1}'.format('backendchallenge', '711b8090e84dcb4981e6381b59757ac5c75ebb26'),
    'Content-Type': 'application/json'
}



def post_translation(text, lang):

	data = {"text": text, "target_language": lang}
	p = requests.post(ENDPOINT+'mt_translation/', headers = HEADERS, data = json.dumps(data))
	#print (dir(p))
	#print (p.url)
	#print (p.headers)
	#print (p.reason)
	if p and (p.status_code == 201): # to check that the request is successful, using requests
		return p.json()
	else:
		return None


def get_translation(uid):
	response = requests.get(ENDPOINT+'mt_translation/'+uid, headers = HEADERS)

	if response and (response.status_code == 200): # to check that the request is successful, using requests
		return response.json()
	else:
		return None


post_translation("Hello, world", "pt")