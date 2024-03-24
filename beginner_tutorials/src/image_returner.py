import numpy as np
import cv2
import rospy
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError

def callback(msg):
    cvBridge = CvBridge()

    rospy.loginfo("receiving image")

    current_frame = cvBridge.imgmsg_to_cv2(msg)

    returnImage = cvBridge.cv2_to_imgmsg(current_frame, encoding="passthrough")

    rospy.loginfo("publishing image back")

    imagePublisher.publish(returnImage)


if __name__ == '__main__':
    rospy.init_node("ROSImageReturner")
    imagePublisher = rospy.Publisher('return_image', Image, queue_size=10)
    imageSubscriber = rospy.Subscriber('camera_image', Image, callback)
    rospy.spin()


