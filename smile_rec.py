import cv2

face_cascade = cv2.CascadeClassifier('F:\\Projects\\opencv-master\\data\\haarcascades\\'
                                     'haarcascade_frontalface_default.xml')
smile_cascade = cv2.CascadeClassifier('F:\\Projects\\opencv-master\\data\\haarcascades\\haarcascade_smile.xml')


def detect(frame):
    faces = face_cascade.detectMultiScale(frame, 1.1, 5)
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), ((x + w), (y + h)), (0, 255, 0), 2)
        font = cv2.FONT_HERSHEY_COMPLEX_SMALL
        cv2.putText(frame, 'Face', (x, y - 10), font, 1, (155, 155, 155), 1, cv2.LINE_4)
        roi_color = frame[y:y + h, x:x + w]
        smiles = smile_cascade.detectMultiScale(roi_color, 1.8, 20)

        for (sx, sy, sw, sh) in smiles:
            cv2.rectangle(roi_color, (sx, sy), ((sx + sw), (sy + sh)), (0, 0, 255), 2)
    return frame


def Simulator():
    video_capture = cv2.VideoCapture('C:\\Users\\N K Dubey\\OneDrive\\Desktop\\output.mp4')
    while video_capture.isOpened():
        ret, frame = video_capture.read()
        controlkey = cv2.waitKey(1)
        if ret:
            face_frame = detect(frame)
            cv2.imshow('frame', face_frame)
        else:
            break
        if controlkey == ord('q'):
            break

#video_capture = cv2.VideoCapture(0)
#while True:
 #   _, frame = video_capture.read()
  #  gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
   # canvas = detect(gray, frame)
    #cv2.imshow('Video', canvas)
    #if cv2.waitKey(1) & 0xff == ord('q'):
     #   break

    video_capture.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    Simulator()