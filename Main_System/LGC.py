import pandas as pd
import random
import xml.etree.ElementTree as ET
import requests

# tree = gfg.ElementTree()
df = pd.read_csv("people.csv")
# root = gfg.Element(tree.getroot()) 
#FirstName,LastName,Email,DateOfBirth,Phone,Address,Country

for index, row in df.iterrows():
    firstName = row["FirstName"]
    lastName = row["LastName"]
    email = row["Email"]
    dateOfBirth = row["DateOfBirth"]
    # phone = row["Phone"]
    # address = row["Address"]
    # country = row["Country"]
    
    lastFour = random.randint(1000,9999)
    
    cpr = dateOfBirth[:2] + dateOfBirth[3:5] + dateOfBirth [6:] + str(lastFour)

    # m1 = gfg.Element("person") 
    # root.append (m1) 

    # gfg.SubElement(m1, "FirstName").text = firstName
    # gfg.SubElement(m1, "LastName").text = lastName
    # gfg.SubElement(m1, "CprNumber").text = cpr
    # gfg.SubElement(m1, "Email").text = email

    person = ET.Element("Person")   
    ET.SubElement(person, "FirstName").text = firstName
    ET.SubElement(person, "LastName").text = lastName
    ET.SubElement(person, "cprnumber").text = cpr
    ET.SubElement(person, "email").text = email
    tree = ET.ElementTree(person)
    tree.write(firstName + ".xml")  
    headers = {'Content-Type': 'application/xml'} 
    
    with open(firstName + ".xml") as xml:
      resp = requests.post("http://localhost:8080/nemID", data=xml, headers=headers)
      print(resp.json())
  
    
