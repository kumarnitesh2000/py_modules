import network
import pygame
from pygame import mixer

pygame.init()


height=600
width=800
win_size=(width,height)
win=pygame.display.set_mode(win_size)
#background sounds
mixer.music.load("back_aud.mpeg")
mixer.music.play(-1)

#client info
client_num=0
class Player:
    def __init__(self,name,x,y,width,height,color):
        self.name=name
        self.x=x
        self.y = y
        self.width=width
        self.height=height
        self.color=color
        self.rect=(x,y,width,height)
        self.x_change=3
        self.y_change=3

    def draw(self,win):
        pygame.draw.rect(win,self.color,self.rect)

    def move(self):
        keys=pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.x-=self.x_change
        if keys[pygame.K_UP]:
            self.y-=self.y_change
        if keys[pygame.K_RIGHT]:
            self.x += self.x_change
        if keys[pygame.K_DOWN]:
            self.y += self.x_change
        self.update()
    def update(self):
        self.rect=(self.x,self.y,self.height,self.width)


def read_pos(string):
    #string=22,40
    string=string.split(",")
    return int(string[0]),int(string[1])


#to send to the server
def make_pos(tup):
    return str(tup[0])+","+str(tup[1])




def redraw_win(win,player,player2):
    win.fill((255,255,255))
    player.draw(win)
    player2.draw(win)
    pygame.display.update()





def main():
    run=True
    n=network.Network()
    start_pos=read_pos(n.getpos())
    #print(start_pos)

    p=Player("Nitesh",start_pos[0],start_pos[1],50,50,(0,255,0))
    #second player
    p2=Player("Anmol",0,0,100,100,(0,255,0))
    while run:
        p2pos=read_pos(n.send(make_pos((p.x,p.y))))
        p2.x,p2.y=p2pos[0],p2pos[1]
        p2.update()
        win.fill((255,255,255))
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                run=False

        p.move()
        redraw_win(win,p,p2)




#calling the main function

main()