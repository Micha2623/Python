import pygame


class Enemy:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.ancho = 50
        self.alto = 50
        self.velocidad = 5
        self.color = "purple"
        self.rect = pygame.Rect(self.x, self.y, self.ancho, self.alto)
        self.vida = 3
        self.image = pygame.image.load(
            "C:/Users/micha/Desktop/Programation/Python/Game/shipp.png"
        )
        self.image = pygame.transform.scale(self.image, (70, 70))
        self.image = pygame.transform.rotate(self.image, 90)
        self.image = pygame.transform.rotate(self.image, 90)

    def draw(self, ventana):
        # Actualizar la posición del rectángulo
        self.rect = pygame.Rect(self.x, self.y, self.ancho, self.alto)
        # Dibujar la imagen en la posición correcta
        ventana.blit(self.image, (self.x, self.y))

    def movement(self):
        # Actualizar la posición vertical del enemigo
        self.y += self.velocidad
