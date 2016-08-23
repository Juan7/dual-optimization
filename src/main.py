from random import randint


class Population:
    people = []
    def load_people(self):
        self.people = [ [2,4], [4,5], [6,7], [14,2], [11,7]]

class Fitness:
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
        
class Run:
    mutation_factor = 0.7
    
    def get_indexes(people, current_index):
        first_index = randint(0,len(people))
        second_index = randint(0,len(people))
        while current_index == first_index:
            first_index = randint(0,len(people))
        while current_index == second_index:
            second_index = randint(0,len(people))
        return first_index, second_index
    
    
    def operate(people, current_index, first_index, second_index):
        new_person = []
        for idx, value in enumerate(people[current_index]):
            tmp_value = people[first_index][idx] - people[second_index][idx]
            new_person.append(tmp_value)    
        return new_person
    
    
    def mutate(new_person):
        for elem in new_person:
            elem = elem * self.mutation_factor   
        return new_person
    
    
    def complete(person, new_person):
        candidate_person = []
        for idx, value in enumerate(new_person):
            elem = person[idx] + new_person[idx]
        return candidate_person
    
    
    def run(self):
        people = Population()
        people.load_people()
        
        candidate = []
        
        for current_index, person in enumerate(people):
            first_index, second_index = get_indexes(people, current_index)
            new_person = operate(people, current_index, first_index, second_index)
            new_person = mutate(new_person)
            candidate_person = complete(person, new_person)
            candidate.append(candidate_person)
        
        
        
        fit = Fitness()
        fit.start()
        
        fit.evaluation(people.people)
        
        #print('Hello World!')
        
run = Run()
run.run()