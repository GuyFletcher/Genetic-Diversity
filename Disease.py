import random

class Disease:
    '''
    Class will contain info on disease.
    Variables include:
    Name: String
    Lethality: Float (between 0.0 and 1.0) //essentially a percentage chance if individual dies before mating
    Mating effect: Float (between 0.0 and 1.0) //how much it lowers mating chance, which is defaulted to 100%
    '''
    def __init__(self):
        self.name = "N/A"
        self.lethality = random.randint(0,50)
        self.effect_on_mating = random.randint(0,50)

        