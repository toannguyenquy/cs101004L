print('Welcome to Flarsheim Guesser!')
print()
choose = 'Y'
while choose =='Y' or choose =='y':
    print('Please think of a number between and including 1 and 100.')
    print()
    threeleft = 0
    fiveleft = 0
    sevenleft = 0
    while True:
        threeleft = int(input('What is the remainder when your number is divided by 3 ?'))
        if 3> threeleft >=0:
            break
        elif threeleft >=3:
            print('The value entered must be less than 3')
            continue
        else:
            print('The value entered must be 0 or greater')
            continue
    print()
    while True:
        fiveleft = int(input('What is the remainder when your number is divided by 5 ?'))
        if 5> fiveleft >=0:
            break
        elif fiveleft >=5:
            print('The value entered must be less than 5')
            continue
        else:
            print('The value entered must be 0 or greater')
            continue
    print()
    while True:
        sevenleft = int(input('What is the remainder when your number is divided by 7 ?'))
        if 7> sevenleft >=0:
            break
        elif sevenleft >=5:
            print('The value entered must be less than 7')
            continue
        else:
            print('The value entered must be 0 or greater')
            continue
    for num in range(1,101):
        if num%3==threeleft and num%5 == fiveleft and num%7 == sevenleft:
            print(f'Your number was {num} ')
            print('How amazing is that?')
            print()
    choose = input('Do you want to play again? Y to continue, N to quit ==>')
    if choose == 'Y' or choose =='y':
        continue
    elif choose == 'N' or choose =='n':
        break
    while choose!='Y' or choose!='y' or choose!='N' or choose!='n':
        choose = input('Do you want to play again? Y to continue, N to quit ==>')
        if choose == 'Y' or choose =='y' or choose == 'N' or choose =='n':
            break
        
    print()
        
