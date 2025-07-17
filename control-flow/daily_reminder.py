task = input('Enter your task: ')
priority = input('Enter priority (high,medium,low): ')
time_bound = input('is the task time-bound? (yes/no): ')
match priority:
    case "high":
        if time_bound =="yes":
            print(f"Reminder: '{task}' is a {priority} priority task that requires immediate attention today!")
        else:
            print('Enjoy your day!')
    case "medium":
        if time_bound == "no":
            input('Enter a date you will like to complete this task: ')
            print('Your schedule is fixed. Enjoy your day!')
        else:
            print('Have a nice day!')
    case "low":
        if time_bound == "yes":
            print(f"Note: '{task}' is a {priority} priority task. Consider completing it when you have free time.")
