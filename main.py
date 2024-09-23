import math
import random
import os
os.environ["SDL_VIDEODRIVER"] = "dummy"

import pygame
from pygame import mixer

import time
from database import insertar_voto, obtener_movimiento_ganador  # Importar funciones de la base de datos

# Initialize the pygame
pygame.init()

# Create the screen
screen = pygame.display.set_mode((800, 600))

# Background
background = pygame.image.load('background.png')

# Sound
#mixer.music.load("background.wav")
#mixer.music.play(-1)

# Caption and Icon  
pygame.display.set_caption("Space Invader")
icon = pygame.image.load('ufo.png')
pygame.display.set_icon(icon)

# Player
playerImg = pygame.image.load('player.png')
playerX = 370
playerY = 480
playerX_change = 0

# Enemy
enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemies = 6

for i in range(num_of_enemies):
    enemyImg.append(pygame.image.load('enemy.png'))
    enemyX.append(random.randint(0, 736))
    enemyY.append(random.randint(50, 150))
    enemyX_change.append(4)
    enemyY_change.append(40)

# Bullet
bulletImg = pygame.image.load('bullet.png')
bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change = 10
bullet_state = "ready"

# Score
score_value = 0
font = pygame.font.Font('freesansbold.ttf', 32)
textX = 10
testY = 10

# Game Over
over_font = pygame.font.Font('freesansbold.ttf', 64)

def show_score(x, y):
    score = font.render("Score : " + str(score_value), True, (255, 255, 255))
    screen.blit(score, (x, y))

def game_over_text():
    over_text = over_font.render("GAME OVER", True, (255, 255, 255))
    screen.blit(over_text, (200, 250))

def player(x, y):
    screen.blit(playerImg, (x, y))

def enemy(x, y, i):
    screen.blit(enemyImg[i], (x, y))

def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x + 16, y + 10))

def isCollision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt(math.pow(enemyX - bulletX, 2) + (math.pow(enemyY - bulletY, 2)))
    if distance < 27:
        return True
    else:
        return False

# Variables de nivel y dificultad
current_level = 1
max_level = 5

# Diccionario para los niveles
level_difficulty = {
    1: {'num_of_enemies': 6, 'enemy_speed': 4, 'enemy_y_change': 40},
    2: {'num_of_enemies': 8, 'enemy_speed': 5, 'enemy_y_change': 50},
    3: {'num_of_enemies': 10, 'enemy_speed': 6, 'enemy_y_change': 60},
    4: {'num_of_enemies': 12, 'enemy_speed': 7, 'enemy_y_change': 70},
    5: {'num_of_enemies': 15, 'enemy_speed': 8, 'enemy_y_change': 80}
}

# Función para generar enemigos según el nivel
def generate_enemies(level):
    enemyImg.clear()
    enemyX.clear()
    enemyY.clear()
    enemyX_change.clear()
    enemyY_change.clear()
    num_of_enemies = level_difficulty[level]['num_of_enemies']
    for i in range(num_of_enemies):
        enemyImg.append(pygame.image.load('enemy.png'))
        enemyX.append(random.randint(0, 736))
        enemyY.append(random.randint(50, 150))
        enemyX_change.append(level_difficulty[level]['enemy_speed'])
        enemyY_change.append(level_difficulty[level]['enemy_y_change'])

# Sonido de disparo y explosión
laserSound = mixer.Sound("laser.wav")
explosionSound = mixer.Sound("explosion.wav")

# Generar enemigos al iniciar el primer nivel
generate_enemies(current_level)

fire_rate = 200
last_shot_time = pygame.time.get_ticks()

# Lógica para obtener el movimiento ganador
ultimo_voto_tiempo = time.time()

# Game Loop
running = True
while running:

    # Cada minuto, obtener el movimiento ganador
    if time.time() - ultimo_voto_tiempo > 60:
        movimiento_ganador = obtener_movimiento_ganador()
        if movimiento_ganador:
            if movimiento_ganador == 'Izquierda':
                playerX_change = -5
            elif movimiento_ganador == 'Derecha':
                playerX_change = 5
            elif movimiento_ganador == 'Disparar' and bullet_state == "ready":
                laserSound.play()
                bulletX = playerX
                fire_bullet(bulletX, bulletY)
        ultimo_voto_tiempo = time.time()

    screen.fill((0, 0, 0))
    screen.blit(background, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Movimiento del jugador
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -5
            if event.key == pygame.K_RIGHT:
                playerX_change = 5
            if event.key == pygame.K_SPACE:
                current_time = pygame.time.get_ticks()
                if bullet_state == "ready" and current_time - last_shot_time > fire_rate:
                    laserSound.play()
                    bulletX = playerX
                    fire_bullet(bulletX, bulletY)
                    last_shot_time = current_time

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0

    playerX += playerX_change
    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736

    # Copiar las listas de enemigos para iterar sin problemas
    enemies_to_remove = []

    # Movimiento de los enemigos
    for i in range(len(enemyX)):
        if enemyY[i] > 440:
            for j in range(len(enemyY)):
                enemyY[j] = 2000
            game_over_text()
            running = False
            break

        enemyX[i] += enemyX_change[i]
        if enemyX[i] <= 0:
            enemyX_change[i] = level_difficulty[current_level]['enemy_speed']
            enemyY[i] += enemyY_change[i]
        elif enemyX[i] >= 736:
            enemyX_change[i] = -level_difficulty[current_level]['enemy_speed']
            enemyY[i] += enemyY_change[i]

        # Verificar colisión
        collision = isCollision(enemyX[i], enemyY[i], bulletX, bulletY)
        if collision:
            explosionSound.play()
            bulletY = 480
            bullet_state = "ready"
            score_value += 1
            enemies_to_remove.append(i)

        enemy(enemyX[i], enemyY[i], i)

    # Eliminar enemigos después de iterar
    for i in sorted(enemies_to_remove, reverse=True):
        enemyX.pop(i)
        enemyY.pop(i)
        enemyImg.pop(i)
        enemyX_change.pop(i)
        enemyY_change.pop(i)

    # Movimiento del disparo
    if bulletY <= 0:
        bulletY = 480
        bullet_state = "ready"

    if bullet_state == "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change

    # Verificación de enemigos
    if len(enemyX) == 0:
        if current_level < max_level:
            current_level += 1
            generate_enemies(current_level)
        else:
            print("¡Has completado todos los niveles!")
            running = False  # El juego termina después de todos los niveles

    player(playerX, playerY)
    show_score(textX, testY)
    pygame.display.update()
