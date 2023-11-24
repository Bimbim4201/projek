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

            result = self.apply_color_mask(frame)

            cv2.imshow('frame', result)
            cv2.imshow('mask', self.create_mask(frame))

            if cv2.waitKey(1) == ord('q'):
                break

        self.cap.release()
        cv2.destroyAllWindows()

    def create_mask(self, frame):
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        lower_blue = np.array([50, 50, 50])
        upper_blue = np.array([130, 255, 255])
        mask = cv2.inRange(hsv, lower_blue, upper_blue)
        return mask

    def apply_color_mask(self, frame):
        mask = self.create_mask(frame)
        result = cv2.bitwise_and(frame, frame, mask=mask)
        return result

# Usage example
video_processor = VideoProcessor()
video_processor.process_video()
