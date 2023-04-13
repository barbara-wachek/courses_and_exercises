
class Category:
    
    def __init__(self, category):
        self.category = category
        self.ledger = []
        self.total = 0
        
    def deposit(self, amount, description=""): 
        
        new_record = {"amount": float(amount), "description": description} 
        self.ledger.append(new_record)
        self.total = self.total + amount

        
    def withdraw(self, amount, description=""):
        self.amount = amount
        self.description = description
        
        if self.total > self.amount:
            new_record= {"amount": -abs(amount), "description":description} 
            self.ledger.append(new_record)
            self.total = self.total - self.amount
            return True
        else:
            return False
    
    
    def get_balance(self):
        return self.total
        
    def transfer(self, amount, another_category):
        if self.total > amount: 
            self.ledger.append({'amount': -abs(amount), 'description': f"Transfer to {another_category.category}"})
            self.total = self.total - amount
            
            another_category.ledger.append({'amount': float(amount), 'description': f"Transfer from {self.category}"})
            another_category.total = another_category.total + amount
            
            return True
        
        else:
            return False

    def check_funds(self, amount):
        if self.total >= amount: 
            return True
        else:
            return False
        
    def __str__(self): 
        length_of_category_name = len(self.category)
        start_index_of_category_name = (30 - length_of_category_name)/2 - 1
        number_of_stars = int((30 - length_of_category_name)/2) * "*"
        
        all_output = ''
        
        for x in self.ledger:
            for k, v in x.items():
                if k == 'amount':
                    amount = "{:.2f}".format(v)
                if k == 'description':
                    if v != '':
                        description = v[:23]
                    else:
                        description = ' '
                    
            space = (30 - (len(description) + len(str(amount)))) * ' '
                
            ledger_output = f'{description}{space}{amount}'
            all_output = f'{all_output}\n{ledger_output}'
                
      
        return f'{number_of_stars}{self.category}{number_of_stars}{all_output}\nTotal: {self.total}'
        


#categories = [food, entertainment, business]
def create_spend_chart(categories):
    
    list_of_expenses_for_category =  []
    list_of_percentage_for_category = []
    sum_of_all_expenses = 0 
    category_names = []
    
    for x in categories:
        
        category_name = x.category
        ledger = x.ledger
        expenses = 0
        category_names.append(category_name)
        
        for y in x.ledger:
            for k,v in y.items():
                if isinstance(v, float) and v < 0:
                    expenses = expenses + abs(v)
                    
        list_of_expenses_for_category.append({category_name:expenses})
   
        
    for x in list_of_expenses_for_category:
        for k, v in x.items():
            sum_of_all_expenses = sum_of_all_expenses + v
            
   
        
    for x in list_of_expenses_for_category:
        for k, v in x.items(): 
            percentage_for_category = int((v/sum_of_all_expenses)*100)
            
            list_of_percentage_for_category.append({k:percentage_for_category})
              
    
    for x in list_of_percentage_for_category:        
        for k,v in x.items():
           # v = 10
            new_value = (v//10)*10
            x[k] = new_value


    # number_of_o_in_one_row = len(categories)
    # if number_of_o_in_one_row == 4: 
    #     a = 'o'
    #     b = 'o'
    #     c = 'o'
    #     d = 'o'
    # if number_of_o_in_one_row == 3: 
    #     a = 'o'
    #     b = 'o'
    #     c = 'o'
    #     d = ''
    # if number_of_o_in_one_row == 2:    
    #     a = 'o'
    #     b = 'o'
    #     c = ''
    #     d = ''
    
    title = f'Percentage spent by category\n'   
    first_row = f'100| {a} {b} {c} {d}|\n'

    
    category_names = [business.category, food.category, entertainment.category]
    thirteen_row = f'{category_names[0][0]} {category_names[1][0]} {category_names[2][0]} '    
     
    number_of_o_for_all_categories = []
    for x in list_of_percentage_for_category:
        for k,v in x.items():
             number_of_o_for_all_categories.append({k:(v+10)/10})
                
    
     
        
        
    #return list_of_percentage_for_category 
    return f'Percentage spent by category\n100|\n 90|\n 80|\n 70|\n 60|\n 50|\n 40|\n 30|\n 20|\n 10|\n  0|\n    ----------'
 


            f'''Percentage spent by category\n100 {a}{b}{c}{d}|\n
            90|\n 80|\n 70|\n 60|\n 50|\n 40|\n 30|\n 20|\n 10|\n  0|\n    ----------'''


#%%TEST
        food = Category('Food')
        entertainment = Category('Entertainment')
        business = Category('Business')
        
        food.deposit(900, "deposit")
        entertainment.deposit(900, "deposit")
        business.deposit(900, "deposit")
        
        food.withdraw(105.55)
        entertainment.withdraw(33.40)
        business.withdraw(10.99)
        
        
        food.ledger
        business.ledger
        entertainment.ledger
        
        
        actual = create_spend_chart([business, food, entertainment])
        
        
        expected = "Percentage spent by category\n100|          \n 90|          \n 80|          \n 70|    o     \n 60|    o     \n 50|    o     \n 40|    o     \n 30|    o     \n 20|    o  o  \n 10|    o  o  \n  0| o  o  o  \n    ----------\n     B  F  E  \n     u  o  n  \n     s  o  t  \n     i  d  e  \n     n     r  \n     e     t  \n     s     a  \n     s     i  \n           n  \n           m  \n           e  \n           n  \n           t  "
        
        
        self.assertEqual(actual, expected, 'Expected different chart representation. Check that all spacing is exact.')

   
create_spend_chart([food, clothing, auto])



    
    # for x in categories: 
    #     name_of_category = x.category
    #     #expenses = x.ledger[amount]
    #     total_expenses = total_expenses + expenses
        
    # for y in categories:
    #     percentage = 
        
        
    # return f'Percentage spent by category\n100 |'





print_output = f'Percentage spent by category\n100|\n 90|\n 80|\n 70|\n 60|\n 50|\n 40|\n 30|\n 20|\n 10|\n  0|\n    ----------'
print(print_output)



#%%Main

food = Category('Food')
food.category
food.deposit(3000, 'initial deposit')
food.withdraw(5, 'Banana')
food.withdraw(15, 'Bread')
food.withdraw(100, 'Restaurant (soup, dinner, ice creams, coffees')
food.get_balance()
food.ledger
food.check_funds(200)
print(food)



clothing = Category('Clothing')
clothing.deposit(3000, 'initial deposit')
clothing.withdraw(5, 'Shoes')
clothing.withdraw(15, 'Coat')
clothing.get_balance()
clothing.ledger
print(clothing)

food.transfer(50, clothing)
food.ledger

clothing.check_funds(200)

auto = Category('Auto')
auto.deposit(1000, 'initial deposit')
auto.withdraw(300, 'gasoline')
auto.get_balance()
auto.ledger
print(auto)



print(create_spend_chart([food, clothing, auto]))





# entertainment = Category('Entertainment')
# entertainment.deposit(500)

# entertainment.withdraw(25, 'Cinema')
# entertainment.withdraw(100, 'Ski')

# entertainment.ledger

# categories = [food, clothing]


# clothing = Category('Clothing')



    
    
    
    
#%% main (z zadania)
    
food = budget.Category("Food")
food.deposit(1000, "initial deposit")
food.withdraw(10.15, "groceries")
food.withdraw(15.89, "restaurant and more food for dessert")
print(food.get_balance())
clothing = budget.Category("Clothing")

food.transfer(50, clothing)
clothing.withdraw(25.55)
clothing.withdraw(100)
auto = budget.Category("Auto")
auto.deposit(1000, "initial deposit")
auto.withdraw(15)

print(food)
print(clothing)

print(create_spend_chart([food, clothing, auto]))

# Run unit tests automatically
main(module='test_module', exit=False)