MAX_NUMBER = 1000000
MAX_LOOPS = 50
NUMBER_TO_GUESS = 500001

def verify(guess):
    if guess == NUMBER_TO_GUESS:
        return 0
    elif guess < NUMBER_TO_GUESS:
        return -1
    elif guess > NUMBER_TO_GUESS:
        return 1

def guess_the_number(guess, last_low=0, last_high=MAX_NUMBER, loops=1):
    if loops > MAX_LOOPS:
        raise Exception("You've had more than "+str(MAX_LOOPS)+" guesses!")
    if verify(guess) == 0:
        return guess
    elif verify(guess) == -1:
        last_low = guess
    elif verify(guess) == 1:
        last_high = guess
    guess = int((last_low+last_high)/2)
    return guess_the_number(guess, last_low, last_high, loops+1)

def test():
    print(guess_the_number(500000))
    print("Tests passed!")

if __name__ == "__main__":
    test()
