#funciones
import pygame
import random


def mover_derecha(pantalla, diccionario):
    nueva_x = diccionario["rectangulo"].x + diccionario["velocidad"]
    if nueva_x > 0 and nueva_x <= pantalla.get_width()-diccionario["rectangulo"].width:
        diccionario["rectangulo"].x = nueva_x
        # diccionario["boca"].x += diccionario["velocidad"]

def mover_izquierda(pantalla, diccionario):
    nueva_x = diccionario["rectangulo"].x - diccionario["velocidad"]
    if nueva_x > 0 and nueva_x <= pantalla.get_width()-diccionario["rectangulo"].width:
        diccionario["rectangulo"].x = nueva_x
        # diccionario["boca"].x -= diccionario["velocidad"]

#------------------------------------------------------------------------------------

def crear_charcos(pantalla: pygame.Surface, lista, cantidad, imagen, distancia_entre_charcos):
    for i in range(cantidad):
        diccionario = {}
        diccionario["superficie"] = imagen
        diccionario["rectangulo"] = imagen.get_rect()
        diccionario["velocidad"] = -random.randrange(5, 10, 1)
        diccionario["tamaño"] = diccionario["rectangulo"].width
        diccionario["rectangulo"].x = i * (distancia_entre_charcos + diccionario["tamaño"])
        # Genera una posición Y aleatoria cerca de la parte inferior de la pantalla
        diccionario["rectangulo"].y = random.randrange(pantalla.get_height() - diccionario["tamaño"] - 50, pantalla.get_height() - 10)
        lista.append(diccionario)


