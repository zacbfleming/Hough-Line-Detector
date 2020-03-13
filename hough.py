import cv2
import numpy as np
import argparse

def get_args():
    parser = argparse.ArgumentParser("Hough line detector")
    v_desc = "Enter the voting threshold for a found line, default is 100 votes"
    i_desc = "Input the location of the image to be processed, default is shapes.png in the same folder"
    t_desc = "Enter theta, the angle step size in degrees. 1 to 180, 180 will use all degrees 1 thru 180, choose 1 to only use 0 degrees, default is 90, 2,4,6...,180 degrees"
    parser._action_groups.pop()
    required = parser.add_argument_group('required arguments')
    optional = parser.add_argument_group('optional arguments')
    optional.add_argument("-v", help=v_desc, default=110)
    optional.add_argument("-i", help=i_desc, default='shapes.png')
    optional.add_argument("-t", help=t_desc, default=90)
    args = parser.parse_args()
    return args



args = get_args()
votes = args.v
theta = np.pi/args.t
im = cv2.imread(args.i)
cv2.imshow('shapes', im)
cv2.waitKey(0)
cv2.destroyAllWindows()
gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
img_edge = cv2.Canny(gray, 150, 250,apertureSize = 3)
cv2.imshow('shapes', img_edge)
cv2.waitKey(0)
cv2.destroyAllWindows()

lines = cv2.HoughLines(img_edge, 1, theta, votes)
for line in lines:
    rho, theta = line[0]
    a = np.cos(theta)
    b =np.sin(theta)
    x0 = a*rho
    y0 = b * rho
    x1 = int(x0+1000*(-b))
    y1 = int(y0+1000*(a))
    x2 = int(x0 - 1000*(-b))
    y2 = int(y0 - 1000*(a))
    
    cv2.line(im, (x1, y1), (x2, y2), (0,255,0), 2)
    
cv2.imshow('Hough Lines', im)
cv2.waitKey(0)
cv2.destroyAllWindows()
