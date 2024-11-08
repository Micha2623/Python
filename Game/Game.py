import pygame
from character import cubo

ancho = 1000
alto = 750

ventana = pygame.display.set_mode([ancho,alto])


jugando = True
cubo = cubo(900,630)
while jugando:
    eventos = pygame.event.get()
    
    for evento in eventos:
        if evento.type == pygame.QUIT:
            jugando = False
            
    cubo.draw(ventana)
    pygame.display.update()
        
quit()