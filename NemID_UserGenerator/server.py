from flask import Flask, request
import random
app = Flask(__name__)

@app.route('/generate-nemId', methods = ['POST'])
def generate():
	data = request.get_json()
	last_four = data["cpr"][-4:]
	first_five = random.randint(10000,99999)
	return {"nemId":str(first_five) + last_four}, 201

