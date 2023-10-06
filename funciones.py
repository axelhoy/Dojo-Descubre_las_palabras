import pygame, sys, random

def elegir_key(claves:list):
    """recibe una lista de claves y devuelve una al azar

    Args:
        palabras (list): lista de palabras

    Returns:
        _type_: False en caso de que la lista este vacia, sino retorna una key al azar
    """
    return random.choice(claves)

def crear_lista_claves(lista:list):
    """recibe la lista de las palabras y retorna una lista con las key 

    Args:
        lista (list): lista de las palabras

    Returns:
        _type_: False en caso de que la lista este vacia, sino retorna una lista con todas las key
    """
    retorno = False
    if len(lista) > 0:
        lista_claves = []
        for claves in lista:
            lista_claves.append(claves)
        retorno = lista_claves
    return retorno

def letras_disponibles(palabra):
    """recibe una serie de letras la mete en una lista y crea un set de la misma

    Args:
        palabra (_type_): letras a settear

    Returns:
        _type_: False en caso de que la palabra este vacia, sino devuelve una lista seteada de las letras de ese palabra
    """
    retorno = False
    if len(palabra) > 0:
        lista_letras = []
        for letra in palabra:
            lista_letras.append(letra.lower())
        letras_disponibles = set(lista_letras)
        retorno = letras_disponibles
    return retorno

def azar(letras:str):

    lista_letras = list(letras)

    random.shuffle(lista_letras)
    mezcla = "".join(lista_letras)

    return mezcla

def dibujar_shuffle(window):
    BLACK = 0,0,0
    WHITE = 255, 255, 255
    pygame.draw.rect(window, BLACK, (650, 10, 120, 40))  
    font = pygame.font.Font(None, 36)
    text = font.render("MEZCLA!", True, WHITE)
    text_rect = text.get_rect(center=(710, 30))
    window.blit(text, text_rect)

def dibujar_borrar(window):
    BLACK = 0,0,0
    WHITE = 255, 255, 255
    pygame.draw.rect(window, BLACK, (650, 10, 120, 40))  
    font = pygame.font.Font(None, 36)
    text = font.render("Borrar", True, WHITE)
    text_rect = text.get_rect(center=(710, 60))
    window.blit(text, text_rect)
