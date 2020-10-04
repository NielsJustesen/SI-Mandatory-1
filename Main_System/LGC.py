import pandas as pd

df = pd.read_csv("people.csv")

#FirstName,LastName,Email,DateOfBirth,Phone,Address,Country
firstNames, lastNames, emails, datesOfBirth, phoneNumbers,address,countries = "","","","","","",""




for index, row in df.iterrows():
    firstName = row["FirstName"]
    lastname = row["LastName"]
    email = row["Email"]
    dateOfBirth = row["DateOfBirth"]
    phone = row["Phone"]
    address = row["Address"]
    country = row["Country"]
    print(firstName)
    print(lastname)
    print(email)
    print(dateOfBirth)
    print(phone)
    print(address)
    print(country)