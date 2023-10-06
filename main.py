import random
from data import *
from funciones import *

import pygame

pygame.init()

WIDTH, HEIGHT = 800, 600
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Juego de Palabras")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

palabra_key = elegir_key(crear_lista_claves(lista_palabras))

font = pygame.font.Font(None, 36)
texto = ""
texto_color = BLACK
maximo = 6
letras_validadas = letras_disponibles(palabra_key)
letras = azar(palabra_key)
score = 0
time_left = 90 
clock = pygame.time.Clock()
running = True
pressed_shuffle = False
palabras_escritas = []

while running:
    time_left -= clock.tick(60) / 1000
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1: 
                mouse_pos = pygame.mouse.get_pos()
                if 650 <= mouse_pos[0] <= 770 and 10 <= mouse_pos[1] <= 50:
                    letras = azar(letras)
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                texto = texto[:-1]
            elif event.key == pygame.K_RETURN:
                print("Texto escrito: ", texto)
                if texto in lista_palabras[palabra_key]:
                    palabras_escritas.append(texto)
                    if texto in palabras_escritas:
                        score += len(texto)
                    else:
                        score = score
                texto = ""
            else:
                if len(texto) < maximo:
                    if event.unicode in letras_validadas:
                        texto += event.unicode

    window.fill(WHITE)
    dibujar_shuffle(window)
    texto_surface = font.render(f"Adivina!: {texto}", True, texto_color)
    window.blit(texto_surface, (10, 150))
    text = font.render("Letras: " + " ".join(letras), True, BLACK)
    window.blit(text, (10, 10))
    text = font.render("Puntuación: " + str(score), True, BLACK)
    window.blit(text, (10, 50))
    text = font.render("Tiempo: " + str(int(time_left)), True, BLACK)
    window.blit(text, (10, 90))

    pygame.display.flip()

pygame.quit()
