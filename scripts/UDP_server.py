#!/usr/bin/env python3

# Python libs
import sys, time

# numpy and scipy
import numpy as np
#from scipy.ndimage import filters

# OpenCV
""" ros_path = '/opt/ros/kinetic/lib/python2.7/dist-packages'
if ros_path in sys.path:
    sys.path.remove(ros_path)
import cv2
sys.path.append('/opt/ros/kinetic/lib/python2.7/dist-packages') """
import cv2


# Ros libraries
import roslib
import rospy

# Ros Messages
from sensor_msgs.msg import CompressedImage
# We do not use cv_bridge it does not support CompressedImage in python
# from cv_bridge import CvBridge, CvBridgeError
import socket 
import os
import struct
FORMAT = "utf-8"      

def sub_server(localIP,localPort):
    # Create a datagram socket
    UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
    # Bind to address and ip
    UDPServerSocket.bind((localIP,localPort))
    print("UDP server up and listening")
    # Listen for incoming datagrams
    count=0
    while not rospy.is_shutdown():
        bytesAddressPair = UDPServerSocket.recvfrom(1024)
        message = bytesAddressPair[0]
        address = bytesAddressPair[1]
        clientMsg = "Message from Client:{}".format(message)
        clientIP  = "Client IP Address:{}".format(address)    
        print(clientMsg)
        print(clientIP)   
        count=count+1
        print(count) 

if __name__ == "__main__":
    '''
        initialize the node and the publisher
    '''

    rospy.init_node('UDP_server', anonymous=True)
    
	## getting the IP address 
    ip_add = [l for l in ([ip for ip in socket.gethostbyname_ex(socket.gethostname())[2] if not ip.startswith("127.")][:1], [[(s.connect(('8.8.8.8', 53)), s.getsockname()[0], s.close()) for s in [socket.socket(socket.AF_INET, socket.SOCK_DGRAM)]][0][1]]) if l][0][0]
    print("IP Address: ", ip_add)
    
    #creating the server at the specified ip and port
    sub_server(ip_add,8888)

    #uncomment this if the auto-recognition of the Ip doesn't work
    #sub_server(("192.168.1.195",8888)) 
