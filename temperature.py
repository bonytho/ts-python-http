import requests
import config
import random
import time
import json

temperature = random.randint(1,31);
preassure = random.randint(21,71);
while True:
	temperature = temperature + 5;
	preassure = preassure + 5;
	print "Temperature : " + str(temperature) + ", Preassure : " + str(preassure);
	payload = '{ "api_key" : "'+ config.WRITEKEY + '","field1":' + str(temperature) + ', "field2":' +str(preassure) + '}'
	headers = {'Content-type': 'application/json'}
	print payload
	response = requests.request("POST", 'https://api.thingspeak.com/update', data=payload, headers=headers);
	print response;
	time.sleep(40);