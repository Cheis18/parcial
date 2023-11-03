import pygame
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
    # Finalizar Pygame

def start_game():
    running = True
    resolucion_de_pantalla = {"alto": 600, "ancho": 1000}
    origen = (0, 0)
    vidas = 3

    # Inicialización de Pygame
    pygame.init()
    clock = pygame.time.Clock()

    # Configuración de la pantalla
    screen = pygame.display.set_mode((resolucion_de_pantalla["ancho"], resolucion_de_pantalla["alto"]))
    pygame.display.set_caption("Juego de Arturito")

    # cargo icono en ventana
    icono = pygame.image.load(r"src\Recursos\logo.png")
    pygame.display.set_icon(icono)

    imagen = pygame.image.load(r"src\Recursos\navee.jpg")  # la r anula la secuencia de escape
    imagen = pygame.transform.scale(imagen, (resolucion_de_pantalla["ancho"], resolucion_de_pantalla["alto"]))

    # Personaje principal (Arturito)
    arturito = pygame.image.load(r"src\Recursos\arturito.webp")
    arturito = pygame.transform.scale(arturito, (resolucion_de_pantalla["ancho"] / 7, resolucion_de_pantalla["alto"] / 4))
    arturito_original = arturito
    arturito_rect = arturito.get_rect()
    arturito_speed = 6

    # Variables de salto
    jumping = False
    jump_count = 15

    # Posición inicial de Arturito
    arturito_rect.x = 0
    arturito_rect.y = resolucion_de_pantalla["alto"] - arturito_rect.height - 15

    # Variables para el movimiento del fondo
    fondo_x = 0

    # Crear obstáculo (charco de agua)
    obstaculo = pygame.Surface((75, 65))
    obstaculo.fill((0, 0, 255))
    obstaculo_rect = obstaculo.get_rect()
    obstaculo_rect.x = resolucion_de_pantalla["ancho"]
    obstaculo_rect.y = resolucion_de_pantalla["alto"] - obstaculo_rect.height - 15
    charco = pygame.image.load(r"src\Recursos\charco.jpg")
    charco = pygame.transform.scale(charco, (95, 68))

    obstaculo_speed = 5

    # Fuente para el marcador
    font = pygame.font.Font(None, 36)

    # Bucle principal del juego
    while running:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Movimiento lateral de Arturito
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            arturito = pygame.transform.flip(arturito_original, True, False)
            arturito_rect.x -= arturito_speed
        if keys[pygame.K_RIGHT]:
            arturito = arturito_original
            arturito_rect.x += arturito_speed

        # Salto de Arturito
        if not jumping:
            if keys[pygame.K_SPACE]:
                jumping = True
        else:
            if jump_count >= -15:
                neg = 1
                if jump_count < 0:
                    neg = -1
                arturito_rect.y -= (jump_count ** 2) * 0.25 * neg
                jump_count -= 1
            else:
                jumping = False
                jump_count = 15

        # Restringir el movimiento de Arturito a la pantalla
        arturito_rect.x = max(0, min(arturito_rect.x, resolucion_de_pantalla["ancho"] - arturito_rect.width))
        arturito_rect.y = max(0, min(arturito_rect.y, resolucion_de_pantalla["alto"] - arturito_rect.height))

        # Movimiento del fondo hacia la izquierda
        fondo_x -= 5
        if fondo_x <= -resolucion_de_pantalla["ancho"]:
            fondo_x = 0

        # Movimiento del obstáculo (charco de agua)
        obstaculo_rect.x -= obstaculo_speed
        if obstaculo_rect.right < 0:
            obstaculo_rect.x = resolucion_de_pantalla["ancho"]

        # Verificar colisión con el charco de agua
        if arturito_rect.colliderect(obstaculo_rect):
            vidas -= 1
            print(f"Te quedan {vidas} vidas")
            if vidas == 0:
                running = False
                show_game_over()  # Llama a la función de Game Over

            # Reposicionar el charco
            obstaculo_rect.x = resolucion_de_pantalla["ancho"]

        # Dibujar el marcador de vidas
        marcador = font.render(f"Vidas: {vidas}", True, (255, 255, 255))
        screen.blit(imagen, (fondo_x, 0))
        screen.blit(imagen, (fondo_x + resolucion_de_pantalla["ancho"], 0))
        screen.blit(arturito, arturito_rect)
        screen.blit(charco, obstaculo_rect)
        screen.blit(marcador, (10, 10))  # Posición del marcador
        pygame.display.flip()


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
