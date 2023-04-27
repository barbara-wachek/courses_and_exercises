#%%Class

class Rectangle():
    
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def set_width(self, width):
        self.width  = width
        
    def set_height(self, height):
        self.height = height
        
    def get_area(self):
        return self.width * self.height
          
    def get_perimeter(self):
        return (2*self.width) + (2*self.height)
    
    def get_diagonal(self): 
        return (self.width ** 2 + self.height ** 2) ** .5

    def get_picture(self): 
        
        if self.width > 50 or self.height > 50:
            return "Too big for picture."
        
        number_of_asterisks_in_one_line = self.width * '*'
       
        return ((f'{number_of_asterisks_in_one_line}'+'\n')*self.height)

    def get_amount_inside(self, another_width, another_height): 
        
        self.another_width = another_width
        self.another_height = another_height
        
        w = self.width//another_width
        h = self.height//another_height
        
        return h*w
    
    
    def __str__(self):
        return f'Rectangle(width={self.width}, height={self.height})'    
    
    
    
class Square(Rectangle):
    
    def __init__(self, side):
        self.width = side
        self.height = side
        
    def set_side(self, side):  
        self.height = side
        self.width = side

    def set_width(self, side):
        self.width = side
        self.height = side
        
    def set_height(self, side):
        self.width = side
        self.height = side
        
    def __str__(self):
        return f'Square(side={self.width})'
    
    
    
#%% Main

        
test = Rectangle(width=15, height=100)  
test.width      
test.set_height(5)
test.height

test.get_area()


test.get_perimeter()

test.get_diagonal()

test.get_picture()

test.get_amount_inside(50,5)



rect = Rectangle(10, 5)
print(rect.get_area())
rect.set_height(3)
print(rect.get_perimeter())
print(rect)
print(rect.get_picture())

sq = Square(9)
print(sq.get_area())
sq.set_side(4)
sq.set_side(2)
print(sq.get_diagonal())
print(sq)
print(sq.get_picture())

rect.set_height(8)
rect.set_width(16)
print(rect.get_amount_inside(sq))



#%% Testy niezaliczone



def test_get_amount_inside_none(self):
        rect2 = shape_calculator.Rectangle(2, 3)
        actual = rect2.get_amount_inside(self.rect)
        expected = 0
        self.assertEqual(actual, expected, 'Expected `get_amount_inside` to return 0.')

       
def test_get_amount_inside_two_rectangles(self):
       rect2 = shape_calculator.Rectangle(4, 8)
       actual = rect2.get_amount_inside(self.rect)
       expected = 1
       self.assertEqual(actual, expected, 'Expected `get_amount_inside` to return 1.')









