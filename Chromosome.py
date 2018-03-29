import random
from Disease import Disease
import pytest

class Chromosome:
    '''
    This class contains specific gene information. 
    Planned variables: 
    Name: String
    Nucleotide segment (ATCG): Char
    active/inactive: Boolean
    Disease link: Disease object
    '''
    def __init__(self, num_genes, entered_gene_size):
        self.name = "N/A"
        self.is_y = False
        self.genes = [(None, [])] * num_genes
        gene_size = entered_gene_size
        self.traits = { 0:"Hair: None", 1:"Hair: Brown", 2:"Hair: White", 3:"Hair: Black", 4:"Hair: Blond",
        5:"Eye: Blue", 6:"Eye: Red", 7:"Eye: Green", 8:"Eye: Hazel", 9:"Eye: Yellow",
        10:"Skin: White", 11:"Skin: Black"}
            
        #instantiates the nucleobases of a gene and determines link with disease, if applicable.
        for y in range (0, len(self.genes)):
            acid_list = []
            for x in range(0, gene_size):
                acid_list.append(self.gene_name_generator())
            
            if random.randint(0,1000) > 998:  #chance of gene linked disease set to 1%
                disease = Disease()
                disease.name = "Syndrome"
                disease.gene_linked = True
                self.genes[y] = (disease, acid_list)
            else:
                self.genes[y] = (self.pheno_data(random.randint(0,11)), acid_list)
    
    
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

    def pheno_data(self, x):
        if x in self.traits:
            return self.traits[x]
        else:
            pytest.fail("Not a valid option: %s" %(x,))
        
        
def test_pheno_pass():
    c = Chromosome(2, 2)
    num = random.randint(0,11)
    h = c.pheno_data(num)
    assert h == c.traits[num]
        
def test_pheno_fail():
    c = Chromosome(2, 2)
    num = 0
    h = c.pheno_data(num)
    assert h == c.traits[1]