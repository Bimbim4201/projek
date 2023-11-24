import cv2

class FaceDetector:
    def __init__(self):
        self.face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
        self.eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')

    def detect_faces(self, frame):
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = self.face_cascade.detectMultiScale(gray, 1.3, 3)
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 3)
            roi_gray = gray[y:y+w, x:x+w]
            roi_color = frame[y:y+h, x:x+w]
            self.detect_eyes(roi_color, roi_gray)

    def detect_eyes(self, roi_color, roi_gray):
        eyes = self.eye_cascade.detectMultiScale(roi_gray, 1.3, 3)
        for (ex, ey, ew, eh) in eyes:
            center = (ex + ew // 2, ey + eh // 2)
            radius = min(ew, eh) // 2
            cv2.circle(roi_color, center, radius, (0, 255, 0), 3)

class Webcam:
    def __init__(self):
        self.cap = cv2.VideoCapture(0)
        self.face_detector = FaceDetector()

    def run(self):
        while True:
            ret, frame = self.cap.read()
            self.face_detector.detect_faces(frame)
            cv2.imshow('frame', frame)

            if cv2.waitKey(1) == ord('q'):
                break

        self.cap.release()
        cv2.destroyAllWindows()

# Gunakan contoh penggunaan
webcam = Webcam()
webcam.run()
