import os 

def mostrar_datos_nombre(lista_personajes:dict)->None:
    for personaje in lista_personajes:
        print(f"Nombre: {personaje['nombre']}")
    


def mostrar_datos_altura(lista_personajes):
    """Muestra la altura de los characters

    Args:
        lista_personajes (dict): imprime la altura de los personajes del dict
    """
    for personaje in lista_personajes:
        print(f"Nombre: {personaje['nombre']} || Altura: {personaje['altura']}")
        

def mas_alto(lista_personajes):
    altura_max = None
    heroe_mas_alto = ""
    for personaje in lista_personajes:
        if altura_max == None or float(altura_max) < float(personaje['altura']):
            heroe_mas_alto = personaje['nombre']
            altura_max = personaje['altura']
    print (f"El heroe mas alto es {heroe_mas_alto} con una altura de {altura_max} metros/centimetros")
    

def mas_bajo(lista_personajes):
    altura_min = None
    heroe_mas_bajo = ""
    for personaje in lista_personajes:
        if altura_min == None or float(altura_min) > float(personaje['altura']):
            heroe_mas_bajo = personaje['nombre']
            altura_min = personaje['altura']
    print (f"El heroe mas bajo es {heroe_mas_bajo} con una altura de {altura_min} metros/centimetros")

def promedio_altura(lista_personajes):
    sumador_alturas = 0
    for personaje in lista_personajes:
        sumador_alturas += float(personaje['altura']) 
    print(f"El promedio de alturas es {sumador_alturas / len(lista_personajes)}")


def mas_pesado(lista_personajes):
    peso_max = None
    heroe_mas_pesado = ""
    for personaje in lista_personajes:
        if peso_max == None or float(peso_max) < float(personaje['peso']):
            heroe_mas_pesado = personaje['nombre']
            peso_max = personaje['peso']
    print (f"El heroe mas pesado es {heroe_mas_pesado} con un peso de {peso_max} kilogramos")
    

def mas_liviano(lista_personajes):
    peso_min = None
    heroe_mas_liviano = ""
    for personaje in lista_personajes:
        if peso_min == None or float(peso_min) > float(personaje['peso']):
            heroe_mas_liviano = personaje['nombre']
            peso_min = personaje['peso']
    print (f"El heroe mas liviano es {heroe_mas_liviano} con un peso de {peso_min} kilogramos")

def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')