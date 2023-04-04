import json


class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad


persona = Persona("Juan", 30)

with open("persona.json", "w") as archivo:
    json.dump(persona.__dict__, archivo)
