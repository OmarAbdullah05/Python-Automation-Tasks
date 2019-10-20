import random
#start program
print ('Hello. What is your name?')
name = input()
print('Hi, ' + name + ', How are you doing today?')
feeling = input()
if feeling == 'I am sad':
    secretnumber = random.randint(1, 10)
    print('Just becasue you are sad, I am going to make this game easier for you. Guess a number between 1 and 10')
    for guesstaken in range(1, 6):
        print('Take a guess.')
        guess = int(input())
        if guess < secretnumber:
            print('You guessed too low.')
        elif guess > secretnumber:
            print('You guessed too high')
        else:
            break #This condition is the correct guess

    if guess == secretnumber:
        print('Good job, ' + name + '! you guessed the correct number')
    else:
        print('Nice try, but the number I was thinking of was ' + str(secretnumber))
elif feeling == 'I am happy':
    secretnumber = random.randint(1, 15)
    print('Bcasue you are happy I will make this more challenging for you. Guess a number between 1 and 15')
    for guesstaken in range(1, 8):
        print('Take a guess.')
        guess = int(input())
        if guess < secretnumber:
            print('You guessed too low.')
        elif guess > secretnumber:
            print('You guessed too high')
        else:
            break #This condition is the correct guess

    if guess == secretnumber:
        print('Good job, ' + name + '! you guessed the correct number')
    else:
        print('Nice try, but the number I was thinking of was ' + str(secretnumber))
elif feeling == 'I am annoyed':
    secretnumber = random.randint(1, 5)
    print('Bcasue you are annoyed I will make this quick for you. Guess a number between 1 and 5')
    for guesstaken in range(1, 4):
        print('Take a guess.')
        guess = int(input())
        if guess < secretnumber:
            print('You guessed too low.')
        elif guess > secretnumber:
            print('You guessed too high')
        else:
            break #This condition is the correct guess

    if guess == secretnumber:
        print('Good job, ' + name + '! you guessed the correct number')
    else:
        print('Nice try, but the number I was thinking of was ' + str(secretnumber))
elif feeling == 'I am bored':
    secretnumber = random.randint(1, 20)
    print('Because you are bored I will make this long for you. Guess a number between 1 and 20')
    for guesstaken in range(1, 8):
        print('Take a guess.')
        guess = int(input())
        if guess < secretnumber:
            print('You guessed too low.')
        elif guess > secretnumber:
            print('You guessed too high')
        else:
            break #This condition is the correct guess

    if guess == secretnumber:
        print('Good job, ' + name + '! you guessed the correct number')
    else:
        print('Nice try, but the number I was thinking of was ' + str(secretnumber))
