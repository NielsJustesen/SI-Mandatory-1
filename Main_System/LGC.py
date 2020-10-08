import pandas as pd
import random
import xml.etree.ElementTree as ET
import requests
import msgpack
import json

df = pd.read_csv("people.csv")
#FirstName,LastName,Email,DateOfBirth,Phone,Address,Country

for index, row in df.iterrows():
    #Get all the data from the CSV file
    firstName = row["FirstName"]
    lastName = row["LastName"]
    email = row["Email"]
    dateOfBirth = row["DateOfBirth"]
    phone = row["Phone"]
    address = row["Address"]
    country = row["Country"]
    
    #Generate the last four digits of the cpr
    lastFour = random.randint(1000,9999)
    
    #Generate cpr from dateOfBirth
    cpr = dateOfBirth[:2] + dateOfBirth[3:5] + dateOfBirth [6:] + str(lastFour)

    #Create the xml body for the person object
    person = ET.Element("Person")   
    ET.SubElement(person, "FirstName").text = firstName
    ET.SubElement(person, "LastName").text = lastName
    ET.SubElement(person, "cprnumber").text = cpr
    ET.SubElement(person, "email").text = email
    headers = {'Content-Type': 'application/xml'} 
    
    #Send the person as XML to the nemID generator
    resp = requests.post("http://localhost:8080/nemID", data=ET.tostring(person), headers=headers)

    #Get the nemID from the repsonse
    nemID = resp.json()['nemID']

    #Generate the person as a json object
    person_json = {
      "f_name": firstName,
      "l_name": lastName,
      "birth_date": dateOfBirth,
      "email": email,
      "country": country,
      "phone": phone,
      "address": address,
      "CPR": cpr,
      "NemID": nemID
    }
    print(json.dumps(person_json))
    #Serialize the person_json object to a .msgpack file
    serialized_json = json.dumps(person_json)
    with open(cpr + ".msgpack", "wb") as data_file:
      package = msgpack.packb(serialized_json)
      data_file.write(package)
