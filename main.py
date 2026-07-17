import cv2
import numpy as np
import time


from src.camera import Camera
from src.face_mesh import FaceMeshDetector
from src.eye_detection import *
from src.drowsiness import DrowsinessDetector
from src.alarm import Alarm
from src.visualization import Visualizer
from vehicle.vehicle_controller import VehicleController

from interface.controls import VehicleControls
from interface.dashboard import Dashboard

controls = VehicleControls()

controls.start()


dashboard = Dashboard()

visualizer = Visualizer()

camera = Camera()

mesh = FaceMeshDetector()

drowsiness = DrowsinessDetector()

alarm = Alarm()

vehicle = VehicleController()

vehicle.connect()

cv2.namedWindow("Vehicle Camera", cv2.WINDOW_NORMAL)
cv2.resizeWindow("Vehicle Camera", 800, 600)

cv2.namedWindow("Driver Monitor", cv2.WINDOW_NORMAL)
cv2.resizeWindow("Driver Monitor", 900, 700)



while True:

    command = controls.get_command()

    start=time.time()


    face_frame = camera.get_face_frame()
    road_frame = camera.get_road_frame()

    if face_frame is None:
        break

    end = time.time()

    fps = int(
        1/(end-start))



    results = mesh.process(face_frame)

    ear = 0

    drowsy=False



    if results.multi_face_landmarks:


        face = results.multi_face_landmarks[0]


        h,w,_ = face_frame.shape


        left=[]
        right=[]


        for id in LEFT_EYE:

            point = face.landmark[id]

            left.append(
                [
                point.x*w,
                point.y*h
                ]
            )


        for id in RIGHT_EYE:

            point = face.landmark[id]

            right.append(
                [
                point.x*w,
                point.y*h
                ]
            )


        left=np.array(left)

        right=np.array(right)



        leftEAR = calculate_EAR(left)

        rightEAR = calculate_EAR(right)


        ear = (
            leftEAR+
            rightEAR
        )/2



        drowsy = drowsiness.update(
            ear
        )


#        frame = visualizer.display_status(
#            frame,
#            ear,
#            drowsy,
#            fps
#        )



    alarm.update(drowsy)



    if drowsy:

        command = "STOP"

        cv2.putText(
            face_frame,
            "DROWSINESS WARNING",
            (20,230),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0,0,255),
            3
        )

        vehicle.send(command)

    vehicle.send(command)

    face_frame = dashboard.draw(
        face_frame,
        "DROWSY" if drowsy else "ACTIVE",
        command,
        ear,
        drowsiness.get_score()
    )



    cv2.imshow(
    "Driver Monitor",
    face_frame
    )

    if road_frame is not None:

        cv2.imshow(
            "Vehicle Camera",
            road_frame
        )



    if cv2.waitKey(1)==ord("q"):

        break


vehicle.disconnect()
camera.release()

cv2.destroyAllWindows()