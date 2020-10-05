from flask import Flask, request
app = Flask(__name__)

@app.route('/generate-password-nemID', methods = ['POST'])
def generate():
	data = request.get_json()
	first_two = data["nemId"][:2]
	last_two = data["cpr"][-2:]
	return {"nemIdPassword": str(first_two) + str(last_two)}, 200

