import pygame


class cubo:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.ancho = 50
        self.alto = 50
        self.velocidad = 10
        self.color = "red"
        self.rect = pygame.Rect(self.x, self.y, self.ancho, self.alto)
        self.image = pygame.image.load(
            "C:/Users/micha/Desktop/Programation/Python/Game/ship.png"
        )
        self.image = pygame.transform.scale(self.image, (70, 70))
        # self.image = pygame.transform.rotate(self.image, 90)
        # self.image.set_colorkey((255, 255, 255))  # Elimina el fondo blanco

    def draw(self, ventana):
        self.rect = pygame.Rect(self.x, self.y, self.ancho, self.alto)
        # pygame.draw.rect(ventana, self.color, self.rect)
        ventana.blit(self.image, (self.x, self.y))
