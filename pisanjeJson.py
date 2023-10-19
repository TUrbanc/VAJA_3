import json

person = {
    "name" : "Tilen",
    "age" : 21,
    "address": {
        "steet" : "Bognarjeva",
        "city" : "Ljubljana"
    },
    "married": False
}

with open('/Users/tilen/Desktop/TP/VAJE/VAJE-3/DATA/person.json','w') as f:
    json.dump(person, f, indent = 4, sort_keys=False)