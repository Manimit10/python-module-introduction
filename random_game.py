from random import randint

print(__name__)

def guess_game():
    answer = randint(1, 10)

    print(answer)
    count = 0

    while True:
        count +=1
        try:
            guess = input('I hold a number between 1 to 10 guess it: ')
            if int(guess) > 0 and int(guess) < 11:
                if int(guess) == answer:
                    print(f"You won after {count} tries!!")
                    break
            else:
                print('try another time.. ')
        except ValueError:
            print('Make sure you enter a number')
            continue