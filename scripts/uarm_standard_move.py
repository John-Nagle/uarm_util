#
#   Evol UArm robot arm controller
#
#   Operates with UArm running the Arduino program "Standard".
#   Sends positional commands, no feedback from arm.
#   No delays, just dumb movement command sends.
#
#   John Nagle
#   nagle@animats.com
#   November, 2015
#
import struct
#
#   Message format to uarm is documented here:
#   https:#dl.dropboxusercontent.com/u/37860507/uArm%20Serial%20Protocol.pdf
#
#   This is for the uArm program called "Standard"
#
#   Message format is:
#       Start of frame 1 (0xff)
#       Start of frame 2 (0xaa)
#       Base rotation (2 bytes)
#       Stretch (2 bytes)
#       Height (2 bytes)
#       Wrist (2 bytes)
#       Grip and mouse control (1 byte)
#
#
#   Constants
#
STARTOFFRAME0 = 0xff
STARTOFFRAME1 = 0xaa
#
#
#   moveto  --  move to indicated X,Y,Z,R coords.
#
def moveto(fd, baserot, stretch, height, wristrot, cmd) :
    #   Construct message to send over serial line.
    msg = struct.pack(">BBhhhhB", STARTOFFRAME0, STARTOFFRAME1, round(baserot), round(stretch), round(height), round(wristrot), cmd)
    assert(len(msg) == 11)
    fd.write(msg)                           # send to robot
    fd.flush()                              # now

