import pygame
from scripts.configuracion import ventana_ancho,ventana_altura

def imagen():
#    baldosa_muro=pygame.image.load('recursos/imagenes/baldosa_pared.png').convert_alpha()
    baldosa_puertas=pygame.image.load("recursos/imagenes/baldosa_puertas.png").convert_alpha()
    baldosa_suelo=pygame.image.load("recursos/imagenes/baldosa_sueloc.png").convert_alpha()
    return baldosa_puertas, baldosa_suelo

def construir_mapa(mapa, baldosa_puertas, baldosa_suelo): #baldosa_muro
    #limites=[]
    puertas=[]
    suelo=[]
    x=0
    y=0
    for linea in mapa:
        for baldosa in linea:
#            if baldosa=="PA":
#                limites.append([baldosa_muro,pygame.Rect(x,y,64,64)])
            if baldosa=="PU":
                puertas.append([baldosa_puertas, pygame.Rect(x,y,64,64)])
            elif baldosa=="S":
                suelo.append([baldosa_suelo, pygame.Rect(x,y,64,64)])
            x+=64
        x=0
        y+=64
    return puertas,suelo # limites 

