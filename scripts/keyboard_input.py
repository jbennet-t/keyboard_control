#!/usr/bin/env python


#Authors: Jordan Sinoway,

import rospy
import getch


from geometry_msgs.msg import Twist

def get_keys():
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
            pass
        rospy.loginfo(key)
        return key

def keyboard_input():
    pub = rospy.Publisher('cmd_vel', Twist, queue_size=1)
    rospy.init_node('keyboard_input')

    speed = rospy.get_param("~speed", 0.5)
    turn = rospy.get_param("~turn", 1.0)
    x = 0
    y = 0
    z = 0
    th = 0
    status = 0

    while(1):
        key = get_keys()
        if(key = 1):
            x = 1
            y = 0
            z = 0
            th = 0
        elif(key = 2):
            x = -1
            y = 0
            z = 0
            th = 0
        elif(key = 3):
            x = 0
            y = 0
            z = 0
            th = 1
        elif(key = 4):
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





if __name__ == '__main__':
    try:
        keyboard_input()
    except rospy.ROSInterruptException:
        pass
