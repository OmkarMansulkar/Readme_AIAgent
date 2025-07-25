import random
from deap import base, creator, tools

creator.create("FitnessMin", base.Fitness,)
creator.create("Individual", list,fitness=creator.FitnessMin)

best = tools.selBest(pop,1)[0]
print("Best individual:",best)
print("Best fitness:   ",best.fitness)