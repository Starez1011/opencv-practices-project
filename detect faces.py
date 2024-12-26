import cv2

# Load the pre-trained Haar Cascade classifier
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# Open the video file
cap = cv2.VideoCapture(0)

while True:
    # Read a frame from the video
    ret, frame = cap.read()

    # Break the loop if there are no more frames
    if not ret:
        break

    # Convert the frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces in the frame
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=4)

    # Draw rectangles around the detected faces
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 3)

    # Display the output frame
    cv2.imshow('Frame', frame)

    # Exit when 'q' is pressed
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

# Release the video capture and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()
