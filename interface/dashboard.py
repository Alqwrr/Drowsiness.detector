import cv2



class Dashboard:


    def __init__(self):

        pass



    def draw(
        self,
        frame,
        driver_status,
        command,
        ear,
        score
    ):


        height, width, _ = frame.shape


        # Information panel

        cv2.rectangle(
            frame,
            (0,0),
            (300,200),
            (89,42,0),
            -1
        )


        cv2.putText(
            frame,
            "DRIVER MONITOR",
            (20,30),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.7,
            (255,255,255),
            2
        )


        cv2.putText(
            frame,
            f"STATUS: {driver_status}",
            (20,70),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.6,
            (0,255,0),
            2
        )


        cv2.putText(
            frame,
            f"COMMAND: {command}",
            (20,110),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.6,
            (255,255,255),
            2
        )


        cv2.putText(
            frame,
            f"EAR: {ear:.2f}",
            (20,150),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.6,
            (255,255,255),
            2
        )


        cv2.putText(
            frame,
            f"SCORE: {score}",
            (20,190),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.6,
            (255,255,255),
            2
        )


        return frame