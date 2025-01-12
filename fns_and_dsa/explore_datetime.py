from datetime import datetime, timedelta
def display_current_date():
    """displays current date and time in a readable format"""
    current_date = datetime.now()
    formatted_date = current_date.strftime("%Y-%m-%d-%H:%M:%S")
    print("Current date and time is: ", formatted_date)

def calculate_future_date():
    "calculate future_date bases on user input"
    days_to_add = int(input("Enter the number of days to be added: "))
    current_date = datetime.now()
    future_date = current_date + timedelta(days=days_to_add)
    formatted_date = future_date.strftime("%Y-%m-%d")
    print(f"Future date is : {formatted_date}")

def main():
    "Main function to demonstrate the use of datetime module"
    print("Exploring The Datetime module")
    display_current_date()
    calculate_future_date()

if __name__ == "__main__":
    main()
