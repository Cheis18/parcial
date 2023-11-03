import pygame
import random
from base_funciones import *
from pygame_menu import*
import pygame_menu


def main_menu():
    pygame.quit()
    pygame.init()
    surface = pygame.display.set_mode((800, 600))
    menu = Menu("Menú Principal", 800, 600, theme=pygame_menu.themes.THEME_DARK)

    menu.add.button('Jugar', start_game)
    menu.add.button('Salir', pygame_menu.events.EXIT)

    menu.mainloop(surface)

def start_game():
    seguir = True
    resolucion_de_pantalla = {"alto": 600, "ancho": 800}

    pygame.init()
    clock = pygame.time.Clock()

    pantalla = pygame.display.set_mode((resolucion_de_pantalla["ancho"], resolucion_de_pantalla["alto"]))
    pygame.display.set_caption("Prueba")
    fuente = pygame.font.SysFont("Arial", 50)

    imagen = pygame.image.load(r"src\Recursos\navee.jpg")
    imagen = pygame.transform.scale(imagen, (resolucion_de_pantalla["ancho"], resolucion_de_pantalla["alto"]))
    fondo = 0

    arturito = pygame.image.load(r"src\Recursos\arturito.webp")
    arturito = pygame.transform.scale(arturito, (resolucion_de_pantalla["ancho"] / 7, resolucion_de_pantalla["alto"] / 4))
    arturito_rect = arturito.get_rect()
    arturito_rect.bottom = resolucion_de_pantalla["alto"]
    arturito_velocidad = 6
    diccionario_arturito = {"superficie": arturito, "rectangulo": arturito_rect, "velocidad": arturito_velocidad, "score": 0, "orientacion": "derecha"}
    flip_derecha = True
    flip_izquierda = False

    # Variables de salto
    salta = False
    contar_salta = 15

    # Crear obstáculo (charco de agua)
    charco = pygame.image.load(r"src\Recursos\charco.jpg")
    charco = pygame.transform.scale(charco, (resolucion_de_pantalla["ancho"] / 7, resolucion_de_pantalla["alto"] / 4))
    charco_rect = charco.get_rect()
    charco_rect.bottom = resolucion_de_pantalla["ancho"]
    charco_velocidad = 5
    diccionario_charco = {"superficie":charco,"rectangulo":charco_rect,"velocidad":charco_velocidad,"puntaje":0}


    lista_charco = []
    cantidad_charco = 50
    distancia_entre_charcos = 400
    crear_charcos(pantalla, lista_charco, cantidad_charco, charco,distancia_entre_charcos)

    while seguir:
        clock.tick(60)
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                seguir = False

        tecla = pygame.key.get_pressed()

        if tecla[pygame.K_LEFT]:
            mover_izquierda(pantalla, diccionario_arturito)
            if flip_izquierda == False:
                flip_izquierda = True
                flip_derecha = False
                diccionario_arturito["superficie"] = pygame.transform.flip(diccionario_arturito["superficie"], True, False)

        if tecla[pygame.K_RIGHT]:
            mover_derecha(pantalla, diccionario_arturito)
            if flip_derecha == False:
                flip_derecha = True
                flip_izquierda = False
                diccionario_arturito["superficie"] = pygame.transform.flip(diccionario_arturito["superficie"], True, False)

        # Salto de Arturito
        if not salta:
            if tecla[pygame.K_SPACE]:
                salta = True
        else:
            if contar_salta >= -15:
                neg = 1
                if contar_salta < 0:
                    neg = -1
                arturito_rect.y -= (contar_salta ** 2) * 0.25 * neg
                contar_salta -= 1
            else:
                salta = False
                contar_salta = 15   

        # Movimiento del fondo hacia la izquierda
        fondo -= 5
        if fondo <= -resolucion_de_pantalla["ancho"]:
            fondo = 0
        
        texto = fuente.render(f"Puntaje: {diccionario_charco['puntaje']}", True, "black")
        pantalla.blit(imagen, (fondo + resolucion_de_pantalla["ancho"], 0))
        pantalla.blit(imagen, (fondo, 0))
        pantalla.blit(diccionario_arturito["superficie"], diccionario_arturito["rectangulo"])

        # pantalla.blit(charco, charco_rect)
        for charco in lista_charco:
            pantalla.blit(charco["superficie"], charco["rectangulo"])
            charco["rectangulo"].x += charco["velocidad"] 

        for charco in lista_charco:
            if diccionario_charco["rectangulo"].colliderect(charco["rectangulo"]):
                lista_charco.remove(charco)
                diccionario_charco["puntaje"] += 10


        pygame.display.flip()

    pygame.quit()

def show_game_over():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    font = pygame.font.Font(None, 72)
    text = font.render("Game Over", True, (255, 0, 0))
    text_rect = text.get_rect(center=(400, 300))

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((0, 0, 0))
        screen.blit(text, text_rect)
        pygame.display.flip()

if __name__ == '__main__':
    main_menu()

