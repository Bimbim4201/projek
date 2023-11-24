import numpy as np
import cv2

class VideoProcessor:
    def __init__(self):
        self.cap = cv2.VideoCapture(0)

    def process_video(self):
        while True:
            ret, frame = self.cap.read()
            width = int(self.cap.get(3))
            height = int(self.cap.get(4))

            img = self.draw_lines(frame, width, height)
            img = self.draw_rectangle(img)
            img = self.draw_circle(img)
            img = self.draw_text(img, height)

            cv2.imshow('frame', img)

            if cv2.waitKey(1) == ord('q'):
                break

        self.cap.release()
        cv2.destroyAllWindows()

    def draw_lines(self, img, width, height):
        img = cv2.line(img, (0, 0), (width, height), (255, 0, 0), 10)
        img = cv2.line(img, (0, height), (width, 0), (0, 255, 0), 5)
        return img

    def draw_rectangle(self, img):
        img = cv2.rectangle(img, (100, 100), (200, 200), (128, 128, 128), 5)
        return img

    def draw_circle(self, img):
        img = cv2.circle(img, (300, 300), 60, (0, 0, 255), -1)
        return img

    def draw_text(self, img, height):
        font = cv2.FONT_HERSHEY_SIMPLEX
        img = cv2.putText(img, 'BIMBIM GYATTT', (10, height - 10), font, 1, (28, 172, 255), 3, cv2.LINE_AA)
        return img

# Usage example
video_processor = VideoProcessor()
video_processor.process_video()
