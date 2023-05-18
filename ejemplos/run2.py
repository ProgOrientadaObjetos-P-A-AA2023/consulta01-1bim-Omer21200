from mis_clases import Perro
# Crear dos objetos de la clase 02

# objeto 01
# crear
perro1 = Perro("Firulais",1)
# Presentar objeto; usar el método __st__
print(perro1)
# objeto 02
perro2 = Perro()
# crear ingresando valores por teclado
print("Ingrese el nombre:")
nom=input()
print("Ingrese la edad: ")
ed=input()
perro2.nombreP=nom
perro2.edadP=ed

# Presentar objeto; usar el método __st__
print(perro2)
