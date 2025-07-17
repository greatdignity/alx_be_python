task = input("Enter your task: ")
time_bound = input("Is it time-bound? (yes/no): ")
priority = input("Priority (high,medium,low): ")
match priority:
    case "high":
        if time_bound =="yes":
            print(f"Reminder: '{task}' is a {priority} priority task that requires immediate attention today!")
    case "low":
        if time_bound == "yes":
            print(f"Note: '{task}' is a {priority} priority task. Consider completing it when you have free time.")
