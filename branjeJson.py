import json

with open('/Users/tilen/Desktop/TP/VAJE/VAJE-3/DATA/person.json', 'r') as f:
    deserialized_person = json.load(f)

deserialized_person['age'] = 22
deserialized_person['married'] = False

with open('/Users/tilen/Desktop/TP/VAJE/VAJE-3/DATA/person.json', 'w') as f:
    json.dump(deserialized_person, f, indent=4)