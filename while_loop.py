'''
i = 6
while(i < 19):
    i = i + 1
    print(i)
'''
'''
for i in range(7, 19):
    if i % 2 == 0:
        print(i)
'''
def evens():
    
    number1 = int(input("Please enter 1st random number: "))
    number2 = int(input("Please enter 2nd random number: "))
    for i in range(number1, number2):
        print(i * 2)
evens()