print('Welcome to Flarsheim Guesser!') # Message Welcome to Flarsheim Guesser!
print()
choose = 'Y' # Variable to store user choice
while choose =='Y' or choose =='y': #This loop is continue if the user type 'Y' or 'y' if they want to try it (other number) again. 
    print('Please think of a number between and including 1 and 100.')
    print()
    threeleft = 0   #set up the varible use for remainer of 3
    fiveleft = 0    #set up the varible use for remainer of 5
    sevenleft = 0   #set up the varible use for remainer of 7
    while True: #This loop is run again again and again until break function
        threeleft = int(input('What is the remainder when your number is divided by 3 ?'))
        if 3> threeleft >=0:    #condition
            break       #break out of the loop and move-on to the next if qualify the condition
        elif threeleft >=3:     #condition
            print('The value entered must be less than 3')
            continue    # continue the loop if > or = 3
        else:       
            print('The value entered must be 0 or greater')
            continue    # continue the loop if it is something else like a negative number 
    print()
    while True:   #This loop is run again again and again until break function
        fiveleft = int(input('What is the remainder when your number is divided by 5 ?'))
        if 5> fiveleft >=0: #condition
            break   #break out of the loop and move-on to the next if qualify the condition
        elif fiveleft >=5:  #condition
            print('The value entered must be less than 5')
            continue     # continue the loop if > or = 5
        else:   
            print('The value entered must be 0 or greater')
            continue     # continue the loop if it somethin else
    print()
    while True:     #This loop is run again again and again until break function
        sevenleft = int(input('What is the remainder when your number is divided by 7 ?'))
        if 7> sevenleft >=0:
            break       #break out of the loop and move-on to the next if qualify the condition
        elif sevenleft >=5:
            print('The value entered must be less than 7')
            continue    # continue the loop if > or = 7
        else:
            print('The value entered must be 0 or greater')
            continue    # continue the loop if it somethin else
    for num in range(1,101):    #For each number from 1to 100
        if num%3==threeleft and num%5 == fiveleft and num%7 == sevenleft:   #Find the number from 1 to 100 that remainder %3,%5,%7 same with the user input 
            print(f'Your number was {num} ') #print out the number that qualifily all the condition
            print('How amazing is that?')
            print()
    choose = input('Do you want to play again? Y to continue, N to quit ==>')  #Ask to play again
    if choose == 'Y' or choose =='y':   #if the user type Y or y continue all again
        continue
    elif choose == 'N' or choose =='n': #if the user type N or n break te first loop and it end 
        break
    while choose!='Y' or choose!='y' or choose!='N' or choose!='n': # Loop ask the user want to play again if they not type Y or y or N or n  
        choose = input('Do you want to play again? Y to continue, N to quit ==>')
        if choose == 'Y' or choose =='y' or choose == 'N' or choose =='n':  #If they type one of the condition Y or y or N or n this loop will break
            break
        
    print()
        
