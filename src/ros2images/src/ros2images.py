import rospy
from std_msgs.msg import String
from sensor_msgs.msg import Image
import cv2
import numpy as np
from cv_bridge import CvBridge, CvBridgeError

i = 0

def callback(data):
    bridge = CvBridge()
    try:
      img = bridge.imgmsg_to_cv2(data, "bgr8")
    except CvBridgeError as e:
      print(e)
    global i
    name = "out/images_"+str(i)+".png"
    print(name)
    i = i + 1
    cv2.imwrite(name,img)


if __name__ == '__main__':
    rospy.init_node('listener', anonymous=True)
    rospy.Subscriber("/d400/color/image_raw", Image, callback)
    rospy.spin()
