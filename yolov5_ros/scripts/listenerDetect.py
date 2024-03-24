#!/usr/bin/env python

import rospy
from std_msgs.msg import String
from std_msgs.msg import Float64

def callback(data):
    rospy.loginfo(rospy.get_caller_id() + ' I heard %s', data.data)

def listener():
    
    # Initialisieren des Nodes zur Kommunikation mit ROS-Master
    rospy.init_node('listenerDetect', anonymous=True)

    # Abbonieren der Publisher-Informationen ueber die Topics
    subObj = rospy.Subscriber('object', String, callback)
    subDist = rospy.Subscriber('distance', Float64, callback)
    subX = rospy.Subscriber('x_coordinate', Float64, callback)
    subY = rospy.Subscriber('y_coordinate', Float64, callback)

    rospy.spin()

if __name__ == '__main__':
    listener()
