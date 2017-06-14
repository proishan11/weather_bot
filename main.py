import sys, json, traceback, requests
from flask import Flask, request

app = Flask(__name__)
FB_ACCESS_TOKEN = 'EAAEbJLBq7pIBAKssZBhQLZA89RaTgcNLPUXDUo0R0jteBnvSmU5wDQZBV8uNrXMq7rXoAJ77jFoEvt7ZACQYjcw4jes2aHJTg2XvSrThDgfQGTRh2chzHbB3Ez7SUVJZCMrTR1PRRsOyRMiJN1sYKZAvTWy5c2RSetJig2TUm3JtSRLYCSdbTJ'
VERIFICATION_TOKEN = 'weatherbot'

@app.route('/', methods = ['GET'])
def handle_verification():
	print "Handling Verification"
	if request.args.get('hub.verify_token', '') == VERIFICATION_TOKEN:
		print "Webhook verified!"
		return request.args.get('hub.challenge', '')
	else:
		return "Wrong verification token!"

@app.route('/', methods=['POST'])
def handle_messages():
	data = json.loads(request.data.decode())
	text = data['entry'][0]['messaging'][0]['message']['text']
	user_id = data['entry'][0]['messaging'][0]['sender']['id']
	'''json data tp be returned through post request'''
    #payload = {'recipient': {'id': user_id}, 'message': {'text': }}

def process_incoming(user_id, message):
	API_KEY = "7bb3ab5eda2ab147d9b12bdf955092d4"
	url = "http://api.openweathermap.org/data/2.5/weather?q={0}&appid={1}&units=metric"
	message_text = message['data']
	hello = ['hii','hi','hey','hiii','hello','helloo','hui']
	if message_text in hello:
		return "Hello"
	elif message_text.lower() == "weather":
		return "Enter your location(city name)"
	else: #',' in message_text:
		return process_weather(place,API_KEY,url)
	#else:
	#	return "Sorry I didn't get that"

def process_weather(place,KEY,url):
	url = url.format(place,KEY)
	r = requests.get(url)
	description = r.json()['weather'][0]['description'].title()
	icon = r.json()['weather'][0]['icon']
	weather = r.json()['main']
	text_res =  '{}\n'\
				'Temperature: {}\n'\
				'Pressure: {}\n'\
				'Humidity: {}\n'\
				'Max: {}\n' \
				'Min: {}'.format(description, weather['temp'],
					weather['pressure'],weather['humidity'],weather['temp_max'],
					weather['temp_min'])
	return text_res
	


def send_message(PAT, user_id, text):
	pass
	
	'''Send the message text to recipient. '''

if __name__ == '__main__':
	app.run(debug=True)