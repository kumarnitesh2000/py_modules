import pygame
from pygame import mixer
import math
import random
pygame.init()
#initialize the pygame
win_size=(800,600)
screen=pygame.display.set_mode(win_size)
#background img and bullet
background=pygame.image.load('img.png')
#background sounds
mixer.music.load("background.wav")
mixer.music.play(-1)


#title and icons
pygame.display.set_caption("SPACE Bots")
icon=pygame.image.load('alien.png')
pygame.display.set_icon(icon)

#players

player=pygame.image.load('space.png')
playerX=370
playerY=480

#bullet
bullet=pygame.image.load('bull.png')
bulletX=0
bulletY=480
#so you cant see the bullet on the screen
#fire motion
bullet_state="ready"

#enemy
enymy=[]
enymyX=[]
enymyY=[]
enymyX_change=[]
enymyY_change=[]
n_enemy=6
for i in range(n_enemy):

    enymy.append(pygame.image.load('alienpic.png'))
    enymyX.append(random.randint(0,800))
    enymyY.append(0)
    enymyX_change.append(0.8)
    enymyY_change.append(0)


def playermove(posx=370,posy=480):
    screen.blit(player,(posx,posy))

def alienmove(enymyx,enymyy,i):
    screen.blit(enymy[i],(enymyx,enymyy))

def fire_bullet(x,y):
    global bullet_state
    bullet_state="fire"
    screen.blit(bullet,(x+16,y+10))


def is_collision(enemyx,enemyy,bulletx,bullety):
    distance=math.sqrt(math.pow(enemyx-bulletx,2)+math.pow(enemyy-bullety,2))
    if distance < 27:
        return True
    return False

#Scores -> display here

score=0
#for font go to dafont.com
font=pygame.font.Font("Magnolia.ttf",32)
#font=pygame.font.Font("freesansbold.ttf",32)
textX=10
textY=10


def show_score(x,y):
    score_show=font.render("Score is : "+str(score),True,(255,255,255))
    screen.blit(score_show,(x,y))
#game over
over_textX=160
over_textY=250
game_over_font=pygame.font.Font("freesansbold.ttf",70)
def game_over_text(x,y):
    game_over=game_over_font.render(" GAME OVER ",True,(0,0,0))
    screen.blit(game_over,(x,y))


#game loops

run=True
#score=0
while run:
    screen.fill((0, 0, 0))

    #background image
    boundaries=(0,0)
    screen.blit(background,boundaries)
    #playerY-=0.1

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False
    #red green blue
    #check if key stroke is pressed or not .
    if event.type==pygame.KEYDOWN:#hence keystoke is pressed
        if event.key==pygame.K_LEFT:
            playerX-=0.8
        if event.key==pygame.K_RIGHT:
             playerX+=0.8
        if event.key == pygame.K_SPACE:
            #bulletY+=20
            if bullet_state is "ready":
                #means now bullet can be shoot
                bullet_sound=mixer.Sound("laser.wav")
                bullet_sound.play()
                bulletX=playerX
                fire_bullet(bulletX,bulletY)
    if event.type==pygame.KEYUP:
        if event.key==pygame.K_DOWN:
            playerY+=0.8
        if event.key==pygame.K_UP:
            playerY-=0.8
    if playerX<=2 or playerX>=795 or playerY<=2 or playerY>=594:
        screen.fill((240, 0, 0))
        pygame.display.update()


    #enemy movement

    for i in range(n_enemy):
        #game over
        if enymyY[i]>450:
            for j in range(n_enemy):
                enymyY[i]=2000

            screen.fill((255,0,0))
            game_over_text(over_textX, over_textY)
            break
            #display game over




        enymyX[i]+=enymyX_change[i]
        if enymyX[i]>=740:
            enymyX_change[i]=-1.7
            enymyY[i] += 30
        elif enymyX[i]<=0:
            enymyX_change[i]=1.7
            enymyY[i] += 30

        # collision
        collision = is_collision(enymyX[i], enymyY[i], bulletX, bulletY)
        if collision:
            coll_sound = mixer.Sound("explosion.wav")
            coll_sound.play()
            bulletY = 480
            bullet_state = "ready"
            score += 1
            print(score)
            enymyX[i]+=random.randint(50,150)
            enymyY[i]-=random.randint(50,150)

        alienmove(enymyX[i], enymyY[i],i)

    #bullet mechanics

    if bullet_state=="fire":
        fire_bullet(bulletX,bulletY)
        bulletY-=4
    if bulletY<=0:
        bulletY=480
        bullet_state="ready"

    #enymyX+=enymyX_change
    #enymyY-=enymyY_change
    playermove(playerX,playerY)
    show_score(textX, textY)
    pygame.display.update()



    #time.sleep(4)
    #run=False
