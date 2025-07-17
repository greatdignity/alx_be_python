num1 = int(input('Enter the first number: '))
num2 = int(input('Enter the second number: '))
operations = input("Choose the operation (+, -, *, /): ")
match operations:
    case "Addition":
        result = int(num1) + int(num2)
        print(f'The result is: {result}.')
    case "Multiplication":
        result = int(num1) * int(num2)
        print(f'The result is: {result}.')
    case "Subtraction":
        result = int(num1) - int(num2)
        print(f'The result is: {result}.')
    case "Division":
        if num2 != 0:
            result = int(num1) / int(num2)
            print(f'The result is: {result}.')
        else:
            print('Cannot divide by zero.')
    case _:
        print('Invalid operation')