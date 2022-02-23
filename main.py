import random
def run_guess(guess,answer):
     if 0 < guess < 10:
         if guess == answer:
             print("Bravio Genio!!!")
             return True
     else:
         print("BOZO I said 1~10!!!! :P")
         return False

if __name__ == "__main__":
    answer = random.randint(1,10)
    while True:
        try:
            guess = int(input('Guess a number 1~10:  '))
            if (run_guess(guess, answer)):
                break
        except ValueError:
            print("Please Enter a number!!!")
            continue
