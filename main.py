'''
name = input("Please enter your name: ")
age = input("Please enter your age: ")
print(f"Your name is: {name} and you are {age} Years Old!" )
'''
'''
Number = input("Please enter a 2 digit number: ")
a = int(Number[0]) 
b = int(Number[1])  
c = a + b
print(f"The result of the 2 numbers is: {c}")
'''

#enter your weight in kilograms and height in metres 

'''
Weight = float(input("Please enter your weight in kilograms: "))
Height = float(input("Please enter your height in metres: "))

BMI = Weight / (Height * Height)

if BMI <18:
    print("You are underweight")
elif BMI >19:
    print("You are overweight")


print("Your BMI is: " + round(BMI))
'''

#determine if a user has entered a number and tell if its even or odd

'''
Number = float(input("Please enter a number: "))

if Number % 2 == 0:
    print("It is an even number")
else:
    print("It is an odd number")
'''

'''
import random 
Coin_Flip = random.randint(1, 2)
if Coin_Flip == 1:
    print('Heads')
else:
    print('Tails')
#print(dice_value)
'''


#add all numbers up to 100
'''
for i in range (1, 101):
    if i % 2 == 0:
        add  = i + 2 
        print(add)
'''

'''

def my_Function():
    print("Hello Champ")
    print("HOw are you doing")
my_Function()
def greet_with(name, location):
   print(f'Hello {name}!')
   print(f'What is it like in {location}?')
greet_with("Joshua", "Ghana")
'''


Students_Scores = {
    
    "Joshua": 20,
    "Kwame" : 12,
    "Trina" : 11,
    "Abbot" : 20,
    
    }