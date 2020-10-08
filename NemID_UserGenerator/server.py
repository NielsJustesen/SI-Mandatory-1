from flask import Flask, request
import random
app = Flask(__name__)

@app.route('/generate-nemId', methods = ['POST'])
#Get the data as a JSON object
#Get the last 4 digits from the cpr of the JSON object
#Generate the first five as a random number
#return the nemId as a combination of the randomly generated number and the last four of the cpr
def generate():
	data = request.get_json()
	last_four = data["cpr"][-4:]
	first_five = random.randint(10000,99999)
	return {"nemId":str(first_five) + last_four}, 201

