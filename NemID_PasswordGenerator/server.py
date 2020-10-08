from flask import Flask, request
app = Flask(__name__)

@app.route('/generate-password-nemID', methods = ['POST'])
#Get the data as a JSON object
#Get the first 2 digits from the nemID of the object
#Get the last 2 digits from the cpr number of the object
#lastly return the nemIdPassword as first_two and last_two
def generate():
	data = request.get_json()
	first_two = data["nemId"][:2]
	last_two = data["cpr"][-2:]
	return {"nemIdPassword": str(first_two) + str(last_two)}, 200

