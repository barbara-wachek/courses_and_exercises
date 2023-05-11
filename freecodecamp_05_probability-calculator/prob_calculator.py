import copy
import random

class Hat:
    
    def __init__(self, **balls):
        self.balls = balls
        self.contents = []
        for key, value in self.balls.items():
            for x in range(value):
                self.contents.append(key)
        if balls == {}:
            raise TypeError ("__init__() missing 1 required positional argument")

    def draw(self, number):
        list_of_balls = []
        self.number = number
        
        if number > len(self.contents):
            return self.contents
        else: 
            for x in range(number):
                random_ball = random.choice(self.contents)
                self.contents.remove(random_ball)
                list_of_balls.append(random_ball)
                
        return list_of_balls   


def experiment(hat, expected_balls, num_balls_drawn, num_experiments): 
    counter = 0
    
    for x in range(num_experiments):
        new_hat = copy.deepcopy(hat) 
        dictionary_of_drawn_balls = {}
        control_number = 0  
        list_of_drawn_balls = new_hat.draw(num_balls_drawn)
    
        for element in list_of_drawn_balls:
            if element not in dictionary_of_drawn_balls.keys(): 
                dictionary_of_drawn_balls[element] = 1
            else:
                dictionary_of_drawn_balls[element] += 1
        
        for key, value in expected_balls.items():
            for k, v in dictionary_of_drawn_balls.items():
                if key == k and value <= v: 
                    control_number += 1
                    
        if control_number == len(expected_balls.keys()):   
            counter += 1 
                     
    probability = counter/num_experiments       
            
    return probability



















