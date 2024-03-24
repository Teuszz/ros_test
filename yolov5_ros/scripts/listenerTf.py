#!/usr/bin/env python

import rospy
from std_msgs.msg import String
from std_msgs.msg import Float64

import math
import tf2_ros
import tf2_msgs.msg
import geometry_msgs.msg

def callbackObj(data):
    rospy.loginfo('Objekt: %s', data.data)

def callbackTf(msg):
    
    x = msg.transforms[0].transform.translation.x
    y = msg.transforms[0].transform.translation.y
    z = msg.transforms[0].transform.translation.z
    rospy.loginfo('x: {}, y: {}, z: {}'.format(x, y, z))
    

def listener():

    rospy.init_node('listenerDetect', anonymous=True)
        
    rate = rospy.Rate(10.0)
        
    subObj = rospy.Subscriber('object', String, callbackObj)
    #subDist = rospy.Subscriber('distance', Float64, callback)
    #subX = rospy.Subscriber('x_coordinate', Float64, callback)
    #subY = rospy.Subscriber('y_coordinate', Float64, callback)
    subTf = rospy.Subscriber('/tf', tf2_msgs.msg.TFMessage, callbackTf)

    rospy.spin()

if __name__ == '__main__':
    listener()
