import pygame
from character import cubo
from enemy import Enemy
from bullets import bala
import random

pygame.init()
pygame.mixer.init()

ancho = 1000
alto = 750
fps = 60
vida = 5
points = 0
font = pygame.font.SysFont("Comic Sans", 40)
reloj = pygame.time.Clock()
bullets = []
ventana = pygame.display.set_mode([ancho, alto])
trigger = pygame.mixer.Sound(
    "C:/Users/micha/Desktop/Programation/Python/Game/laser.wav"
)
explosion = pygame.mixer.Sound(
    "C:/Users/micha/Desktop/Programation/Python/Game/death.wav"
)
death = pygame.mixer.Sound(
    "C:/Users/micha/Desktop/Programation/Python/Game/explosion.wav"
)

last_bullet = 0
bullet_bullet_time = 200


def shoot_bullets():
    global last_bullet

    if pygame.time.get_ticks() - last_bullet > bullet_bullet_time:
        bullets.append(bala(cubo.rect.centerx, cubo.rect.centery))
        last_bullet = pygame.time.get_ticks()
        trigger.play()


def gestionTeclas(teclas):
    if teclas[pygame.K_a]:
        if cubo.x >= 0:
            cubo.x -= cubo.velocidad
    if teclas[pygame.K_d]:
        if cubo.x + cubo.ancho <= ancho:
            cubo.x += cubo.velocidad
    if teclas[pygame.K_SPACE]:
        shoot_bullets()


jugando = True

cubo = cubo(ancho / 2, alto - 75)
enemys = []

pastTime = 0
enemy_enemy_time = 500
enemys.append(Enemy(ancho / 2, 100))

while jugando and vida > 0:
    pastTime += reloj.tick(fps)

    if pastTime > enemy_enemy_time:
        enemys.append(Enemy(random.randint(0, ancho), -70))
        pastTime = 0

    eventos = pygame.event.get()
    teclas = pygame.key.get_pressed()
    gestionTeclas(teclas)

    for evento in eventos:
        if evento.type == pygame.QUIT:
            jugando = False

    ventana.fill("black")
    cubo.draw(ventana)

    for enemy in enemys[:]:  # Iterando sobre una copia para modificar la lista
        enemy.draw(ventana)
        enemy.movement()

        if pygame.Rect.colliderect(cubo.rect, enemy.rect):
            vida -= 1
            explosion.play()
            enemys.remove(enemy)
            if vida == 0:
                death.play()

        if enemy.y > alto:
            points += 1
            enemys.remove(enemy)

        for bullet in bullets[:]:
            if pygame.Rect.colliderect(bullet.rect, enemy.rect):
                enemy.vida -= 1
                bullets.remove(bullet)

        if enemy.vida <= 0:
            death.play()
            enemys.remove(enemy)
            points += 10

    for bullet in bullets[:]:
        bullet.draw(ventana)
        bullet.movement()

    text_vida = font.render(f"Lives: {vida}", True, "White")
    text_points = font.render(f"Points: {points}", True, "White")

    ventana.blit(text_vida, (20, 20))
    ventana.blit(text_points, (20, 60))

    pygame.display.update()

pygame.quit()

# Pedir el nombre del jugador y guardar los puntos en el archivo
name = input("Introduce a name: ")

try:
    with open(
        r"C:\Users\micha\Desktop\Programation\Python\Game\scores.txt", "a"
    ) as archivo:
        archivo.write(f"{name} - {points}\n")
    print(f"Score saved: {name} - {points}")
except Exception as e:
    print(f"Error saving score: {e}")

quit()
