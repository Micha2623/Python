import pygame


class bala:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.ancho = 15
        self.alto = 15
        self.velocidad = 10
        self.color = "blue"
        self.rect = pygame.Rect(self.x, self.y, self.ancho, self.alto)
        self.image = pygame.image.load(
            "C:/Users/micha/Desktop/Programation/Python/Game/bullet.png"
        )
        self.image = pygame.transform.scale(self.image, (20, 20))

    def draw(self, ventana):
        # pygame.draw.rect(ventana, self.color, self.rect)
        self.rect = pygame.Rect(self.x, self.y, self.ancho, self.alto)
        ventana.blit(self.image, (self.x, self.y))

    def movement(self):
        self.y -= self.velocidad
