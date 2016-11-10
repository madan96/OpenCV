import cv2
import numpy as np

#List down all events
events = [i for i in dir(cv2) if 'EVENT' in i]
print events

#mouse callback
def draw_circle(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        cv2.circle(img, (x,y), 10, (255,0,0), 5)

#Create black image and bind function to window
img = np.zeros((512,512,3), np.uint8)
cv2.namedWindow('image', cv2.WINDOW_AUTOSIZE)
cv2.setMouseCallback('image', draw_circle)

while(1):
    cv2.imshow('image', img)
    if cv2.waitKey(20) & 0xFF == 27:
        break

cv2.destroyAllWindows()
