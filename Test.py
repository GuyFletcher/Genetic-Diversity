from ete3 import Tree
import string
import random


'''
To generate random names = ''.join(random.choices(string.ascii_uppercase, k=5)) 

#t = Tree("(A:1,(B:1,(E:1,D:1):0.5):0.5);" )
#print (t)
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
    def __init__(self, entered_gene_size):
        self.name = "N/A"
        self.is_y = False
        self.genes = [(None, [])] * 10
        gene_size = entered_gene_size
            
        #instantiates the nucleobases of a gene and determines link with disease, if applicable.
        for y in range (0, len(self.genes)):
            acid_list = []
            for x in range(0, gene_size):
                acid_list.append(self.gene_name_generator())
            
            if random.randint(0,100) > 95:  #chance of gene linked disease set to less than 5%
                disease = Disease()
                disease.name = "Syndrome"
                disease.gene_linked = True
                self.genes[y] = (disease, acid_list)
            else:
                self.genes[y] = (None, acid_list)
    
    def gene_name_generator(self):
        n_acid = random.randint(0, 3) 
        if n_acid == 0:
            return "A"
        elif n_acid == 1:
            return "T"
        elif n_acid == 2:
            return "C"
        else:
            return "G"       
        


            

class Person:
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
    
    
    '''def initialize(self):
        
        for x in range (0,20):
            self.chromosomes[x] = Chromosome()
        
        if random.randint(0,1) == 0:
            self.chromosomes[19].is_y = True
        else:
            pass'''
        #print(person.chromosomes[0].genes)
   
    
    
def mate():    
    
    '''
    if person1.chromosomes[19].is_y == True and person2.chromosomes[19].is_y == False:
        print("Mating occurred")
        for x in range (0, 20):
            if random.randint(0,1) == 0:
                child.chromosomes[x] = person1.chromosomes[x]
            else:
                child.chromosomes[x] = person2.chromosomes[x]
        print(person1.name, person1.chromosomes[0].genes)
        print(person2.name, person2.chromosomes[0].genes)
        print("Child", child.chromosomes[0].genes)
    else:
        print("Both males, no mating occurred")
    '''

def initialize(person):
    
    for x in range (0,20):
        person.chromosomes[x] = Chromosome(10)
    
    if random.randint(0,1) == 0:
        person.chromosomes[19].is_y = True
    else:
        pass    

parent1 = Person("Parent 1")
parent2 = Person("Parent 2")
child = Person("Child")   

initialize(parent1)    
initialize(parent2)

print(parent1.name, parent1.chromosomes[0].genes)
print(parent2.name, parent2.chromosomes[0].genes)

mate()



