#1. Age calculator
#Write a Python program to ask for a user's name and year of birth, then calculate and display their age.
name = input("Enter your name: ")
age = int(input("Enter your year of birth: "))
print(f'{name}\'s age is {2025-age} years old.')



#2. Extract Car Names
# Extract car names from the following text:
txt = 'LMaasleitbtui'
print(txt[::2])
print(txt[1::2])



#3. Extract Car Names
# Extract car names from the following text:
txt = 'MsaatmiazD'
print(txt[::2])
print(txt[::-2])



#4. Extract Residence Area
# Extract the residence area from the following text:
txt = "I'am John. I am from London"
a = txt.index('from')+5
print(txt[a::])




#5. Reverse String
# Write a Python program that takes a user input string and prints it in reverse order.
my_input = input('Enter a string: ')
my_input2 = my_input[::-1]
print(my_input2)



#6. Count Vowels
# Write a Python program that counts the number of vowels in a given string.
my_input = input('Enter a string: ')
my_input2 = my_input.count('a') + my_input.count('e') + my_input.count('i') + my_input.count('u') + my_input.count('o') + my_input.count('y')
print(my_input2)



#7. Find Maximum Value
# Write a Python program that takes a list of numbers as input and prints the maximum value.
inp = input("Enter a list of numbers with ','")
a = inp.split(',')
print(f'Maximum value is: {max(a)}')




#8. Check Palindrome
# Write a Python program that checks if a given word is a palindrome (reads the same forward and backward).
inp = input("Enter a word: ")
rev = inp[::-1]
if inp == rev:
    print(f'{inp} is a palindrome')
else:
    print(f'{inp} is not a palindrome')



#9. Extract Email Domain
# Write a Python program that extracts and prints the domain from an email address provided by the user.
a = input('Enter your email: ')
print(f'{a}\'s doimain is {a[a.index('@')+1:]}')



#10. Generate Random Password
# Write a Python program to generate a random password containing letters, digits, and special characters.
import random
import string
length = int(input("Enter password length: "))
characters = string.ascii_letters + string.digits + string.punctuation
pas = ''.join(random.choice(characters) for _ in range(length))
print(pas)
