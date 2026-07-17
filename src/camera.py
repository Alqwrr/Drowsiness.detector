import cv2

from src.config import (
    CAMERA_ID,
    FRAME_WIDTH,
    FRAME_HEIGHT,
    ESP32_CAMERA_URL,
)


class Camera:

    def __init__(self):

        # Driver webcam
        self.face_cap = cv2.VideoCapture(CAMERA_ID)

        self.face_cap.set(
            cv2.CAP_PROP_FRAME_WIDTH,
            FRAME_WIDTH
        )

        self.face_cap.set(
            cv2.CAP_PROP_FRAME_HEIGHT,
            FRAME_HEIGHT
        )

        # Road camera (ESP32)
        self.road_cap = cv2.VideoCapture(
            ESP32_CAMERA_URL
        )

    def get_face_frame(self):

        ok, frame = self.face_cap.read()

        if ok:
            return frame

        return None

    def get_road_frame(self):

        ok, frame = self.road_cap.read()

        if ok:
            return frame

        return None

    def release(self):

        self.face_cap.release()
        self.road_cap.release()