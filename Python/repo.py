datasource = [
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


# get
def findOne(name):
    selected = None
    for i in range(len(datasource)):
        if datasource[i].get('name') == name:
            selected = datasource[i]
            break
    if selected is None:
        return f"No college found with the name {name}"
    else:
        return selected


# get
def findAll():
    return datasource


# post
def addOne(newCollege):
    datasource.append(newCollege)
    return findAll()


# delete
def deleteOne(valueToDelete):
    datasource.remove(valueToDelete)
    return findAll()


# put
def putOne(someCollege):
    college = findOne(someCollege['name'])
    datasource.remove(college)
    datasource.append(someCollege)
    return findAll()
