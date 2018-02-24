import json
import datetime

import urllib.request
import urllib.parse
import json

import keys

# --------- User Settings ---------
BUCKET_KEY = keys.BUCKET_KEY
ACCESS_KEY = keys.ACCESS_KEY

# ---------------------------------

def get_conditions():
	api_conditions_url = "https://min-api.cryptocompare.com" + "/data/pricemulti?fsyms=ETH,BTC,LTC,XRB,ELA,XRP&tsyms=USD"
	try:
		f = urllib.request.urlopen(api_conditions_url)
	except:
		print("Failed to get conditions")
		return False
	json_conditions = f.read()
	f.close()
	return json.loads(json_conditions)

def tracker(event, context):
	conditions = get_conditions()

	if (conditions != False):
		payload = urllib.parse.urlencode({'ETH USD':conditions['ETH']['USD'],'BTC USD':conditions['BTC']['USD'],'LTC USD':conditions['LTC']['USD'],'XRB USD':conditions['XRB']['USD'], 'ELA USD':conditions['ELA']['USD'], 'XRP USD':conditions['XRP']['USD']})
		payload = payload.encode('ascii')
		url = 'https://groker.initialstate.com/api/events?accessKey=' + ACCESS_KEY + '&bucketKey=' + BUCKET_KEY
		urllib.request.urlopen(url,payload)
		exit()

	body = {
		"message": "tracker triggered"
	}

	response = {
		"statusCode": 200,
		"body": json.dumps(body)
	}

	return response

def timepls(event, context):
    current_time = datetime.datetime.now().time()
    body = {
        "message": "Hello, the current time is " + str(current_time)
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response
