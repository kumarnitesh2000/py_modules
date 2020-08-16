from _thread import *
import time

def target_function(player,delay,limit):

    #count=0
    #limit concept will came into mind at the time of infinite looping : deadlock occurs
    while limit:
        time.sleep(delay)
        #count+=1
        if player==1:
            limit-=1
        elif player==2:
            limit+=1
        print("player no . ",player,"with time : ",time.ctime(time.time()))


try:
    delay=3
    player=1
    limit=2
    start_new_thread(target_function,(player,delay,limit))
    player+=1
    start_new_thread(target_function, (player, delay,limit))
    player += 1
    start_new_thread(target_function, (player, delay,limit))


except:
    pass

while 1:
    pass



