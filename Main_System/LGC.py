import pandas as pd
import random
import xml.etree.ElementTree as gfg
import requests

tree = gfg.ElementTree()
df = pd.read_csv("people.csv")
root = gfg.Element(tree.getroot()) 
#FirstName,LastName,Email,DateOfBirth,Phone,Address,Country

for index, row in df.iterrows():
    firstName = row["FirstName"]
    lastName = row["LastName"]
    email = row["Email"]
    dateOfBirth = row["DateOfBirth"]
    phone = row["Phone"]
    address = row["Address"]
    country = row["Country"]
    
    lastFour = random.randint(1000,9999)
    
    cpr = dateOfBirth[:2] + dateOfBirth[3:5] + dateOfBirth [6:] + str(lastFour)

    m1 = gfg.Element("person") 
    root.append (m1) 

    gfg.SubElement(m1, "FirstName").text = firstName
    gfg.SubElement(m1, "LastName").text = lastName
    gfg.SubElement(m1, "CprNumber").text = cpr
    gfg.SubElement(m1, "Email").text = email
    
    
tree = gfg.ElementTree(root)
tree.write("filename.xml")