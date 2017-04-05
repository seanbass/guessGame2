import random

# 1. Assign an integer to a variable
user_guesses = 0

# 2. Assign a string to a variable
name = raw_input('Hello! What shall I call you?\n')

# 4. Use the print function and .format() notation to print out the variable you assigned 
number = random.randint(1, 25)
print 'Well, {0}, I am thinking of a number between 1 and 25.'.format(name)



# 8. Use of a while loop
# 12. Define a function that returns a string variable
#  11. Create a tuple and iterate through it using a for loop to print each item out on a new line (Close enough?)
while user_guesses < 6:

    guess = int(raw_input('Take a guess: '))

    user_guesses += 1

    if guess < number:
        print 'Your guess is too low.'

    if guess > number:
        print 'Your guess is too high.'

    if guess == number:
        break


# 7. Use of conditional statements: if, elif, else
# 13. Call the function you defined above and print the result to the shell

if guess == number:
    print 'Good job, {0}! You guessed my number in {1} guesses! \n'.format(name, user_guesses)
else:
    print 'Close one! The number was {0} \n'.format(number)


# 5. Use each of these operators +, - , * , / , +=, ­= , % (Yes this is stupid and pointless to the program)

print 'Your number +1: ',number + 1
print 'Your number -1: ',number - 1
print 'Your number divided by 1: ',number / 1
print 'Your number multiplied by 1: ' ,number * 1
print 'The remainder of your number divided by 1.1: ',number % 1.1



# 10. Create a list and iterate through that list using a for loop to print each item out on a new line (Yes this is stupid and pointless to the program)

myList = ['\n That', '\n Was', '\n Fun!']
i = 0
while i < len(myList):
  print(myList[i])
  i += 1



print "\n List of all possible numbers: \n"


# 9. Use of a for loop (Yes this is stupid and pointless to the program)
for foo in range(1, 26):
    print "%d" % (foo),


# 3. Assign a float to a variable (Yes this is stupid and pointless to the program)
anotherNumber = 100.00



# 6. Use of logical operators: and, or, not (Yes this is stupid and pointless to the program)
foo = "Numbers are fun!"
zoo = "123"
bar = "Number are fun!"
if foo == 'abc' and bar == 'bac' or zoo == '123':
  print "<--- All these numbers are fun!"
  







