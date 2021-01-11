#!/usr/bin/env python3.6
from __future__ import print_function
from cv_bridge import CvBridge, CvBridgeError
from sensor_msgs.msg import Image
from std_msgs.msg import String
import cv2
import rospy
from inference import DeepLabModel, label_to_color_image
import sys
from matplotlib import gridspec
import numpy as np
from virtual_guide import Add_Guide
import time
from matplotlib.animation import FuncAnimation
print("Python version")
print(sys.version)
# print(python.__version__)

print(cv2.__version__)


class image_converter:

    def __init__(self):
        self.image_pub = rospy.Publisher("/camera/image_raw", Image)

        self.bridge = CvBridge()
        self.image_model = DeepLabModel(
            "/home/soliman/catkin_ws/src/robo_sim/scripts/models/mobilev2indoor_stride16_90000.tar.gz")

        self.image_sub = rospy.Subscriber(
            "/camera/rgb/image_raw", Image, self.callback)

    def visualize(self):
        seg_image_overlay = cv2.addWeighted(
            self.seg_image, 0.8, self.resized_cv_img, 0.05, 0)

        img_concate_Hori = np.concatenate(
            (self.resized_cv_img,  seg_image_overlay), axis=1)
        cv2.imshow("images", img_concate_Hori)
        cv2.waitKey(3)

    def callback(self, data):
        time_start = time.time()
        self.cv_image = self.bridge.imgmsg_to_cv2(data, "bgr8")
        self.resized_image, self.seg_map = self.image_model.run(self.cv_image)
        self.seg_image = label_to_color_image(self.seg_map).astype(np.uint8)

        self.resized_image = self.resized_image.convert('RGB')
        self.resized_cv_img = np.array(self.resized_image)
        self.visualize()
        time_final = time.time()
        delta_t = (time_final - time_start)
        print("[INFO] Execution time: ", delta_t)

        # try:
        # self.image_pub.publish(data)
        # except CvBridgeError as e:
        # print(e)


def main(args):

    rospy.init_node('image_converter', anonymous=True)

    ic = image_converter()
    try:
        rospy.spin()
    except KeyboardInterrupt:
        print("Shutting down")
        cv2.destroyAllWindows()


if __name__ == '__main__':
    main(sys.argv)
