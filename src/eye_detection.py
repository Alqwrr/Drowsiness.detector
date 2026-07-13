import numpy as np


LEFT_EYE = [
    362,
    385,
    387,
    263,
    373,
    380
]


RIGHT_EYE = [
    33,
    160,
    158,
    133,
    153,
    144
]



def calculate_EAR(points):


    vertical1 = np.linalg.norm(
        points[1] - points[5]
    )


    vertical2 = np.linalg.norm(
        points[2] - points[4]
    )


    horizontal = np.linalg.norm(
        points[0] - points[3]
    )


    ear = (
        vertical1 + vertical2
    ) / (
        2.0 * horizontal
    )


    return ear