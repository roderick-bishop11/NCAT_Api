from flask import jsonify

data = [
        {"name": "Barber-Scotia College", "City": "Concord"},
        {"name": "Bennett College", "City": "Greensboro"},
        {"name": "Elizabeth City State University", "City": "Elizabeth City"},
        {"name": "Fayetteville State", "City": "Fayetteville"},
        {"name": "Johnson C. Smith University", "City": "Charlotte"},
        {"name": "Livingstone College", "City": "Salisbury"},
        {"name": "North Carolina Central State University", "City": "Durham"},
        {"name": "St. Augustine University", "City": "Raleigh"},
        {"name": "Shaw University", "City": "Raleigh"},
        {"name": "Winston-Salem State University", "City": "Winston-Salem"}
    ]

#get
def findOne(name):
    selected = None
    for i in range(len(data)):
        if data[i].get('name') == name:
            selected = data[i]
            break
    if selected is None:
            return f"No college found with the name {name}"
    else:
        return selected

#get
def findAll():
    return data

#post
def addOne(newCollege):
    data.append(newCollege)
    return findAll()

#delete
def deleteOne(valueToDelete):
    data.remove(valueToDelete)
    return findAll()

#patch
def patchOne(someCollege):
    college = findOne(someCollege['name'])
    data.remove(college)
    data.append(someCollege)
    return findAll()
