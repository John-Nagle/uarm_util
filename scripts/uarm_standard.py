#!/usr/bin/env python
#
#   Evol UArm robot arm controller
#
#   Operates with UArm running the Arduino program "Standard".
#   Sends positional commands, no feedback from arm.
#
#   Version 1 - no delays, dumb version.
#
#   John Nagle
#   Animats
#
import rospy
import serial
from uarm_utils.msg import Standard_move
import uarm_standard_move

    
def run() :
    uarmport = rospy.get_param("/uarmport")                         # get USB serial device for UArm.
    ser = serial.Serial(uarmport, 9600, timeout=1)                  # open serial device
    def movecallback(m) :                                           # create a closure
        rospy.loginfo(rospy.get_caller_id() + "Move command: %s", repr(m))
        uarm_standard_move.moveto(ser, m.baserot, m.stretch, m.height, m.wristrot, m.cmd)     
    listener(movecallback)
    
def listener(callback):

    # In ROS, nodes are uniquely named. If two nodes with the same
    # node are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.
    rospy.init_node('uarm', anonymous=True)

    rospy.Subscriber("moveuarm", Standard_move, callback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    run()

