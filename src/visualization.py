import cv2


class Visualizer:


    def __init__(self):

        pass



    def draw_eye_points(
        self,
        frame,
        points
    ):

        for point in points:

            x,y = point

            cv2.circle(
                frame,
                (int(x), int(y)),
                2,
                (0,255,0),
                -1
            )


        return frame



    def display_status(
        self,
        frame,
        ear,
        drowsy,
        fps
    ):


        if drowsy:

            status = "PLEASE STOP VEHICLE"

            color = (0,0,255)

            
            

        else:

            status = "DRIVER ACTIVE"

            color = (0,255,0)



        cv2.putText(
            frame,
            status,
            (20,40),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            color,
            3
        )


        cv2.putText(
            frame,
            f"FPS: {fps}",
            (800,30),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.7,
            (255,255,255),
            2
        )

        cv2.putText(
            frame,
            f"press q to exit",
            (800,20),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.7,
            (100,65,5),
            2
        )


        return frame