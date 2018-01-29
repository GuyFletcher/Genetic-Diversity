from ete3 import Tree
import string
import random


'''
To generate random names = ''.join(random.choices(string.ascii_uppercase, k=5)) 
'''

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

class Chromosome:
    '''
    This class contains specific gene information. 
    Planned variables: 
    Name: String
    Nucleotide segment (ATCG): Char
    active/inactive: Boolean
    Disease link: Disease object
    '''
    name = "N/A"
    is_xy = False
    genes = [(None, [])] * 10
    
    def gene_name_generator():
        n_acid = random.randint(0, 3) 
        if n_acid == 0:
            return "A"
        elif n_acid == 1:
            return "T"
        elif n_acid == 2:
            return "C"
        else:
            return "G"       
        
    gene_size = 10
    
    #instantiates the nucleobases of a gene and determines link with disease, if applicable.
    for y in range (0, len(genes)):
        acid_list = []
        for x in range(0, gene_size):
            acid_list.append(gene_name_generator())
        
        if random.randint(0,100) > 95:  #chance of gene linked disease set to less than 5%
            disease = Disease()
            disease.name = "Syndrome"
            disease.gene_linked = True
            genes[y] = (disease, acid_list)
        else:
            genes[y] = (None, acid_list)
            

class Person(Chromosome):
    '''
    Class contains info on individuals. 
    Will contain variables for:
    Chromosomes: List of Chromosome objects
    Identifier: String of generation and number
    
    Will contain functions for:
    Gene initialization
    '''
    
    def __init__(self, name):
        self.name = name
        self.chromosomes = [None] * 20
    
    
    def initialize(self, person):
        
        for x in range (0,20):
            person.chromosomes[x] = Chromosome()
            
        person.chromosomes[18].is_xy = True
        person.chromosomes[19].is_xy = True
        print(person.chromosomes[0].genes)
   
    
    
def mate():
    person1 = Person("Parent 1")
    person2 = Person("Parent 2")
    child = Person("Child")
    
    person1.initialize(person1)
    person2.initialize(person2)
    
    for x in range (0, 20):
        if random.randint(0,1) == 0:
            child.chromosomes[x] = person1.chromosomes[x]
        else:
            child.chromosomes[x] = person2.chromosomes[x]
    
    print(person1.name, person1.chromosomes[0].genes)
    print(person2.name, person2.chromosomes[0].genes)
    print("Child", child.chromosomes[0].genes)
    #print (gene_list[0].name) 
    
mate()

#t = Tree("(A:1,(B:1,(E:1,D:1):0.5):0.5);" )
#print (t)



