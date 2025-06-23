import random

print("Guess the number game 2!")
print("1-100")
number_to_be_guessed = random.randint(1, 100)
attempts = 1

while True:
    try:
        guessed_number = int(input("Guess the number: "))

        if guessed_number > number_to_be_guessed:
            print("number guessed is higher, try again")
            attempts += 1
        elif guessed_number < number_to_be_guessed:
            print("number guessed is lower, try again")
            attempts += 1
        else:
            print(f'yaay you guessed right in {attempts} attempt(s)')
            break
    except ValueError:
        print("Type a valid number")
