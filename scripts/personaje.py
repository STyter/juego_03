import pygame
from scripts.configuracion import frame_width,frame_height,ventana_altura,ventana_ancho

class Personaje(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.timer = 0
        self.animation_speed = 0.1
        self.current_frame = 0
        self.speed=2
        # Luego llamas a una función que recorte la spritesheet y devuelva la lista de frames
        self.frames_stay = self.animation('recursos/imagenes/stay.png', frame_height, frame_width, columna=3, fila=3, max_frames=9)
        self.frames_run = self.animation('recursos/imagenes/run.png', frame_height, frame_width, columna=3, fila=3, max_frames=8)
        self.frames_attack = self.animation('recursos/imagenes/pegar.png', frame_height, frame_width, columna=3, fila=3, max_frames=8)
        self.frames = self.frames_stay
        self.image = self.frames[self.current_frame]
        self.rect = self.image.get_rect(topleft=(x, y))
        self.is_attacking = False
        self.facing_right = True 
        #para que vea a donde disparara
        self.direccion_bala="derecha"
        #tiempo de disparo entre disparo
        self.cooldown_disparo=300 #milisegundos
        self.t_ultimo_disparo= pygame.time.get_ticks()

    def animation(self,ruta,ancho,alto,columna,fila,max_frames=None):
        spritesheet = pygame.image.load(ruta).convert_alpha()
        frames = []
        total_frames = columna * fila if max_frames is None else max_frames

        for fila in range(fila):
            for columna in range(columna):
                if len(frames) >= total_frames:
                    return frames
                frame = spritesheet.subsurface((columna * ancho, fila * alto, ancho, alto))
                frames.append(frame)
        return frames
    
    def iniciar_ataque(self):
        if not self.is_attacking: #si no esta atacando
            self.is_attacking = True
            self.frames = self.frames_attack
            self.current_frame = 0
            self.timer = 0
            self.actualizar_imagen(self.frames[self.current_frame])

    def actualizar_imagen(self, frame):
        if self.facing_right:
            self.image = frame  #duda
        else:
            self.image = pygame.transform.flip(frame, True, False)  #duda
    
    

    def update(self, dt, keys):
        dx = dy = 0

        if keys[pygame.K_RIGHT]:
            dx = self.speed
            self.direccion_bala="derecha"
            self.facing_right = True
        elif keys[pygame.K_LEFT]:
            dx = -self.speed
            self.facing_right = False
            self.direccion_bala="izquierda"

        if keys[pygame.K_DOWN]:
            dy = self.speed
            self.direccion_bala="abajo"
        elif keys[pygame.K_UP]:
            dy = -self.speed
            self.direccion_bala="arriba"



        # Si está atacando, reproducir solo la animación de ataque
        if self.is_attacking:
            self.timer += dt
            if self.timer >= self.animation_speed:
                self.timer = 0
                self.current_frame += 1
                if self.current_frame >= len(self.frames_attack):
                    self.current_frame = 0
                    self.is_attacking = False 
                    self.frames = self.frames_stay 
                self.actualizar_imagen(self.frames_attack[self.current_frame])
            return  




        en_movimiento = dx != 0 or dy != 0   # si esto es verdadero


        # Cambiar animación
        if en_movimiento:
            if self.frames != self.frames_run:
                self.frames = self.frames_run
                self.current_frame = 0
                self.timer = 0
        else:
            if self.frames != self.frames_stay:
                self.frames = self.frames_stay
                self.current_frame = 0
                self.timer = 0

        # Actualizar frame de animación
        self.timer += dt
        if self.timer >= self.animation_speed:
            self.timer = 0
            self.current_frame = (self.current_frame + 1) % len(self.frames)
            self.actualizar_imagen(self.frames[self.current_frame])


        # Movimiento
        self.rect.x += dx
        self.rect.y += dy

        # Límite de pantalla (opcional)
        self.rect.clamp_ip(pygame.Rect(10,0,ventana_ancho, ventana_altura))
