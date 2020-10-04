from flask import Flask, request
import random
import sqlite3
app = Flask(__name__)

@app.route('/nemid-auth')
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
    return random.randint(), 201
  else:
    return "no match", 403
  