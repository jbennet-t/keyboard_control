#!/usr/bin/env python

#Program: keyboard_input.py
#Purpose: Acts as a publisher to the /cmd_vel topic and takes keyboard input to control ros robot
#Authors: Jordan Sinoway,

import rospy
import sys, select, termios, tty #alternative keyboard input

#import getch #theoretically gets keyboard input. need pip3 to install
#to install 'pip3 install getch'

from geometry_msgs.msg import Twist #import geometry stuff
from std_msgs.msg import String #for pushing info to terminal

'''
def get_keys(): #gets keyboard input
    key = 0
    k = ord(getch.getch()) #converts keypress to ord value
    if((k>=65)&(key<=68)):
        key = 1 #up
    elif (k==115):
        key = 2 #down
    elif (k==113):
        key = 3 #left
    elif (k==97):
        key = 4 #right
    else:
        key = 8
    rospy.loginfo(str(key)) #write val to terminal
    return key
'''

def get_keys():
    tty.setraw(sys.stdin.fileno())
    select.select([sys.stdin], [], [], 0)
    key = sys.stdin.read(1)
    termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)
    rospy.loginfo(str(key))
    return key

'''
def keyboard_input():
    pub = rospy.Publisher('cmd_vel', Twist, queue_size=1) #publishing to cmd_vel
    rospy.init_node('keyboard_input')

    speed = rospy.get_param("~speed", 0.5) #default speed val
    turn = rospy.get_param("~turn", 1.0) #default turn val
    x = 0
    y = 0
    z = 0
    th = 0
    status = 0

    while(1):
        input = get_keys()
        if(input == 1): #up
            x = 1
            y = 0
            z = 0
            th = 0
        elif(input == 2): #down
            x = -1
            y = 0
            z = 0
            th = 0
        elif(input == 3): #left
            x = 0
            y = 0
            z = 0
            th = 1
        elif(input == 4): #right
            x = 0
            y = 0
            z = 0
            th = -1
        else:
            x = 0
            y = 0
            z = 0
            th = 0

        twist = Twist()
        twist.linear.x = x*speed
        twist.linear.y = y*speed
        twist.linear.z = z*speed
        twist.angular.x = 0
        twist.angular.y = 0
        twist.angular.z = th*turn
        pub.publish(twist)
'''


if __name__ == '__main__':
    settings = termios.tcgetattr(sys.stdin)

    try:
        while(1):
            get_keys()
    except rospy.ROSInterruptException:
        pass
