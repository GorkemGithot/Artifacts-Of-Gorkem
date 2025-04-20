import cv2
import numpy as np
import random
import matplotlib.pyplot as plt
import time

population_size=50
genome_length=8
mutation_rate=0.01
crosoverrate_=0.5
generations=200

image = cv2.imread('real_image.jpg', cv2.IMREAD_GRAYSCALE)
h,w=image.shape
centerX=w//2
centerY=h//4
t1L=image[0:centerY,0:centerX]
t1R=image[0:centerY,centerX:w]
t2L=image[centerY:2*centerY,0:centerX]
t2R=image[centerY:2*centerY,centerX:w]
t3L=image[2*centerY:3*centerY,0:centerX]
t3R=image[2*centerY:3*centerY,centerX:w]
t4L=image[3*centerY:h,0:centerX]
t4R=image[3*centerY:h,centerX:w]


real_values=[t1L,t1R,t2L,t2R,t3L,t3R,t4L,t4R]
np.array(real_values)

def random_genome(length):
    mylist=[]
    np.array(mylist)
    for a in real_values:
        mylist.append(a)
    random.shuffle(mylist)
    return mylist


def init_population(population,genome_length):
    mylist=list()
    for i in range(population):
        mylist.append(random_genome(genome_length))
    return mylist


def fitness(genome):
    fitnessVar=0
    for a in range(genome_length):
        if (np.array_equal(real_values[a],genome[a])):
            fitnessVar+=1 
    return fitnessVar

def select_parent(population,fitness_values):
    total_fitness=sum(fitness_values)
    random_picked_fitness=random.uniform(0,total_fitness)
    current=0
    for individual, fitness_value in zip(population,fitness_values):
        current+=fitness_value
        if current>random_picked_fitness:
            return individual

def crossover(parent1,parent2):
    if(random.random()< crosoverrate_):
        crossover_point=random.randint(1,len(parent1)-1)
        return parent1[:crossover_point]+parent2[crossover_point:],parent2[:crossover_point]+parent1[crossover_point:]
    else:
        return parent1,parent2

    
def mutate(genome):
    for i in range(genome_length):
        if(random.random()<mutation_rate):
            sampleViewFromRealJPG=random.sample(real_values,1)
            genome[i]=sampleViewFromRealJPG[0]
    return genome



def mainAlgorithm():
    population=init_population(population_size,genome_length)
    for generation in range(generations):
        fitness_values=list()
        for genome in population:
            fitness_values.append(fitness(genome))
        newPopulation=list()
        for a in range(population_size//2):
            parent1=select_parent(population,fitness_values)
            parent2=select_parent(population,fitness_values)
            offspring1,offspring2=crossover(parent1,parent2)
            newPopulation.extend([mutate(offspring1),mutate(offspring2)])
        population=newPopulation
        fitness_values=[fitness(genome) for genome in population]
        best_fitness=max(fitness_values)
        print(f"Generation {generation+1}: Best fitness ={best_fitness}")
        temp_max=0
        temp_index=0
        for i in range(len(fitness_values)):
            if(fitness_values[i]>=temp_max):
                temp_max=fitness_values[i]
                temp_index=i
        best_solution=population[temp_index]
        if(generation==generations-1):
            im_h1 = cv2.hconcat([best_solution[0],best_solution[1]]) 
            im_h2 = cv2.hconcat([best_solution[2],best_solution[3]]) 
            im_h3 = cv2.hconcat([best_solution[4],best_solution[5]]) 
            im_h4 = cv2.hconcat([best_solution[6],best_solution[7]]) 
            imfinal=cv2.vconcat([im_h1,im_h2,im_h3,im_h4])
            s=f"saved_generations/generation{generation+1}.jpg"
            cv2.imwrite(s, imfinal)
            cv2.imshow("real_image.jpg", image)
            cv2.imshow(s, image)
            cv2.waitKey(0)
        else:
            im_h1 = cv2.hconcat([best_solution[0],best_solution[1]]) 
            im_h2 = cv2.hconcat([best_solution[2],best_solution[3]]) 
            im_h3 = cv2.hconcat([best_solution[4],best_solution[5]]) 
            im_h4 = cv2.hconcat([best_solution[6],best_solution[7]]) 
            imfinal=cv2.vconcat([im_h1,im_h2,im_h3,im_h4])
            s=f"saved_generations/generation{generation+1}.jpg"
            cv2.imwrite(s, imfinal)

mainAlgorithm()

