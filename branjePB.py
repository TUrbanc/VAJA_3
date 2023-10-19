import person_pb2

person = person_pb2.Person()

with open(r"\Users\tilen\Desktop\TP\VAJE\VAJE-3\DATA\person.pb", "rb") as f:
    person.ParseFromString(f.read())

person.age = 31
person.married = False

with open(r"\Users\tilen\Desktop\TP\VAJE\VAJE-3\DATA\personBranjeUpdated.pb", "wb") as f:
    f.write(person.SerializeToString())

print(person)