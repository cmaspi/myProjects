# import openCV
import cv2

# object to capture video
vid = cv2.VideoCapture(0)

while(True):

    # vid.read() would return 
    # a number whether the command has been successful
    # and and image
    ret,frame=vid.read()

    cv2.imshow('frame',frame)

    # it will produce a new frame every 1ms
    # there is computation delay though
    # ord('q') refers to ascii code of letter q
    #  
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

vid.release()

cv2.destroyAllWindows