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

    










#%% main

hat1 = Hat(yellow=3, blue=2, green=6)
# hat2 = Hat(red=5, orange=4)
# hat3 = Hat(red=5, orange=4, black=1, blue=0, pink=2, striped=9)
#hat_error = Hat()

hat1.balls
hat1.contents

hat1.draw(5)


hat = Hat(black=6, red=4, green=3)
probability = experiment(hat=hat,
                  expected_balls={"red":2,"green":1},
                  num_balls_drawn=5,
                  num_experiments=2000)











