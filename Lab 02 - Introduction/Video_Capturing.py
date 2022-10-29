import cv2

# video = cv2.VideoCapture(0) # to read from the camera 
video = cv2.VideoCapture('./Images/video.mp4') 

while(True):
    # Capture frame-by-frame
    ret, frame = video.read() # ret is a bool variable tells whether the reading was successful or not

    # Our operations on the frame come here
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Display the resulting frame
    cv2.imshow('frame', frame)

    # Press Q on keyboard to  exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
video.release()
cv2.destroyAllWindows()