def main():

    file = "example.txt"
    text = "```text Hello, world! 
                Welcome to file I/O in Python.
                ```"

    with open(file, "w") as f:
        f.write(text)
        
    with open(file, "r") as f:
        f.readline()
        
        #!/usr/bin/python3
with open("words.txt", "w") as file:
    file.write("This is a new file and have 9 words")

def count_words(filename):
    with open(filename, "r") as file:
        content = file.read()
        words =  content.split()
        return len(words)
word_count = count_words("words.txt")
print(f"The file 'words.txt' contains {word_count} words.")

#!/usr/bin/python3

class Vehiculo():
    """Clase para crear un Vehiculo"""
    def init(self, matricula, marca, modelo, año):
        self.matricula = matricula
        self.marca = marca
        self.modelo = modelo
        self.año = año

    def to_dict(self):
        dict = {
                "matricula": self.matricula,
                "marca": self.marca,
                "modelo": self.modelo,
                "año": self.año
        }

        return dict

    @staticmethod
    def from_dict(data):
        #instance de un Vehiculo y le paso la data, key por key
        vehiculo = Vehiculo(data['matricula'], data['marca'], data['modelo'], data['año'])
        return vehiculo
#!/usr/bin/python3
import json
from ejercicio_1 import Vehiculo

class Taller():
    """Clase para gestionar una lista de Vehiculos"""
    def init(self):
        self.list = [] #[{"marca": "owen", "modelo"= "quemado"}, {"marca": "lol", ...}, {...}, {...}]

    def agregar_vehiculo(self, vehiculo):
        self.list.append(vehiculo)

    def listar_vehiculos(self):
        for v in self.list:
            vehiculos = Vehiculo.to_dict(v)
            print(vehiculos)

    def guardar_datos(self, filename):
        list_v = []
        for vehiculo in self.list:
            list_v.append(vehiculo.to_dict())

        with open(filename, "w") as file:
            json.dump(list_v, file)


    def cargar_datos(self, filename):
        try:
            with open(filename, "r") as file:
                data = json.load(file)
                for vehiculo in data:
                    Vehiculo.from_dict(vehiculo)
        except ValueError as e:
            return "Error guei", str(e)
from ejercicio_1 import Vehiculo
from ejercicio_3 import Taller

vehicle1 = Vehiculo("ABC123", "Juli", "Pepe", 2000)
vehicle2 = Vehiculo("ABX123", "Juli", "Pepe", 2001)

taller = Taller()

filename = "vehicles.json"
#taller.cargar_datos(filename)

taller.agregar_vehiculo(vehicle1)

taller.agregar_vehiculo(vehicle2)

taller.listar_vehiculos()

#taller.guardar_datos(filename)

# Paso 1: Solicitar al usuario el nombre del archivo y la palabra a buscar
filename = input("Enter the filename: ")
word_to_search = input("Enter the word to search for: ").lower()  # Convertir la palabra a minúsculas

# Paso 2: Leer el archivo y contar las ocurrencias de la palabra
try:
    with open(filename, 'r') as file:
        content = file.read()  # Leer todo el contenido del archivo
        
        # Contar las ocurrencias de la palabra, usando lower() para hacerlo insensible a mayúsculas/minúsculas
        word_count = content.lower().count(word_to_search)
        
    # Mostrar el resultado
    print(f"The word '{word_to_search}' appears {word_count} times in the file '{filename}'.")
except FileNotFoundError:
    print(f"The file '{filename}' was not found.")
    
import csv
#!/usr/bin/python3
with open("source.txt", "w") as file:
    file.write("Hola mi nombre\n")
    file.write("y esta linea tambien\n")

with open("source.txt", "r") as file:
    content = file.read()

with open("destination.txt", "w") as file:
    file.write(content)
    
#!/usr/bin/python3
import csv

Step 1: Create a CSV file and write data to it
header = ['Name', 'Age', 'City']
data = [{
    'Name': 'Alice',
    'Age': 30,
    'City': 'New York'
    },
    {
    'Name': 'Miram',
    'Age': 30,
    'City': 'Chicago'
    },
    {
    'Name': 'Jorge',
    'Age': 25,
    'City': 'Cansas'
    }]

Writing data to the CSV file
with open('data.csv', mode='w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames = header)
    writer.writeheader()  # Write the header row
    writer.writerows(data)  # Write the data rows

Step 2: Read the CSV file and print its contents in a formatted table
with open('data.csv', mode='r') as file:
    reader = csv.reader(file)
    next(reader)  # Skip the header row
    for row in reader:
        print(row)
import pickle

# Paso 1: Crear una clase personalizada
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __repr__(self):
        return f"Person(name={self.name}, age={self.age})"

# Instanciar un objeto de la clase Person
person1 = Person("Alice", 30)

# Paso 2: Serializar el objeto usando pickle y guardarlo en un archivo
with open('person.pkl', 'wb') as file:
    pickle.dump(person1, file)  # Serializa el objeto y lo guarda en el archivo

print("El objeto ha sido serializado y guardado en 'person.pkl'.")

# Paso 3: Deserializar el objeto desde el archivo y verificar sus propiedades
with open('person.pkl', 'rb') as file:
    loaded_person = pickle.load(file)  # Deserializa el objeto desde el archivo

# Verificar las propiedades del objeto deserializado
print("\nEl objeto deserializado es:")
print(loaded_person)

# Verificar que las propiedades son correctas
print("\nVerificando propiedades:")
print(f"Nombre: {loaded_person.name}")
print(f"Edad: {loaded_person.age}")


En este ejercicio, te mostraré cómo manejar errores al intentar deserializar datos corruptos o mal formateados, como un JSON malformado. Utilizaremos el módulo json para manejar la serialización y deserialización, y se añadirá un bloque try-except para capturar excepciones.

Código:
python
Copiar código
import json

# Paso 1: Crear un JSON malformado (por ejemplo, una comilla faltante)
corrupted_json = '{"name": "Alice", "age": 30, "city": "New York"'

# Intentar deserializar los datos corruptos
try:
    data = json.loads(corrupted_json)  # Intentar deserializar el JSON
except json.JSONDecodeError as e:
    print(f"Error al deserializar el JSON: {e}")
else:
    print("El JSON ha sido deserializado correctamente:")
    print(data)

# Paso 2: Crear un JSON bien formateado para comparar
valid_json = '{"name": "Alice", "age": 30, "city": "New York"}'

try:
    data_valid = json.loads(valid_json)  # Intentar deserializar el JSON válido
    print("\nJSON válido deserializado correctamente:")
    print(data_valid)
except json.JSONDecodeError as e:
    print(f"Error al deserializar el JSON válido: {e}")
    
