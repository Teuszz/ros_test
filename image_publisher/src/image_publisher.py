#!/usr/bin/env python3

import numpy as np
import cv2
import rospy
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError

class ROSImagePublisher(object):
    def __init__(self):
        rospy.loginfo("Initialising object to publish a camera stream to a ROS topic")

        self.cameraFile = cv2.VideoCapture(0) # 0 for Video Device Nr. 0
        self.imagePublisher = rospy.Publisher("camera_image", Image, queue_size=10)
        self.cvBridge = CvBridge()

        rospy.loginfo("Object initialised to publish a camera stream to a ROS topic")

    def publish(self):
        while(self.cameraFile.isOpened()):
            ret, frame = self.cameraFile.read()
            imageMessage = self.cvBridge.cv2_to_imgmsg(frame, encoding="passthrough")
            self.imagePublisher.publish(imageMessage)
    
    def run(self):
        r = rospy.Rate(10)
        while not rospy.is_shutdown():
            self.publish()
            r.sleep()
        self.cameraFile.release()

if __name__ == '__main__':
    rospy.init_node("ROSImagePublisher")
    imagePublisher = ROSImagePublisher()
    imagePublisher.run()