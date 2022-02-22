import cv2 as cv

# simplier way to do the same face detection

# Load the cascade
# face_cascade = cv.CascadeClassifier('haarcascade_frontalface_default.xml')
# # To capture video from webcam. 
# video = cv2.VideoCapture(0)
# # To use a video file as input 
# # cap = cv2.VideoCapture('filename.mp4')
# while True:
#     flag, frame = video.read()
#     gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#     faces = face_cascade.detectMultiScale(gray_frame, 1.1, 4)
#     for (x, y, w, h) in faces:
#         cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 69, 255), 2)
#         print(f"Face found at x: {x}, y: {y}, w: {w}, h: {h}")
#     cv2.imshow('Face Detector', frame)
#     k = cv2.waitKey(30) & 0xff
#     if k==27:
#         break
# video.release()


# slight advance procedure to detect faces with eyes


def detect_and_display(frame):
    frame_gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    frame_gray = cv.equalizeHist(frame_gray)

    faces = face_cascade.detectMultiScale(frame_gray, 1.1, 4)
    for (x,y,w,h) in faces:
        # top line of face recogniszed
        frame = cv.line(frame, (x,y), (x+w,y), (0,69,255), 2 )
        # bottom line of face recogniszed
        frame = cv.line(frame, (x,y+h), (x+w,y+h), (0,69,255), 2 )
        
        # top to bootom lines
        frame = cv.line(frame, (x,y), (x,y+20), (0,69,255), 4 )
        frame = cv.line(frame, (x+w,y), (x+w,y+20), (0,69,255), 4 )

        # bottom to top lines
        frame = cv.line(frame, (x,y+h), (x,y+h-20), (0,69,255), 4 )
        frame = cv.line(frame, (x+w,y+h), (x+w,y+h-20), (0,69,255), 4 )

        print(f"Face at x: {x}, w:{w}")

        faceROI = frame_gray[y:y+h,x:x+w]
        eyes = eyes_cascade.detectMultiScale(faceROI,scaleFactor=1.5)
        for (x1,y1,w1,h1) in eyes:
            frame = cv.rectangle(frame, (x+x1,y+y1), (x+x1+w1,y+y1+h1), (255,0,0),2)



    cv.imshow("Face Detector", frame)



face_cascade = cv.CascadeClassifier('haarcascade_frontalface_default.xml')
eyes_cascade = cv.CascadeClassifier('haarcascade_eye_tree_eyeglasses.xml')


video = cv.VideoCapture(0)

if not video.isOpened:
    print("Couldn't open Video Capure")
    exit(0)

while True:
    flag, frame = video.read()

    if frame is None:
        print("No captured frame")
        break

    detect_and_display(frame)
    
    # press Esc Key to exit the screen
    if cv.waitKey(10) == 27:
        break

video.release()
cv.destroyAllWindows()