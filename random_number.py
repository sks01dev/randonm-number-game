from random import randint

lower_num, higher_num = 1, 10
random_number = randint(lower_num, higher_num)
print(f"Guess the number in the range from {lower_num} to {higher_num}. You only get 3 guesses!")

c = 0
while True:
    if c < 3:
        try:
            user_guess = int(input("Guess: "))  
        except ValueError:
            print("Please enter a valid number.")
            continue

        if user_guess > random_number:
            print("The number is lower.")
            c += 1
        elif user_guess < random_number:
            print("The number is higher.")
            c += 1
        else:
            print("You guessed it!")
            break
    else:
        print("Your attempts are over! Try again.")
        break
