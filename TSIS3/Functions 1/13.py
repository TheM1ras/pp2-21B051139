import random
my_number = random.randint(1, 20)
print("Hello! What is your name?")
user_name = input()
text = "Well, {}, I am thinking of a number between 1 and 20."
print(text.format(user_name), "\nTake a guess.")
trying = 0
while(True):
    user_number = int(input())
    trying += 1
    if user_number == my_number:
        text = "\nGood job, {}! You guessed my number in {} guesses!"
        print(text.format(user_name, trying))
        break
    print("\nYour guess is too low. \nTake a guess.")
input()