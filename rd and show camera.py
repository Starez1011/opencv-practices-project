import cv2

cap = cv2.VideoCapture(0)
#write file.mp4 instead of 0 to open video file

#cap = cv2.VideoCapture('file.mp4')

#value can be 0,-1,1,2

#while(cap.isOpened()) --> it returns true if video is captured by camera otherwise false

while(True):
    #ret stores True if frame is availabe otherwise false
    #frame stores video footage
    ret,frame = cap.read()
    
    #to change video to grayscale or black and white
#[
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    cv2.imshow('frame',gray)
#]
    cap.get(cv2.CAP_PROP_FRAME_WIDTH) #--> to read the width of frame

    #cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
#after reading must release the resources or frame
cap.release()
cv2.destroyAllWindows()