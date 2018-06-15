from enum import Enum

class Days(Enum):
    Friday = 1
    Saturday = 2
    Sunday = 3
    Monday = 4
    Tuesday = 5
    Wednessday = 6
    Thursday = 7
    
days_mapping = {
        Days.Friday : "Today is friday",
        Days.Saturday : "Today is saturday",
        Days.Sunday : "Today is sunday",
        Days.Monday : "Today is monday",
        Days.Tuesday : "Today is tuesday",
        Days.Wednessday : "Today is wednessday",
        Days.Thursday : "Today is thursday"
    }
    
if __name__ == '__main__':
    day_name, day_value = Days.Monday.name, Days.Monday.value # get enum name, value
    print(day_name + ' : ' + str(day_value))
    
    print('Yesterday was : ' + Days(6).name)
    
    # get enum items from dictionary
    for k, v in days_mapping.items():
        print(str(k.value) + '. '+  v)
    
    