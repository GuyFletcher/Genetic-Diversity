from ete3 import Tree
import string
import random
import json
from Chromosome import Chromosome


'''
To generate random names = ''.join(random.choices(string.ascii_uppercase, k=5)) 

#t = Tree("(A:1,(B:1,(E:1,D:1):0.5):0.5);" )
#print (t)
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
    
    def __init__(self, name):
        self.name = name
        self.chromosomes = [None] * 40  #As this model is based loosely on mice this will always be 40
        self.children = [None]
        self.parents = [None, None]
   
    
    
def mate(person1, person2):    
    if person1.chromosomes[39].is_y == True and person2.chromosomes[19].is_y == False:
        print("Mating occurred")
        for x in range (0, 40, 2):
            #Parent 1
            if random.randint(0,1) == 0:
                child.chromosomes[x] = person1.chromosomes[x]
            else:
                child.chromosomes[x] = person1.chromosomes[x+1]
            #Parent 2
            if random.randint(0,1) == 0:
                child.chromosomes[x+1] = person2.chromosomes[x]
            else:
                child.chromosomes[x+1] = person2.chromosomes[x+1]
                
        child.name = "Child"
        
        if person1.children[0] == None:
            person1.children[0] = child
        else:
            person1.children.append(child)
        if person2.children[0] == None:
            person2.children[0] = child
        else:
            person2.children.append(child)
        child.parents[0] = person1
        child.parents[1] = person2
    else:
        print("Both males, no mating occurred")
        return None
    
    return child

def initialize(individual, sex):
    
    for x in range (0,40):
        individual.chromosomes[x] = Chromosome(10)
    
    if sex == 0:
        individual.chromosomes[39].is_y = True
    else:
        pass    

def compare(individual_one, individual_two):
    similarity = 100.0
    for x in range(0,40):
        gene_compare_length = 0
        if len(individual_one.chromosomes[x].genes) <= len(individual_two.chromosomes[x].genes):
            gene_compare_length = len(individual_one.chromosomes[x].genes) 
        else:
            gene_compare_length = len(individual_two.chromosomes[x].genes)
            
        for y in range(0,gene_compare_length):  #TODO: change similarity based on extra genes
            if individual_one.chromosomes[x].genes[y] == individual_two.chromosomes[x].genes[y]:
                pass
            else:
                similarity -= 1
    
    print("Similarity between ", individual_one.name, " and ", individual_two.name, " is ", similarity)

parent1 = Individual("Parent 1")
parent2 = Individual("Parent 2")
child = Individual("Child")   

initialize(parent1, 0)    
initialize(parent2, 1)

#print(parent1.name, parent1.chromosomes[0].genes)
#print(parent2.name, parent2.chromosomes[0].genes)

child = mate(parent1, parent2)

compare(parent1, parent2)
compare(parent2, child)

new_dict = {"id": "0", "label": parent1.name, "level": 0}

str1 = "data = '[" + json.dumps(new_dict,  ensure_ascii=False) + "]'"
print (str)

#with open('data.json', 'w') as outfile:
#    outfile.write(str1)
    
print(parent1.children[0])
    
#with open('genes.txt', 'w') as outfile:
#    for x in range(0,len(parent1.chromosomes[0].genes)):
#        outfile.write(str(parent1.chromosomes[x].genes))
#        outfile.write("\n")
    
    
def make_file(individual_one, individual_two):
    first = {"id": "0", "label": individual_one.name, "level": 0}
    second = {"id": "1", "label": individual_two.name, "level": 0}
    third = {"id": "0.1", "label": individual_two.children[0].name, "level": 1}
    str1 = "data = '[" + json.dumps(first,  ensure_ascii=False) + "]'"
    str2 = "data1 = '[" + json.dumps(second,  ensure_ascii=False) + "]'"
    str3 = "data2 = '[" + json.dumps(third,  ensure_ascii=False) + "]'"
    with open('data.json', 'w') as outfile:
        outfile.write(str1 + "\n")
        outfile.write(str2 + "\n")
        outfile.write(str3 + "\n")
    
make_file(parent1, parent2)
#json.dumps(new_dict,  ensure_ascii=False)
    





