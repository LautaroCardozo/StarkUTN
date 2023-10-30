from funciones import *
from data_stark import lista_personajes
correr = True
while correr:
    opcion = input("Seleccione una opcion: \n"
                   "1-Mostrar nombres de los heroes en la base de datos\n"
                   "2-Mostrar altura de los heroes en la base de datos\n"
                   "3-Superheroe mas alto\n"
                   "4-Superheroe mas bajo\n"
                   "5-Promedio de altura de los superheroes\n"
                   "6-Superheroe mas pesado\n"
                   "7-Superheroe menos pesado\n"
                   "8-Salir\n")
    
    limpiar_pantalla()
    if opcion == "1":
        mostrar_datos_nombre(lista_personajes)
    elif opcion == "2":
        mostrar_datos_altura(lista_personajes)
    elif opcion == "3":
        mas_alto(lista_personajes)
    elif opcion == "4":
        mas_bajo(lista_personajes)
    elif opcion == "5":
        promedio_altura(lista_personajes)
    elif opcion == "6":
        mas_pesado(lista_personajes)
    elif opcion == "7":
        mas_liviano(lista_personajes)
    elif opcion == "8":
        print("Saliendo del programa...")
        correr = False
    else:
        print("Opcion invalida")
    
        
    if opcion != "8":
        volver_al_menu = input("Desea volver al menu? Y/N\n").upper()
        correr = False if volver_al_menu == "N" else True 
        limpiar_pantalla()