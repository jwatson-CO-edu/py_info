# NASDAQ hours: 9:30 a.m. to 4:00 p.m. EST (8:30 a.m. to 3:00 p.m. CST)

# For the use of the timer
import time
# To retrieve the time
from time import localtime


# Useful values
STDSLEEP = 3 # 3 seconds



def pause(pauseTime):
    time.sleep(pauseTime)
    
def is_game_time(startHour,startMin,endHour,endMin):
    gameTime = False
    preGame = False
    data = localtime()
    if (data[3] > startHour or (data[3] == startHour and data[4] >= startMin)):
        gameTime = True
        print "gametime true"
    if (data[3] > endHour or (data[3] == endHour and data[4] >= endMin)):
        gameTime = False
        print "gametime false"
    if (data[3] < startHour or (data[3] == startHour and data[4] < startMin)):
        preGame = True
        print "pregame true"
    return gameTime,preGame
    
    
def main(sleepTime):
    startHour = int(raw_input("Enter clock hour of start time (0-23): "))
    startMin = int(raw_input("Enter clock minutes of start time (0-59): "))
    endHour = int(raw_input("Enter clock hour of end time (0-23): "))
    endMin = int(raw_input("Enter clock minutes of end time (0-59): "))
    data = localtime()
    keepGoing = True
    gamefile = open("gamefile.txt","w")
    while keepGoing:
        timeStates = is_game_time(startHour,startMin,endHour,endMin)
        gamefile.write("beep" + str(localtime()[3]) + str(localtime()[4]) + str(localtime()[5]))
        if timeStates[0]:
            gamefile.write("bonk" + str(localtime()[3]) + str(localtime()[4]) + str(localtime()[5]))
        elif not timeStates[1]:
            keepGoing = False
        pause(sleepTime)
    gamefile.close()
                
        
main(STDSLEEP)
