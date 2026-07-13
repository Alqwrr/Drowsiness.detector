from src.config import EAR_THRESHOLD


class DrowsinessDetector:


    def __init__(self):

        self.score = 0


    def update(self, ear):


        if ear < EAR_THRESHOLD:

            self.score += 2


        else:

            self.score -= 1



        if self.score < 0:

            self.score = 0



        if self.score > 100:

            self.score = 100



        return self.score > 50



    def get_score(self):

        return self.score