from Persona import Persona
from Lista_persona import Lista_persona

persona1 = Persona(1,"Luis",34)
persona2 = Persona(2,"Juan",14)
persona3 = Persona(3,"Pedro",44)
persona4 = Persona(4,"fe",50)
persona5 = Persona(5,"jeimy",2)
persona6 = Persona(6,"sandra",10)

Lista = Lista_persona()

Lista.insetar(persona1)
Lista.insetar(persona2)
Lista.insetar(persona3)
Lista.insetar(persona4)
Lista.insetar(persona5)
Lista.insetar(persona6)

print("")
print("Listado de edades de menor a mayor")
Lista.listar_Persona()