import cv2
import numpy as np
import time


from src.camera import Camera
from src.face_mesh import FaceMeshDetector
from src.eye_detection import *
from src.drowsiness import DrowsinessDetector
from src.alarm import Alarm
from src.visualization import Visualizer

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



while True:

    command = controls.get_command()

    start=time.time()


    frame = camera.get_frame()


    if frame is None:
        break

    end = time.time()

    fps = int(
        1/(end-start))



    results = mesh.process(frame)

    ear = 0

    drowsy=False



    if results.multi_face_landmarks:


        face = results.multi_face_landmarks[0]


        h,w,_ = frame.shape


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
            frame,
            "DROWSINESS WARNING",
            (20,230),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0,0,255),
            3
        )

    frame = dashboard.draw(
        frame,
        "DROWSY" if drowsy else "ACTIVE",
        command,
        ear,
        drowsiness.get_score()
    )



    cv2.imshow(
        "Driver Monitor",
        frame
    )



    if cv2.waitKey(1)==ord("q"):

        break



camera.release()

cv2.destroyAllWindows()