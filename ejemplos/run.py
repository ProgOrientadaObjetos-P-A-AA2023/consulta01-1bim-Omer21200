from mis_clases import Persona
# Crear dos objetos de la clase 01

# objeto 01
# crear
per1 = Persona("Omer", "Benitez",18)

# Presentar objeto; usar el método __st__
print(per1)
# objeto 02
per2 = Persona();
# crear ingresando valores por teclado
print("Ingrese el nombre:")
nom=input()
print("Ingrese el apellido:")
ape=input()
print("Ingrese la edad: ")
ed=input()
per2.nombre=nom
per2.apellido=ape
per2.edad=ed

# Presentar objeto; usar el método __st__

print(per2)
