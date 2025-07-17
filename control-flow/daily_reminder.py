Task = input('Enter your task: ')
Priority = input('Enter priority (high, medium,low): ')
Time_Bound = input('is the task time-bound? (yes/no): ')
match Priority:
    case "high":
        if Time_Bound =="yes":
            print(f"Reminder: '{Task}' is a {Priority} priority task that requires immediate attention today!")
        else:
            print('Enjoy your day!')
    case "medium":
        if Time_Bound == "no":
            input('Enter a date you will like to complete this task: ')
            print('Your schedule is fixed. Enjoy your day!')
        else:
            print('Have a nice day!')
    case "low":
        if Time_Bound == "yes":
            print(f"Note: '{Task}' is a {Priority} priority task. Consider completing it when you have free time.")
