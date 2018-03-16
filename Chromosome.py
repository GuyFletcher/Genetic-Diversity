import random
from Disease import Disease

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
            
        #instantiates the nucleobases of a gene and determines link with disease, if applicable.
        for y in range (0, len(self.genes)):
            acid_list = []
            for x in range(0, gene_size):
                acid_list.append(self.gene_name_generator())
            
            if random.randint(0,100) > 98:  #chance of gene linked disease set to less than 5%
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
        