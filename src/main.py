from random import randint


class Population():
    people = []
    def load_people(self):
        self.people = [[2,4,6,8], [4,5,8,12], [6,7,10,12], [14,2,45,33], [11,7,4,1]]

class Fitness():
    functions = []
    
    def add(self,a,b):
        return a+b
    
    def rest(self,a,b):
        return a-b
    
    def start(self):
        self.functions = [self.add,self.rest]
        
    def evaluation(self, people):
        for person in people:
            for fun in self.functions:
                a = fun(person[0],person[1])
                print(a)
            #print [fun(person[0],person[1]) for fun in self.functions]
        
class Run():
    
    def __init__(self, mutation_factor=0.7, crossover_ratio=0.4, iterations=10)
        self.mutation_factor = mutation_factor
        self.combination_ratio = combination_ratio
        self.iterations = iterations
    
    def get_new_index(people, taken_indexes):
        first_index = randint(0,len(people))
        while first_index in taken_indexes:
            first_index = randint(0,len(people))
        return first_index
    
    def get_indexes(people, current_index):
        taken_indexes = [current_index]
        for i in range(0,3):
            taken_indexes.append(self.get_new_index(people, taken_indexes))
        return taken_indexes[1:]
    
    
    def operate(people, current_index, indexes):
        new_person = []
        for idx, value in enumerate(people[current_index]):
            if random.uniform(0, 1) < self.crossover_ratio:
                tmp_value = people[indexes[0]][idx] + self.mutation_factor * (people[indexes[1]][idx] - people[indexes[2]][idx])
            else:
                tmp_value = value
            new_person.append(tmp_value)    
        return new_person
    
    
#    def mutate(new_person):
#        for elem in new_person:
#            elem = elem * self.mutation_factor   
#        return new_person
#    
#    
#    def complete(person, new_person):
#        candidate_person = []
#        for idx, value in enumerate(new_person):
#            elem = person[idx] + new_person[idx]
#        return candidate_person
    
    
    def run(self):
        people = Population()
        people.load_people()
        
        fit = Fitness()
        fit.start()
        
        for iteration in self.iterations:
            next_generation = []

            for current_index, person in enumerate(people):
                indexes = get_indexes(people, current_index)
                new_person = operate(people, current_index, indexes)
                next_generation.append(choose_best(person, new_person))
        
        
        
        fit.evaluation(people.people)
        
        #print('Hello World!')
        
run = Run()
run.run()