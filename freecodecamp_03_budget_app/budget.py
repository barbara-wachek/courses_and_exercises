#%% Class
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
        

#%% Function
def create_spend_chart(categories):
    
    list_of_expenses_for_category =  []
    list_of_percentage_for_category = []
    list_of_rounded_percentages = []
    sum_of_all_expenses = 0 
    category_names = []
    
    for x in categories:
        category_name = x.category
        expenses = 0
        category_names.append(category_name)
        
        for y in x.ledger:
            for k,v in y.items():
                if (isinstance(v, float) or isinstance(v, int)) and v < 0:
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
            new_value = (v//10)*10
            list_of_rounded_percentages.append(new_value)
             
    #Chart
    title = f'Percentage spent by category\n'   
    chart = ""
    for value in reversed(range(0, 101, 10)):
        chart += str(value).rjust(3) + '|'
        for x in list_of_rounded_percentages:
            if x >= value:
                chart += " o "
            else:
                chart += "   "
            
        chart += " \n" 
           
    footer = "    " + "-" * ((3 * len(categories)) + 1) + "\n"
    max_length = max(map(lambda x: len(x), category_names))
    category_names_with_spaces = list(map(lambda name: name.ljust(max_length), category_names))

    for x in zip(*category_names_with_spaces):
        footer += "    " + "".join(map(lambda s: s.center(3), x)) + " \n"

    return (title + chart + footer).rstrip("\n")

    
    