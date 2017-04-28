'''

This project is to implement a dlib face detection and object tracking.

Steps

1. Initialize the web cam to grab frames
2. Check if there is a face in the frame - if there is one proceed else , repeat the same loop till a face is detected
3. After the first face is detected the bounding box of the face is given to the objecttracking obj to track the face in the subsequent frames
4. Since the object tracker just tracks the object and does not perform any detection, it my loose the object,
    hence we update the tracked with a new detected face after every 100 frames.


This project can be extended to deted and track pedestrians in an image, but care has to be taken to detect every pedestrian seperately,
Also steps to speed up this process for multi object tracking in every frame would be required


'''



import dlib
import cv2


#initialize he vide capture object to read the default web cam connected to the computer
# we can set 0 or 1 if there are other webcams available
cap = cv2.VideoCapture(0)

#initialize the tracker
tracker = dlib.correlation_tracker()
#initialize the face detector
detector = dlib.get_frontal_face_detector()
#initialize the diaplay window
win = dlib.image_window()



while(True):
    # Capture 1st frame
    ret, frame = cap.read()
    # convert image to gray scale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    #show the frame
    win.clear_overlay()
    win.set_image(gray)
    #check for face in the frame
    dets = detector(gray, 1)
    win.add_overlay(dets)

    #stay in this loop till we capture a face inside the frame
    if len(dets)>=1:
        break




#after this start tracking the face in the frames
dlib.hit_enter_to_continue() #press any key to continue

#initializa the tracker to track the face in the frame
tracker.start_track(gray, dets[0])

#initialize the frame, and use the frame number to perform specific tasks during the process
frameNo = 0

#infinite loop to continuously track the faces in the frames after the first one
while(True):
    #capture frame
    ret, frame = cap.read()
    #convert it to gray scale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    #update the tracker for the face
    tracker.update(gray)

'''
    after every 100 frames check if the face is really there
    this is required because if the face is lost, it keep tracking a wrong object,
    so we need to keep checking for a face in the frame again and again
'''
    # check for a face in the frame after every 100 frames
    if frameNo != 0 and frameNo%100==0:
        dets = detector(gray, 1)
        if len(dets)>=0:
            win.clear_overlay()
            win.set_image(gray)
            win.add_overlay(dets)
            tracker.start_track(gray, dets[0])
            frameNo = 0 #set frame to 0 just so that it does not overflow

    win.clear_overlay()
    win.set_image(gray)
    #update the display to show the tracked face
    win.add_overlay(tracker.get_position())
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    frameNo = frameNo+1

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()