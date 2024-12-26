import numpy as np
import cv2
#black image
img = np.zeros([512,512,3],np.uint8)
#draw line(img,start,end,color(B-G-R format),thickness)
img = cv2.line(img,(0,0),(255,255),(255,0,0),5)
#draw arrowline
img = cv2.arrowedLine(img,(0,255),(255,255),(255,255,0),5)
#draw rectangle(img,(x1,y1),(x2,y2),color,thickness)
# (x1,y1)-----
# |           |
# |___________(x2,y2)
img = cv2.rectangle(img,(384,0),(510,128),(0,0,255),5)
#circle(img,center,radius,color,thickness)
img = cv2.circle(img,(447,63),63,(0,255,0),-1)
#when thickness is -1 then the shape is filled with specified color
#draw text on image i.e text(img,'text',start,font,font size,color,thickness,line type)
font = cv2.FONT_HERSHEY_SIMPLEX
img = cv2.putText(img,'OpenCV',(10,500),font,4,(255,255,255),10,cv2.LINE_AA)

cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()