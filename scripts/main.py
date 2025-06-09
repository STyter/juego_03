import pygame
from scripts import *

def main():
    # Inicializar pygame
    pygame.init()
    # Creación de la ventana y reloj
    ventana = pygame.display.set_mode((ventana_ancho, ventana_altura))
    reloj = pygame.time.Clock()
    baldosa_puertas, baldosa_suelo = imagen() #, iimagen_fondo# baldosa_muro

    # Crear al personaje y grupo de sprites
    personaje = Personaje(20,0)
    mascota = Mascota(0,30)
    grupo = pygame.sprite.Group(personaje)
    grupo2 = pygame.sprite.Group(mascota)

    habitacion1=construir_mapa(Mapa1, baldosa_puertas, baldosa_suelo)
    habitacion2=construir_mapa(Mapa2, baldosa_puertas, baldosa_suelo)
    habitacion= habitacion1
    # Estado del juego
    estado = True
    balas=[]
    while estado:
        dt = reloj.tick(fps) / 1000  # Delta #Calcula el tiempo transcurrido entre frames (dt) para controlar animaciones suavemente

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                estado = False
            disparar(event,personaje, balas)

        keys = pygame.key.get_pressed()  # Capturar estado actual del teclado

        personaje.update(dt, keys)       # Actualizar personaje con dt y teclas
        mascota.update(dt,keys)                # Actualizar mascota con dt# se actualizan sefun el tiempo y las teclas
        ventana.fill(RGB) #rellena la pantalla

        puertas, suelo = habitacion

        for puerta in puertas:  # puertas
            if personaje.rect.colliderect(puerta[1]):
                if habitacion==habitacion1:
                    habitacion=habitacion2
                elif habitacion==habitacion2:
                    habitacion=habitacion1
                personaje.rect.x=0
                personaje.rect.y=0
                mascota.rect.x=0
                mascota.rect.y = 0
            break

        for baldosa , rect in suelo:
            ventana.blit(baldosa,rect)
        for baldosa , rect in puertas:
            ventana.blit(baldosa,rect)

        grupo.draw(ventana)
        grupo2.draw(ventana)
        
        for bala in balas[:]: #toda la lista, una copia de toda la lista, de principio a fin
            bala.mover()
            if bala.fuera_pantalla(ventana_ancho, ventana_altura):
                bala.estado =False
                balas.remove(bala)
            else:
                bala.draw(ventana)

        pygame.display.flip()  #muestra en pantalla todo lo dibujado
        if keys[pygame.K_z]:
            personaje.iniciar_ataque()
    pygame.quit() 




#            elif bala.rect.colliderect(villano.rect):
#                bala.estado = False
#                villano.health -= 5