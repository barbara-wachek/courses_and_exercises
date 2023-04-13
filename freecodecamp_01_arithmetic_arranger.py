
#%% def
def arithmetic_arranger(problems, is_result = False):  
    
    list_of_first_row = []
    list_of_second_row = []
    list_of_third_row = []
    list_of_forth_row = []
    
    try:
        if len(problems) > 5:
            raise ValueError
    except ValueError:
        return 'Error: Too many problems.' 
 

    for x in problems:
        first_number = x[0: x.index(' ')]
        second_number = x[x.index(' ')+3:]
        operator = x[x.index(' ') + 1]
        len_of_first_number = len(x[0: x.index(' ')])
        len_of_second_number = len(x[x.index(' ')+3:])
        
        try:
            if operator == '*':
                raise KeyError
            if operator == '/':
                raise KeyError
                
            if len(str(first_number)) > 4 or len(str(second_number)) > 4 :
                raise IndexError    
            
            if len_of_first_number > len_of_second_number:
                first_line_indentations = 2 * " "
                second_line_indentations = (len_of_first_number - len_of_second_number) * " "
                lines = (2+len_of_first_number)*'-'
                len_of_lines = len(lines)
                
              
                list_of_first_row.append(f'{first_line_indentations}{int(first_number)}\n')
                list_of_second_row.append(f'{operator}{second_line_indentations} {int(second_number)}\n')
                list_of_third_row.append(f'{lines}')
                
                if is_result == True:
                    if operator == '+':
                        result = int(first_number) + int(second_number)
                    elif operator == '-':
                        result = int(first_number) - int(second_number) 
                             
                    index_result = len_of_lines - len(str(result))
                    list_of_forth_row.append(index_result * ' ' + str(result)) 
                        
                     
            if len_of_first_number <= len_of_second_number: 
                first_line_indentations = (2 + (len_of_second_number - len_of_first_number)) * " "
                lines = (2+len_of_second_number)*'-'
                len_of_lines = len(lines)
                
                
                list_of_first_row.append(f'{first_line_indentations}{int(first_number)}\n')
                list_of_second_row.append(f'{operator} {int(second_number)}\n')
                list_of_third_row.append(f'{lines}')
                
                if is_result == True:
                    if operator == '+':
                        result = int(first_number) + int(second_number)
                    elif operator == '-':
                        result = int(first_number) - int(second_number)
   
                    index_result = len_of_lines - len(str(result)) 
                    list_of_forth_row.append(index_result * ' ' + str(result)) 
                
        except KeyError:
            return "Error: Operator must be '+' or '-'."
        except IndexError:
            return 'Error: Numbers cannot be more than four digits.'
        except ValueError:
            return 'Error: Numbers must only contain digits.'
    

        
        
    join_1_list = '    '.join(list_of_first_row).replace('\n', '')    
    join_2_list = '    '.join(list_of_second_row).replace('\n', '') 
    join_3_list = '    '.join(list_of_third_row)
    join_4_list = '    '.join(list_of_forth_row)
        
    if is_result == False:
        arranged_problems = f'{join_1_list}\n{join_2_list}\n{join_3_list}'
    else:
        arranged_problems = f'{join_1_list}\n{join_2_list}\n{join_3_list}\n{join_4_list}'
           
    return arranged_problems


#%% main

print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49", "0 + 1", "5 + 5"], True))
print(arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 / 49"], True))
print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "12302 + 5"], True))
print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + a"], True))
print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 5"]))










