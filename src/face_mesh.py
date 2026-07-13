import mediapipe as mp



class FaceMeshDetector:


    def __init__(self):

        self.face_mesh = (
            mp.solutions.face_mesh.FaceMesh(
                max_num_faces=1,
                refine_landmarks=True,
                min_detection_confidence=0.5
            )
        )



    def process(self, frame):

        rgb = frame[:,:,::-1]

        results = self.face_mesh.process(rgb)

        return results