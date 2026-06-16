# Match-case statement  = An alternative to using many "elif" statements
#                         Execute some code if a value matches a 'case'
#                         Benefits: cleaner and synatx is more readable

# def day_of_week(day):
#     match day:
#         case 1:#it  act as a elif 
#             return "it's Sunday"
#         case 2:
#             return "it's Monday"
#         case 3:
#             return "it's Tuesday"
#         case 4:
#             return "it's Wednesday"
#         case 5:
#             return "it's Thursday"
#         case 6:
#             return "it's Friday"
#         case 7:
#             return "it's Saturday"
#         case _:#it act as else statement
#             return "Not a valid day"
     
# print(day_of_week("pizza"))

def is_weekend(day):
    match day:
        case "saturday" | "sunday":
            return True
        case "monday"| "tuesday"|"wednesday" |"thursday" |"friday":
            return False
        case _:
            return False
        
print(is_weekend("monday"))