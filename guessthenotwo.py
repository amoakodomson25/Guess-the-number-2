# To utilize the functionalities for generating random
# numbers and working with random sequences in Python,
# the random module must be imported.
import random


def Guess_the_number():  # this is how a function is defined in python
    print("Guess The Number Game")
    print("---------------------")
    print("guess a number from 1 - 100")

    number_to_be_guessed = random.randint(1, 100)
    # this is a variable called number_to_be_guessed.
    # It uses The random.randint() function in Python which is used to generate a random
    # integer within a specified range, including both the lower and upper bounds. In this case,
    # lower bound is 1 and upper bound is 100

    attempts = 1  # this is an int variable assigned with integer 1

    while True:  # this is a while loop
        try:  # try block
            guessed_number = int(input("Your guess: "))

            if guessed_number > number_to_be_guessed:  # if statement
                print("your guess is higher, try again")
                attempts += 1  # adds 1 to the number of attempts
                # += is an augmented assignment operator that combines addition and assignment.
                # It provides a shorthand way to add a value to an existing variable
                # and then assign the result back to that same variable.

            elif guessed_number < number_to_be_guessed:
                # elif statement The elif keyword is pythons way of saying
                # "if the previous conditions were not true, then try this condition"
                print("your guess is lower, try again")
                attempts += 1
            else:  # else statement. The else keyword catches anything which isn't caught by the preceding conditions.
                print()
                print(f"you guessed right in {attempts} attempt(s)")
                break
        except ValueError:  # exception block
            print("input a valid number")


# In Python, a while loop executes a block of code repeatedly
# as long as a specified condition remains true. The break statement
# provides a mechanism to exit a loop prematurely, even if the loop's condition is still true.

# In Python, try and except blocks are used for exception handling,
# which allows a program to gracefully manage errors that occur
# during execution instead of crashing.


Guess_the_number()  # this runs the function
