import pandas as pd
import random
import xml.etree.ElementTree as ET


# header = ET.Element('?xml version="1.0"?')

# tree = ET.ElementTree(header)
# tree.write("filename.xml")

df = pd.read_csv("people.csv")

#FirstName,LastName,Email,DateOfBirth,Phone,Address,Country

for index, row in df.iterrows():
    firstName = row["FirstName"]
    lastname = row["LastName"]
    email = row["Email"]
    dateOfBirth = row["DateOfBirth"]
    phone = row["Phone"]
    address = row["Address"]
    country = row["Country"]
    
    lastFour = random.randint(1000,9999)
    
    cpr = dateOfBirth[:2] + dateOfBirth[3:5] + dateOfBirth [6:] + str(lastFour)
    print(cpr)
      
    person = ET.Element("Person")   
    ET.SubElement(person, "FirstName").text = firstName
    ET.SubElement(person, "LastName").text = lastname
    ET.SubElement(person, "CprNumber").text = cpr
    ET.SubElement(person, "Email").text = email
    

tree = ET.ElementTree(person)
# ET.append(person)
tree.write("filename.xml")