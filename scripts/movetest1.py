#!/usr/bin/env python
#
#   movetest1 -- move the UARM around in a fixed pattern.
#
#   This is just to validate that everything is talking.
#
import rospy
from std_msgs.msg import String
from uarm_utils.msg import Standard_move

def talker():
    pub = rospy.Publisher('moveuarm', Standard_move, queue_size=10)
    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(0.2)                                  # 5 secs each
    movegen = nextmove(testmoves())                         # get some test moves
    
    while not rospy.is_shutdown():
        movemsg = movegen.next()                            # get next move
        rospy.loginfo(repr(movemsg))
        pub.publish(movemsg)
        rate.sleep()
        
#
#   nextmove - endlessly cycle through moves with a generator
#
def nextmove(moves) :
    while True :
        for move in moves :
            yield move
        
#
#   Generate move message 
#
def genmove(baserot, stretch, height, wristrot, cmd) :
    msg = Standard_move()                                   # did Catkin generate a positional constructor?
    msg.baserot = baserot
    msg.stretch = stretch
    msg.height = height
    msg.wristrot = wristrot
    msg.cmd = cmd
    return(msg)                                             # return filled in message        
        
#
#   Generate table of moves.  Run these SLOWLY 
#
def testmoves() :
    moves = []
    UP = 70
    DOWN = 0
    OUT = 150
    IN = 50
    WRIST0 = 0
    WRISTLIM = 80                                               # 85 degrees seems to be limit
    BASELIM = 80
    BASE0 = 0
    moves.append(genmove(BASE0,IN,DOWN,WRIST0,0))               # move in
    moves.append(genmove(BASE0 ,OUT,DOWN,WRIST0,0))             # move out
    moves.append(genmove(BASE0, OUT, DOWN, -WRISTLIM, 0))       # exercise wrist
    moves.append(genmove(BASE0, OUT, DOWN, WRISTLIM,0))
    moves.append(genmove(BASE0, OUT, DOWN, WRIST0,0))           # move up
    moves.append(genmove(BASE0,OUT, UP, WRIST0,0))
    moves.append(genmove(-BASELIM,OUT, UP, WRIST0,0))           # exercise base
    moves.append(genmove(BASELIM,OUT, UP, WRIST0,0))
    moves.append(genmove(BASE0,OUT, UP, WRIST0,0))
    moves.append(genmove(BASE0,IN,UP,WRIST0,0))                 # move back
    return(moves)

  

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
