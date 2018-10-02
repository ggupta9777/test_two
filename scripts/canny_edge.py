#!/usr/bin/env python

import rospy
import cv_bridge
import cv2
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError
import numpy as np
bridge = CvBridge ()

"""
  Callback for raw image data
"""
def raw_image_callback (msg):
  try:
    # ros to cv2 
    cv_image = bridge.imgmsg_to_cv2(msg, desired_encoding=msg.encoding)
    frame = np.array(cv_image, dtype=np.uint8)
    grey = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # Blur the image
    grey = cv2.blur(grey, (7, 7))
    # Compute edges using the Canny edge filter
    edges = cv2.Canny(cv_image, 100, 100)
    # back to ROS msg
    out_img = bridge.cv2_to_imgmsg(edges)
    # publish
    pub.publish (out_img)
  except CvBridgeError as e:
    print(e)

"""
  Setup the subscriber
"""
def init ():
  rospy.Subscriber ("/cv_camera/image_raw", Image, raw_image_callback)       
  rospy.spin ()

if __name__ == "__main__":
  rospy.init_node ("canny_image_node")
  pub = rospy.Publisher ('canny_image', Image, queue_size=1)
  init ()