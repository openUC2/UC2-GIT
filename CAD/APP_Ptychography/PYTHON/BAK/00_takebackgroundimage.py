import cv2 
import time

# camera paramters 
myexp_time = 199029
mycamera = '/dev/video0'

mycam_cmd = 'v4l2src device='+ mycamera+ ' ! video/x-raw, format=BGRx ! ximagesink'

cap = cv2.VideoCapture(mycam_cmd, cv2.CAP_GSTREAMER)


# take a background image first! 
print("Blank the beam for five seconds") 
#time.sleep(5)
ret_val, img = cap.read()
time.sleep(1)

 # write out the image information
cv2.imwrite('./background.png', img)
