
def add_time(start, duration, day=None):
  
    dictionary_of_days = {'Monday': 1,
                          'Tuesday': 2,
                          'Wednesday': 3,
                          'Thursday': 4,
                          'Friday': 5,
                          'Saturday': 6,
                          'Sunday': 7
                          }  
    
    start_hours = int(start[0:start.index(':')])
    start_minutes = int(start[(start.index(':')+1): start.index(' ')])
    duration_hours = int(duration[0:duration.index(':')])
    duration_minutes = int(duration[(duration.index(':')+1):])
    time_of_day = start[(start.index(' ')+1):]
    
    count_days = 0
    
    new_time_of_day = time_of_day
    
        
    #Tu się dzień nie zmienia:
    if (start_hours + duration_hours)/12 < 1:
        result_hours = start_hours + duration_hours
        result_minutes = start_minutes + duration_minutes
        if 'PM' in start and result_hours > 12: 
            result_hours =  result_hours - 12
            new_time_of_day = 'AM'
        if 'AM' in start and result_hours > 12: 
            result_hours =  result_hours - 12
            new_time_of_day = 'PM'
        
        if 'AM' in start and result_minutes > 60:
            new_time_of_day = 'PM'  
        if result_minutes > 60: 
            result_minutes = result_minutes - 60
            result_hours = result_hours + 1 
        
    # Tu się zmienia typ oznaczenia godziny PM/AM i ewentualnie dzień
    if (start_hours + duration_hours)/12 > 1:    
        add_days = duration_hours / 24        
        add_hours = duration_hours % 24

        add_days_str = str(add_days)
        count_days = int(add_days_str[:add_days_str.index('.')])
        count_days = count_days % 7 
        
        if count_days == 0 and time_of_day == 'PM' and (start_hours + duration_hours)/12 > 1 :
            count_days = count_days + 1
        

        result_hours = (start_hours + add_hours) - 12
        result_minutes = start_minutes + duration_minutes
        
        if result_minutes > 59 and add_hours > 0:
            result_hours = result_hours + 1
            result_minutes = result_minutes - 60
        
        if result_minutes > 60 and add_hours == 0: 
            add_days = add_days + 1
            count_days = count_days + 1
                    
        if (start_hours + add_hours) > 12 and count_days > 1:
            if time_of_day == 'PM':
                new_time_of_day = 'AM'
                count_days = count_days + 1
            if time_of_day == 'AM': 
                new_time_of_day = 'PM'
                
        if (start_hours + add_hours) > 12 and count_days <= 1:
            if time_of_day == 'PM':
               new_time_of_day = 'AM'
            if time_of_day == 'AM': 
               new_time_of_day = 'PM'
                
        if add_hours == 0 and count_days > 0 and result_minutes < 60:
            result_hours = start_hours 
            
        if add_hours == 0 and result_minutes > 60 :        
            result_hours = start_hours + 1
            result_minutes = result_minutes - 60
            if start_hours == 11 or start_hours == 23:
                if time_of_day == 'PM':
                    new_time_of_day = 'AM'
                if time_of_day == 'AM': 
                    new_time_of_day = 'PM'
                
        
            
    if len(str(result_minutes)) < 2:
        result_minutes = f'0{str(result_minutes)}'
    
    
    if day != None:
        day = day.title()
            
        if (dictionary_of_days[day] + count_days) <= 7:
            actual_day = [k for k,v in dictionary_of_days.items() if v == (dictionary_of_days[day] + count_days)]
        if (dictionary_of_days[day] + count_days) > 7:
            actual_day = [k for k,v in dictionary_of_days.items() if v == -(7 - (dictionary_of_days[day] + count_days))]
        
        
        if count_days == 1:
            new_time = f'{result_hours}:{result_minutes} {new_time_of_day}, {" ".join(actual_day)} (next day)'
            
        if count_days == 0:
            new_time = f'{result_hours}:{result_minutes} {new_time_of_day}, {" ".join(actual_day)}'
            
        if count_days < 0 or count_days > 1:
            round_add_days = round(add_days)
            if round_add_days < add_days:
                round_add_days = round(add_days+1)   
            new_time = f'{result_hours}:{result_minutes} {new_time_of_day}, {" ".join(actual_day)} ({int(round_add_days)} days later)'

        

    if day == None and count_days > 0:
        if count_days >= 1 and add_days < 1: 
            new_time = f'{result_hours}:{result_minutes} {new_time_of_day} (next day)'
            
        if count_days >= 1 and add_days > 1:
            round_add_days = round(add_days)
            if round_add_days < add_days:
                round_add_days = round(add_days+1) 
            new_time = f'{result_hours}:{result_minutes} {new_time_of_day} ({int(round_add_days)} days later)'
            
        if count_days >= 1 and add_days == 1:
            new_time = f'{result_hours}:{result_minutes} {new_time_of_day} (next day)'
            
       
        if count_days == 0:
            round_add_days = round(add_days)
            if round_add_days < add_days:
                round_add_days = round(add_days+1) 
            new_time = f'{result_hours}:{result_minutes} {new_time_of_day} ({int(round_add_days)} days later)'
            
    if day == None and count_days == 0: 
        new_time = f'{result_hours}:{result_minutes} {new_time_of_day}'
               
    
    
    return new_time