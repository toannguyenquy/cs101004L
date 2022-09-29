########################################################################
##
## CS 101 Lab
## Program #Lab5
## Name: Toan Nguyen 
## Email:tqndvt@umsystem.edu or nguyenquytoan2002@gmail.com
##
## PROBLEM : Describe the problem
##
## ALGORITHM : 
##      1. Write out the algorithm
##
## ERROR HANDLING:
##      Any Special Error handling to be noted.  Wager not less than 0. etc
##
## OTHER COMMENTS:
##      Any special comments
##
########################################################################


# import statements

# functions
def get_school(card_num):       #Function for the first number in the Lirary Card to define which school the user is. 
    if card_num[5] == '1':      #The 6 elements is 1 so it will return
        return "School of Computing and Engineering SCE"
    elif card_num[5] == '2':    #The 6 elements is 2 so it will return
        return "School of Law"
    elif card_num[5] == '3':    #The 6 elements is 2 so it will return
        return "College of Arts and Sciences"
    else:                       #Otherwise  
        return "Invalid School"
    
def get_grade (card_num) :      #Function to determine what year of the user 
    if card_num[6] == '1':      #The 7 elements is 1 so it will return
        return "Freshman"   
    elif card_num[6] == '2':    #The 7elements is 2 so it will return
        return "Sophomore"
    elif card_num[6] == '3':    #The 7elements is 3 so it will return
        return "Junior"    
    elif card_num[6] == '4':    #The 7elements is 4 so it will return
        return "Senior"
    else:                       #Otherwise 
        return "Invalid Grade"
    
def character_value(character):     #Function to convert A-Z became(0-25)
    value = ord(character)          #set up value type number to get the aphabet in python
    if (value >= 48 and value<=57): 
        return value - 48
    elif (value >= 65 and value<=90):
        return value - 65

def get_check_digit (card_num):   # This function will add each elements that the user input together (will connect to the function above this one)
    count = 0
    for i in range(len(card_num)):
        value = character_value(card_num[i])
        count += value * (i+1)
    return count % 10             # Can it all devided by 10 (It wil correct)

def verify_check_digit(card_num):
    if len(card_num) != 10:         #Check is it the length of 10 (Have to quatify first (1)
        return False, "The length of the number given must be 10."
    for i in range(0,5):            #Check the first 5 elements of the user input and it have to quatify (2)
        if card_num[i] < 'A' or card_num[i] > 'Z':
            return False, 'The first 5 characters must be A-Z, the invalid character is at '+ str(i)+ ' is ' + card_num[i]
    for i in range(7,10):           #Check the last 3 elements of the user input and it have to quatify (3)
        if card_num[i] < '0' or card_num[i] > '9':
            return False, 'False, "The last 3 characters must be 0-9, the invalid character is at '+ str(i)+ ' is ' + card_num[i]
    if (card_num[5] != '1' and card_num[5] != '2' and card_num[5] != '3'): #Check the last 6 elements of the user input is it 1,2,3 and it have to quatify (4)
        return False, "The sixth character must be 1,2 or 3"
    if (card_num[6] != '1' and card_num[6] != '2' and card_num[6] != '3' and card_num[6] != '4'):  #Check the last 7 elements of the user input is it 1,2,3,4 and it have to quatify (5)
        return False, "The seventh character must be 1,2,3 or 4"
    
    compare1 = get_check_digit(card_num)    #set up the value for the next frunction to compare
    compare2 = int(card_num[9])             #set up the value for the next frunction to compare
    
    if compare1 != compare2:                #IS the words first 5 elements match with 5 last numbers it have to quatify(6)
        return False,"Check digit " + str(compare2) + " does not match calculated value " + str(compare1)
    return True,"Library card is valid."            # This only return when (1),(2),(3),(4),(5),(6) is satify

if __name__=="__main__":
    while(1):   #(The loop run forever)
        print()
        card_num = input("Enter Library Card. Hit Enter to Exit ==> ")  #user input
        (checking,output) = verify_check_digit(card_num)    #because it is a tuple so we have to use this to break this (I forgot the name for it but it not accually break)
        
        if checking == True:    #Only run when it return True
            print(output)
            print("The card belongs to a student in " + get_school(card_num))
            print("The card belongs to a " + get_grade(card_num))
                
        else:               #If this false will run this
            print("Library card is invalid.")
            print (output)


