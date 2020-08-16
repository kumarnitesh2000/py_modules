import pygame
import time
pygame.init()

win=(800,600)
now_draw=False

last_pos=(0,0)
screen=pygame.display.set_mode(win)
pygame.display.set_caption("myGame")

def draw():
    pygame.draw.rect(screen, (255, 255, 255), (10, 10, 180, 60), 1)
    font = pygame.font.Font("Magnolia.ttf", 35)
    text = font.render("Reset Board", True, (255, 255, 255))
    screen.blit(text, (10, 10))
def is_Over(pos,x,width,y,height):
    if pos[0]>x and pos[0]<width+x:
        if pos[1]>y and pos[1]<height+y:
            return True

    return False

def clicked():
    screen.fill((0,0,0))
    pygame.display.update()

def roundline(srf, color, start, end):
    dx = end[0]-start[0]
    dy = end[1]-start[1]
    distance = max(abs(dx), abs(dy))
    for i in range(distance):
        x = int( start[0]+float(i)/distance*dx)
        y = int( start[1]+float(i)/distance*dy)
        pygame.draw.circle(srf, color, (x, y), 10)


run=True
while run:

    event=pygame.event.wait()
    if event.type == pygame.QUIT:
        run = False

    if event.type==pygame.MOUSEBUTTONDOWN:
        pygame.draw.circle(screen, (255,255,255), event.pos, 10)
        now_draw=True
        if is_Over(event.pos, 10, 180, 10, 60):
            clicked()
        if event.button==1:#print("left clicked mouse touch")
            pass
        elif event.button==3:#print("right clicked")
            pass
    if event.type == pygame.MOUSEBUTTONUP:
        now_draw = False
        # when we left the mouse
    if event.type == pygame.MOUSEMOTION:
        if now_draw:
            pygame.draw.circle(screen, (255, 255, 255), event.pos, 10)
            roundline(screen, (255,255,255), event.pos, last_pos)
        last_pos = event.pos


    draw()



    pygame.display.update()
    pygame.display.flip()
