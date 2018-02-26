from flask import Flask, render_template, request
from Test import Individual
import string
import random
import json
from Chromosome import Chromosome
app = Flask(__name__)
    
    
def main(num_genes, generatons, num_pop, is_disease):
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
            child.name = person1.name + " + " + person2.name
        else:
            print("Error: Not Male + Female")
            print(person1.chromosomes[39].is_y, person2.chromosomes[39].is_y)
            return None

        return child   

    def compare(individual_one, individual_two):
        similarity = 0.0
        gene_length = 100
        gene_compare_length = len(individual_one.chromosomes[0].genes)
        for x in range(0,40):            
            for y in range(0,gene_compare_length):
                for z in range(0,gene_length):
                    if x < 39 and x%2: 
                        if individual_one.chromosomes[x].genes[y][1][z] == individual_two.chromosomes[x].genes[y][1][z]:
                            similarity += 1
                        elif individual_one.chromosomes[x].genes[y][1][z] == individual_two.chromosomes[x+1].genes[y][1][z]:
                            similarity +=1
                        else:
                            pass
                    else:
                        if individual_one.chromosomes[x].genes[y][1][z] == individual_two.chromosomes[x].genes[y][1][z]:
                            similarity += 1
                        else:
                            pass
        similarity = (similarity/(gene_compare_length*gene_length*40))*100
        
        print("Similarity between ", individual_one.name, " and ", individual_two.name, " is ", similarity, "%")

        
    males = []
    females = []
    children = []
    
    for i in range(0, int(num_pop/2)):
        male_person = Individual()
        male_person.initialize(0, num_genes, "Male " + str(i))
        males.append(male_person)
        female_person = Individual()
        female_person.initialize(1, num_genes, "Female " + str(i))
        females.append(female_person)
        
        
    for i in range(0, int(num_pop/2)):
        child = Individual()
        child = mate(males[i], females[i])
        children.append(child)
        print(child.name)
        
     

    #compare(parent1, parent2)
    #compare(parent1, child)
    #compare(parent2, child)

    new_dict = {"id": "0", "label": males[0].name, "level": 0}

    str1 = "data = '[" + json.dumps(new_dict,  ensure_ascii=False) + "]'"
    #print (str)

    #with open('data.json', 'w') as outfile:
    #    outfile.write(str1)
        
    #print(parent1.children[0])
        
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
        
    make_file(males[0], females[0])
    #json.dumps(new_dict,  ensure_ascii=False)
    
    
@app.route('/')
def student():
    return render_template('form.html')

@app.route('/result',methods = ['POST', 'GET'])
def result():
    if request.method == 'POST':
        num_genes = int(request.form['Genes'])
        # add length of genes here
        generations = int(request.form['Generations'])
        population = int(request.form['Population'])
        disease = request.form['Disease']
        print(result, generations, disease)
        main(num_genes, generations, population, disease)
        return render_template('result.html')
if __name__ == '__main__':
    app.run(debug = True)