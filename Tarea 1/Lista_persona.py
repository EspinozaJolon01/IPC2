from nodo import nodo

class Lista_persona:

    def __init__(self) :
        self.primero = None
        

    def insetar(self,persona):
        new_nodo = nodo(persona=persona)
        if self.primero is None:
            self.primero = new_nodo
            return
        
        if persona.edad < self.primero.persona.edad:
            new_nodo.siguiente = self.primero
            self.primero.anterior = new_nodo
            self.primero = new_nodo
            return
        actual = self.primero
        while actual.siguiente and actual.siguiente.persona.edad < persona.edad:
            actual = actual.siguiente

        new_nodo.siguiente = actual.siguiente
        
        if actual.siguiente:
            actual.siguiente.anterior = new_nodo
        actual.siguiente = new_nodo
        new_nodo.anterior = actual
    
    def listar_Persona(self):

        if self.primero is None:
            print("la lista se enceuntra vacia")
            return
        
        actual = self.primero
        print("nombre: ", actual.persona.nombre,
            "Edad: ", actual.persona.edad)
        
        while actual.siguiente:
            actual = actual.siguiente
            print("nombre: ", actual.persona.nombre,
            "Edad: ", actual.persona.edad)

