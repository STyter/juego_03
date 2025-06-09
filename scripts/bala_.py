import pygame
import os
from scripts.configuracion import ventana_altura,ventana_ancho

class Bala():
    def __init__(self,x,y, direccion):
        super().__init__()
        self.imagen_or = pygame.image.load('recursos/imagenes/BALA_N.png').convert_alpha()
        self.imagen=self.imagen_or
        self.rect= self.imagen.get_rect()
        self.rect.topleft=(x,y)
        self.estado = True
        self.velocidad= 5
        self.direccion= direccion
        self.actualizar_imagen_bala()
 #bala = Bala(heroe.rect.right, heroe.rect.centery)

    def mover(self): #para que la bala se mueva con la dirrecion en la que esta el heroe
        if self.direccion == "derecha":
            self.rect.x += self.velocidad
        elif self.direccion =="izquierda":
            self.rect.x -= self.velocidad
        elif self.direccion == "arriba":
            self.rect.y -= self.velocidad
        elif self.direccion == "abajo":
             self.rect.y += self.velocidad

    def draw(self, pantalla):
        pantalla.blit(self.imagen, self.rect)
    
    def actualizar_imagen_bala(self):
        if self.direccion=="derecha":
            self.imagen = self.imagen_or  #duda
        elif self.direccion=="izquierda":
            self.imagen = pygame.transform.flip(self.imagen_or, True, False)
        elif self.direccion== "abajo":
            self.imagen= pygame.transform.rotate(self.imagen_or, -90)
        elif self.direccion =="arriba":
            self.imagen= pygame.transform.rotate(self.imagen_or, 90)

        pos = self.rect.topleft  # guardamos la posición antes de cambiar el rect
        self.rect = self.imagen.get_rect()  # actualizamos el rect a la nueva imagen
        self.rect.topleft = pos # restauramos la posición original para que no "salte"

    def fuera_pantalla(self,ventana_ancho, ventana_altura): #para que la bala no salga de la pantal
        if (0<=self.rect.right<= ventana_ancho) and (0<=self.rect.bottom<= ventana_altura):
            return False
        else: 
            return True
#recorres la lista donde estan las balas y luego ves si esta fuera de los limites de la pantalla si fuera asi lo remueves


def disparar(shoot_control, personaje, balas):  #para que la bala se dispare 
        if shoot_control.type == pygame.KEYDOWN and shoot_control.key == pygame.K_e:
                ahora=pygame.time.get_ticks()
                if ahora-personaje.t_ultimo_disparo> personaje.cooldown_disparo:
                    if personaje.direccion_bala=="derecha":
                        x,y = personaje.rect.right, personaje.rect.centery
                    elif personaje.direccion_bala == "izquierda":
                        x,y= personaje.rect.left, personaje.rect.centery
                    elif personaje.direccion_bala == "arriba":
                        x,y= personaje.rect.centerx, personaje.rect.top
                    elif personaje.direccion_bala == "abajo":
                        x,y = personaje.rect.centerx, personaje.rect.bottom
                    nueva_bala= Bala(x,y,personaje.direccion_bala)
                    balas.append(nueva_bala)
                    personaje.t_ultimo_disparo=ahora




#heroe= Heroe()
#villano= Villano()

#for bala in balas[:]: #toda la lista, una copia de toda la lista, de principio a fin
#    bala.mover()
#    if bala.fuera_pantalla(width, height):
#        balas.estado =False
#    elif bala.rect.colliderect(villano.rect):
#        bala.estado = False
#        villano.health -= 5


#for shoot_control in pygame.event.get():
#    dispara(shoot_control,heroe)

#balas_activas = []  
#for bala in balas: 
#    if bala.estado == True:  
#        balas_activas.append(bala)  
#balas = balas_activas  