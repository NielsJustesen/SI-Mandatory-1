from flask import Flask, request
import random
import sqlite3
app = Flask(__name__)

@app.route('/nemid-auth', methods = ['POST'])
#Connect to the database
#Retrieve the data as JSON
#Get the password and nemID from the JSON object
#Retrieve the person with the same nemID from the database
#Generate a nemID code for that person
def generate():
  db = sqlite3.connect('../NemID_ESB/nem_id_database.sqlite')
  data = request.get_json()
  password = data["nemIdCode"]
  nemID = data["nemId"]

  db_cursor = db.cursor()
  get_command = """SELECT Password FROM user WHERE NemID=""" + nemID
  db_cursor.execute(get_command)
  db_pass = db_cursor.fetchone()
  if db_pass[0] == password:
    return random.randint(100000,999999), 201
  else:
    return "Forbidden", 403
  