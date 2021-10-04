import random

print("Hello. What is your name?")
name = input()
print("Well, {}, I am thinking of a number between 1 and 20.".format(name))
secret_number = random.randint(1,20)

for guessTaken in range(1,7):
    try:
        print('Take a guess')
        guess = int(input())
        if guess > secret_number:
            print('Your guess is too high')
        elif guess < secret_number:
            print('Your guess is too low')
        else:
            break
    except Exception as e:
        print(e)
        
if guess != secret_number:        
    print('Nope. The number I was thinking of was {}'.format(secret_number))
else:
    print('Good job, {}! You guessed my number in {} guesses!'.format(name, guessTaken))
    

