from flask import Flask, render_template, request
from Individual import Individual
import string
import random
import json
from Chromosome import Chromosome
from Disease import Disease
from copy import copy
import pytest
import os
app = Flask(__name__)

dirname = os.path.dirname(__file__)
nodeName = os.path.join(dirname, 'static','nodes.js')
connectionsName = os.path.join(dirname, 'static','connections.js')
geneFile = os.path.join(dirname, 'static','geneFile.js')

def select_breed(people, num_gene, gene_length):
    disease_count = 0
    counter = {}
    for i in range(0,len(people)):
        for x in range(0,40):
            for y in range(0, num_gene):
                for z in range(0,gene_length):
                    if isinstance(people[i].chromosomes[x].genes[y][0], Disease):
                        disease_count += 1
        
        counter[people[i]] = disease_count
        disease_count = 0
        
    sorted_people = sorted(counter, key = counter.get, reverse = False)
    return sorted_people
    
def test_select_breed():
    num_gene = 2
    gene_length = 2
    person_1 = Individual()
    person_1.initialize(0, num_gene, gene_length)
    people = []
    people.append(person_1)
    person_2 = Individual()
    person_2.initialize(0, num_gene, gene_length)
    for i in range(0,40):
        person_2.chromosomes[i].genes[0] = (Disease, person_2.chromosomes[i].genes[0])
        
    people.append(person_2)
    test = select_breed(people, num_gene, gene_length)
    assert person_2 == test[1]

def tally(trait_list):
    counter = {}
    
    for trait in trait_list:
        if trait in counter:
            counter[trait] += 1
    else:
        counter[trait] = 1
        
    popular_words = sorted(counter, key = counter.get, reverse = True)
    
    return popular_words[:1][0]

def tally_traits(individual, num_gene, gene_length):
    hair_trait = []
    eye_trait = []
    skin_trait = []
    
    for x in range(0,40):
        for y in range(0,num_gene):
            for z in range(0,gene_length):
                if isinstance(individual.chromosomes[x].genes[y][0], str):
                    if individual.chromosomes[x].genes[y][0] in ["Hair: None", "Hair: Brown", "Hair: White", "Hair: Black", "Hair: Blond"]:
                        hair_trait.append(individual.chromosomes[x].genes[y][0])
                    if individual.chromosomes[x].genes[y][0] in ["Eye: Blue", "Eye: Red", "Eye: Green", "Eye: Hazel", "Eye: Yellow"]:
                        eye_trait.append(individual.chromosomes[x].genes[y][0])
                    if individual.chromosomes[x].genes[y][0] in ["Skin: White", "Skin: Black"]:
                        skin_trait.append(individual.chromosomes[x].genes[y][0])
    
    return [tally(hair_trait), tally(eye_trait), tally(skin_trait)]

def test_tally_traits():
    individual = Individual()
    num_gene = 2
    gene_length = 2
    individual.initialize(0, num_gene, gene_length)
    bob = tally_traits(individual, 2, 2)
    if len(bob) != 3:
        pytest.fail("Returned list not long enough")
    assert bob[0] in ["Hair: None", "Hair: Brown", "Hair: White", "Hair: Black", "Hair: Blond"]
    assert bob[1] in ["Eye: Blue", "Eye: Red", "Eye: Green", "Eye: Hazel", "Eye: Yellow"]
    assert bob[2] in ["Skin: White", "Skin: Black"]

        
def mutate(individual, mutation_chance, num_gene, gene_length):
    for x in range(0,40):            
        for y in range(0, num_gene):
            for z in range(0,gene_length):
                if x < 39: 
                    if random.randint(0, 10000) < mutation_chance/100:
                        individual.chromosomes[x].genes[y][1][z] = individual.chromosomes[x].gene_name_generator()
                        if random.randint(0, 10000) > 9999:
                            new_tuple = (Disease(), individual.chromosomes[x].genes[y][1])
                            individual.chromosomes[x].genes[y] = new_tuple
                            print("Disease by Mutation")
                        
                        
def check_disease(individual, num_gene, gene_length, check):
    disease = False
    
    for x in range(0,40):            
        for y in range(0, num_gene):
            for z in range(0,gene_length):
                if x < 39: 
                    if isinstance(individual.chromosomes[x].genes[y][0], Disease):
                        disease = True
                        if not check:
                            rand_disease = random.randint(0,10000)
                            if individual.chromosomes[x].genes[y][0].lethality > rand_disease:
                                print("Lethal", rand_disease)
                                individual.has_mated = True
                                individual.name += "\nLethal"
                                return disease
                            
                            rand_disease = random.randint(0,10000)
                            if individual.chromosomes[x].genes[y][0].effect_on_mating > rand_disease:
                                print("Infertile", rand_disease)
                                individual.has_mated = True
                                individual.name += "\nInfertile"
                                return disease
                        
    return disease
                        
def write_gene_to_file(person, gene_length):
    string_of_genes = ""
    string_of_genes += "Progenitor similarity: " + str(person.prog_sim) + "\nParent Similarity: " + str(person.parent_sim)
    traits = tally_traits(person, len(person.chromosomes[0].genes), gene_length)
    string_of_genes += "\n" + traits[0] + "\n" + traits[1] + "\n" + traits[2] + "\n"
    with open(geneFile, 'a') as outfile:
        for y in range(0,40):
            string_of_genes += "\nChromosome " + str(y+1) + "\n"
            for i in range(0, len(person.chromosomes[y].genes)):
                string_of_genes += str(i+1) + " "
                for x in range(0, gene_length):
                    string_of_genes += str(person.chromosomes[y].genes[i][1][x])
                if isinstance(person.chromosomes[y].genes[i][0], Disease):
                    string_of_genes += " " + person.chromosomes[y].genes[i][0].name + " Lethality: " + str(person.chromosomes[y].genes[i][0].lethality) + " Mating Effect: " + str(person.chromosomes[y].genes[i][0].effect_on_mating)
                else: 
                    string_of_genes += " " + person.chromosomes[y].genes[i][0]
                    
                string_of_genes += "\n"
                
            
        outfile.write("{ id: " + str(person.id) + ', genes: `' + string_of_genes + '`}, ')
    
    
def main(num_genes, gene_length, generations, num_pop, selective, mutation_chance):
    def mate(person1, person2):    
        child = Individual()
        
        #enforce person1 as male
        if person1.chromosomes[39].is_y != True:
            inter = person1
            person1 = person2
            person2 = inter      
        
        if person1.chromosomes[39].is_y == True and person2.chromosomes[39].is_y == False:
            if random.randint(0,1) == 0:
                for x in range (0, 40, 2):
                    child.chromosomes[x] = copy(person1.chromosomes[x])
                    child.chromosomes[x+1] = copy(person2.chromosomes[x+1])
            else:
                for x in range (0, 40, 2):
                    child.chromosomes[x+1] = copy(person1.chromosomes[x+1])
                    child.chromosomes[x] = copy(person2.chromosomes[x]) 
                    
            
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
            mutate(child, mutation_chance, num_genes, gene_length)
            #----Progenitor info-----
            if child.parents[0].progenitor[0] == None:
                child.progenitor[0] = copy(person1)
                child.progenitor[1] = copy(person2)
                sim = 0.0
                sim = compare(child, person1)
                sim += compare(child, person2)
                child.prog_sim = (sim/2)
                child.parent_sim = (sim/2)
            else:
                child.progenitor = person1.progenitor + person2.progenitor
                #print("Progenitors: ",len(child.progenitor))
                child.progenitor = list(set(child.progenitor))
                #print("Progenitors: ",len(child.progenitor))
                sim = 0.0
                for i in range(0,len(child.progenitor)):
                    sim += compare(child, child.progenitor[i])
                
                child.prog_sim = (sim/len(child.progenitor))
                sim = compare(child, person1)
                sim += compare(child, person2)
                child.parent_sim = (sim/2)
            
            #print("Mating occurred")
        else:
            print("Error: Not Male + Female")
            print(person1.chromosomes[39].is_y, person2.chromosomes[39].is_y)
            return None

        return child   

    def compare(individual_one, individual_two):    
        similarity = 0.0
        gene_compare_length = len(individual_one.chromosomes[0].genes)
        for x in range(0,40):            
            for y in range(0,gene_compare_length):
                for z in range(0,gene_length):
                    if individual_one.chromosomes[x].genes[y][1][z] == individual_two.chromosomes[x].genes[y][1][z]:
                        similarity += 1
                            
                            
        similarity = (similarity/(gene_compare_length*gene_length*40))*100
        
        #print("Similarity between ", individual_one.name, " and ", individual_two.name, " is ", similarity, "%")
        return similarity

    def make_file(males, females, id, level):
        info = []
        connect = []
        print("Made file")
        for x in range(0, num_pop):
            if x > len(males)-1:
                pass
            else: 
                males[x].id = id
                info.append({"id": str(id), "label": males[x].name, "level": level, "sim": males[x].prog_sim, "disease": str(check_disease(males[x], num_genes, gene_length, True))})
                #-----make genes file-----
                write_gene_to_file(males[x], gene_length)
                
                if males[x].parents[0] == None:
                    pass
                else:
                    connect.append({"from": str(males[x].parents[0].id), "to": str(id)})
                    connect.append({"from": str(males[x].parents[1].id), "to": str(id)})
                id += 1
            if x > len(females)-1:
                pass
            else:
                females[x].id = id
                info.append({"id": str(id), "label": females[x].name, "level": level, "sim": females[x].prog_sim, "disease": str(check_disease(females[x], num_genes, gene_length, True))})
                write_gene_to_file(females[x], gene_length)
                if females[x].parents[0] == None:
                    pass
                else:
                    connect.append({"from": str(females[x].parents[0].id), "to": str(id)})
                    connect.append({"from": str(females[x].parents[1].id), "to": str(id)})
                id += 1
        
        info_to_file = ",".join(map(str, info))
        connections_to_file = ",".join(map(str, connect))
        
        if len(info) != 0:
            with open(nodeName, 'a') as outfile:
                outfile.write(info_to_file + ", \n")
         
        if len(connections_to_file) != 0:
            with open(connectionsName, 'a') as outfile:
                outfile.write(connections_to_file + ", \n")
    
    with open(nodeName, 'w+') as outfile:
        outfile.write("nodeArray = [")
    with open(connectionsName, 'w+') as outfile:
        outfile.write("connections = [")
        
    with open(geneFile, 'w+') as outfile:
        outfile.write("genes = [")
    males = []
    females = []
    children = []
    id = 0
    level = 0
    
    for i in range(0, int(num_pop/2)):
        male_person = Individual()
        male_person.initialize(0, num_genes, gene_length)
        male_person.name = "Male Gen 0"
        check_disease(male_person, num_genes, gene_length, False)
        males.append(male_person)
        female_person = Individual()
        female_person.initialize(1, num_genes, gene_length)
        female_person.name = "Female Gen 0"
        check_disease(female_person, num_genes, gene_length, False)
        females.append(female_person)

    for x in range(0, generations):
        print("Gen ", x)
        
        make_file(males, females, id, level)
        id += num_pop
        level += 1
        
        random.shuffle(males)
        random.shuffle(females)
        
        if selective:
            print("Selective Breeding")
            males = select_breed(males, num_genes, gene_length)
            females = select_breed(females, num_genes, gene_length)
            
        if x != generations-1:
            if len(males) <= len(females):
                num_children = len(males)
            else:
                num_children = len(females)
                
            for i in range(0, num_children):
                if males[i].has_mated == True or females[i].has_mated:
                    pass  
                else:
                    child = mate(males[i], females[i])
                    children.append(child)
                    child2 = mate(males[i], females[i])
                    children.append(child2)
                    males[i].has_mated = True
                    females[i].has_mated = True
                
            del males[:]
            del females[:]
            for x in range(0, len(children)):
                if children[x].chromosomes[39].is_y == True:
                    children[x].name = "Male Gen " + str(level)
                    check_disease(children[x], num_genes, gene_length, False)
                    males.append(children[x])
                else:
                    children[x].name = "Female Gen " + str(level)
                    check_disease(children[x], num_genes, gene_length, False)
                    females.append(children[x])
                    
            print("Length of Males", len(males))
            print("Length of Females", len(females))
            del children[:]
            
        
    with open(nodeName, 'a') as outfile:
        outfile.write("]")

    with open(connectionsName, 'a') as outfile:
        outfile.write("]")
        
    with open(geneFile, 'a') as outfile:
        outfile.write("]")
    
    
@app.route('/')
def run_web():
    return render_template('form.html')

@app.route('/result',methods = ['POST', 'GET'])
def result():
    if request.method == 'POST':
        num_genes = int(request.form['Genes'])
        gene_length = int(request.form['GLength'])
        mutation = int(request.form['Mutate'])
        #Mutation of 300 = 3% chance per nucleotide, which is very high.
        if mutation > 300:
            mutation = 300
        generations = int(request.form['Generations'])
        if generations > 10:
            generations = 10
        population = int(request.form['Population'])
        #Pop values above 50 create problems with display
        if population > 50:
            population = 50
        selective = False
        if request.form.get('selective'):
            print("Selective")
            selective = True
        main(num_genes, gene_length, generations, population, selective, mutation)
        return render_template('result.html')
        
@app.after_request
def add_header(r):
    r.headers["Pragma"] = "no-cache"
    r.headers["Expires"] = "0"
    r.headers['Cache-Control'] = 'public, max-age=0, no-cache, no-store, must-revalidate'
    return r
        
if __name__ == '__main__':
    app.run(debug = True)
