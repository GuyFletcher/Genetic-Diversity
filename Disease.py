import random

class Disease:
    '''
    Class will contain info on disease.
    Variables include:
    Name: String
    Gene Linked: Boolean
    Lethality: Float (between 0.0 and 1.0) //essentially a percentage chance if individual dies before mating
    Mating effect: Float (between 0.0 and 1.0) //how much it lowers mating chance, which is defaulted to 100%
    '''
    name = "N/A"
    gene_linked = False
    lethality = 0.0
    effect_on_mating = 0.0   