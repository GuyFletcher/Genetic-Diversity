from ete3 import Tree
import string
import random
import json
from Chromosome import Chromosome


'''
To generate random names = ''.join(random.choices(string.ascii_uppercase, k=5)) 
'''           

class Individual:
    '''
    Class contains info on individuals. 
    Will contain variables for:
    Chromosomes: List of Chromosome objects
    Identifier: String of generation and number
    
    Will contain functions for:
    Gene initialization
    '''
    
    def __init__(self):
        self.name = "Default"
        self.chromosomes = [None] * 40  #As this model is based loosely on mice this will always be 40
        self.children = [None]
        self.parents = [None, None]
        self.progenitor = [None, None]
        self.prog_sim = 0.0
        self.parent_sim = 0.0
        self.id = 0
        self.has_mated = False
        
    def initialize(self, sex, num_genes, gene_size):
        for x in range (0,40):
            self.chromosomes[x] = Chromosome(num_genes, gene_size)
        
        if sex == 0:
            self.chromosomes[39].is_y = True
        else:
            self.chromosomes[39].is_y = False




