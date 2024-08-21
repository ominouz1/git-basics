def calculate():
    number = int(input("Please input a random number: "))
    number2 = int(input("Please input a second random number: "))
    action = input("Please enter a function: ")

    if action == "add":
        print(number + number2)
    elif action == "subtract":
        print(number - number2)
    elif action == "multiply":
        print(number * number2)
    else: 
        print(number / number2)


    
'''
    add = number + number2
    subtract = number - number2
    mulitply = number * number2
    divide = number / number2
'''

calculate()