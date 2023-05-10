import copy
import random
# Consider using the modules imported above.

class Hat:
    
    def __init__(self, **balls):
        self.balls = balls
        self.contents = []
        
        for key, value in self.balls.items():
            for x in range(value):
                self.contents.append(key)
       

    def draw(self, number):
        list_of_strings = []
        if number > len(self.contents):
            return self.contents
        else: 
            for x in range(number):
                list_of_strings.append(self.contents.pop(random.randrange(1, len(self.contents))))
                
        return list_of_strings     



def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    hat = copy.copy(hat) #w razie problemów spróbować z deepcopy
    list_of_balls = []
    
    
    # num_balls_drawn=5
    # num_experiments=2000
    # hat = Hat(black=6, red=4, green=3)
    # expected_balls={"red":2,"green":1}
    

    counter = 0
    control_number = 0   
    
    for x in range(num_experiments):
        
        test = random.choices(hat.contents, k=num_balls_drawn)
        test_dictionary = {}
        
        for element in test:
            if element not in test_dictionary.keys(): 
                test_dictionary[element] = 1
            else:
                test_dictionary[element] += 1
        
        
        for key, value in expected_balls.items():
            for k, v in test_dictionary.items():
                if key == k and value == v: 
                    control_number += 1
                    
        if control_number == len(expected_balls.keys()):   
            counter += 1 
                
        
        # if expected_balls in test_dictionary:
        #     counter = counter + 1
    
    probability = counter/num_experiments       
            
        # for element in list_of_balls: 
            
        #     #wyjmij 5 random balls ze zbioru
        #     #sprawdz czy wyjete kule sa expected_balls
        #         #Jesli tak - counter + 1
        #     list_of_balls.append(random.randrange(" ".join(hat.contents)))

    return probability






#%% main

hat1 = Hat(yellow=3, blue=2, green=6)
hat2 = Hat(red=5, orange=4)
hat3 = Hat(red=5, orange=4, black=1, blue=0, pink=2, striped=9)
#hat_error = Hat()

hat1.balls
hat1.contents

hat1.draw(5)
hat.draw(2)

hat = Hat(black=6, red=4, green=3)
probability = experiment(hat=hat,
                  expected_balls={"red":2,"green":1},
                  num_balls_drawn=5,
                  num_experiments=2000)



hat = Hat(black=6, red=4, green=3)
probability = experiment(hat=hat,
                  expected_balls={"red":2,"green":1},
                  num_balls_drawn=5,
                  num_experiments=2000)



hat = Hat(blue=4, red=2, green=6)

hat.draw(2)
probability = prob_calculator.experiment(
    hat=hat,
    expected_balls={"blue": 2,
                    "red": 1},
    num_balls_drawn=4,
    num_experiments=3000)
print("Probability:", probability)




