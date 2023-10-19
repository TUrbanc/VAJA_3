import person_pb2

person = person_pb2.Person()
person.name = "Tilen"
person.age = 30
person.street = "Bognarjeva"
person.city = "Ljubljana"
person.married = True


with open(r"\Users\tilen\Desktop\TP\VAJE\VAJE-3\DATA\person.pb", "wb") as f:
    f.write(person.SerializeToString())