import pygame
import math
import random

#Intialize the pygame
pygame.init()

#we are created the screen for the game 
screen = pygame.display.set_mode((800, 600))

#background
background = pygame.image.load("MainFolder/images/backg.png")

# Titile andIcon of the game 
pygame.display.set_caption("Alien Invaders")
icon = pygame.image.load("MainFolder/images/ufo.png")
pygame.display.set_icon(icon)

# Player
playerImg = pygame.image.load("MainFolder/images/spaceship.png")
playerX = 370
playerY = 480
playerX_change = 0


# Ememy
enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemies = 7

for h in range(num_of_enemies):
    enemyImg.append(pygame.image.load("MainFolder/images/alien-2.png"))
    enemyX.append(random.randint (0, 735))
    enemyY.append(random.randint (50, 150))
    enemyX_change.append(3)
    enemyY_change.append(10)
 

# Bullet
bulletImg = pygame.image.load("MainFolder/images/bullet-4.png")
bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change = 5
bullet_state = "ready"

score = 0


def player(x,y):
    screen.blit(playerImg, (x, y))

def enemy(x, y, h):
    screen.blit(enemyImg[h], (x, y))

def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x + 16, y + 10))

def isCollision (enemyX, enemyY, bulletX, bulletY,) :
    distance = math.sqrt((math.pow(enemyX - bulletX,2)) + (math.pow(enemyY - bulletY,2)))
    if distance <27 : 
        return True
    else:
        return False

#Game loop and event handler 
running = True
while running:

    screen.fill((32, 32, 32))
    #background
    screen.blit(background, (0, 0))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        # if arrow pressed is right or left
    if event.type == pygame.KEYDOWN:
        

        if event.key == pygame.K_LEFT:
            playerX_change = -5
            

        if event.key == pygame.K_RIGHT:
            playerX_change = 5
            

        if event.key == pygame.K_ESCAPE:
            if bullet_state == "ready":
                bulletX = playerX
                fire_bullet(bulletX, bulletY)
            
    if event.type == pygame.KEYUP:
        if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
            playerX_change = 0
            

# Setting the color of the game and 24 shows the color
    
    # created the spaceship movements
    playerX += playerX_change
    if playerX <= 0:
        playerX =0 
    elif playerX >= 733:
        playerX = 733

    # enemy movements
    for h in range(num_of_enemies) :
        enemyX[h] += enemyX_change[h]

        # Bound the enemy's movement
        if enemyX[h] <= 0 or enemyX[h] >= 736:
            enemyX_change[h] = -enemyX_change[h]
            enemyY[h] += enemyY_change[h]


    # Bullet movement
    if bulletY <= 0:
        bulletY = 480
        bullet_state = "ready"


    if bullet_state == "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change

    # collision 
    collision = isCollision(enemyX[h], enemyY[h], bulletX, bulletY)
    if collision: 
        bulletY = 480
        bullet_state = "ready"
        score += 1
        print(score)
        enemyX[h] = random.randint (0, 735)
        enemyY[h] = random.randint (50, 150)
        break

    player(playerX, playerY)
    enemy(enemyX[h], enemyY[h], h)
    
    pygame.display.update()