# explore_datetime.py

from datetime import datetime, timedelta

def display_current_datetime():
    current_date = datetime.now()
    print("Current Date and Time:", current_date.strftime("%Y-%m-%d %H:%M:%S"))

def calculate_future_date():
    try:
        days = int(input("Enter the number of days to add: "))
        future_date = datetime.now() + timedelta(days=days)
        print("Future Date:", future_date.strftime("%Y-%m-%d"))
    except ValueError:
        print("Invalid input. Please enter an integer.")

def main():
    print("=== DateTime Explorer ===")
    display_current_datetime()
    calculate_future_date()

if __name__ == "__main__":
    main()
