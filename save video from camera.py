import cv2

cap = cv2.VideoCapture(0)

#Setting Camera Parameter 
cap.set(3,1280)#-->width is set to 1280
cap.set(4,720)#-->height is set to 720
#here 3 and 4 is the code for width and height which is same as cv2.CAP_PROP_FRAME_WIDTH/HEIGHT

#4cc code is used to specify video codec check opencv documentation
#here XVID is video codec
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('copy.mp4',fourcc,30.0,(1280,720))
#out = cv2.VideoWriter('file.mp4',video codec , fps , frame size)
while(cap.isOpened()):
    ret,frame = cap.read()
    if(ret == True):
        #print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))#--> to get height of frame/video
        #print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))#--> to get width of frame/video
        out.write(frame)
        cv2.imshow('frame',frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

cap.release()
out.release()
cv2.destroyAllWindows() 
