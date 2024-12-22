def daily_reminder():
    task = input("Enter your task: ")
    priority = input("Priority (high/medium/low): ")
    time_bound = input("Is it time-bound? (yes/no): ")

    valid_priorities = {"high", "medium", "low"}
    if priority not in valid_priorities:
        print("Invalid priority. Please restart the program and enter high, medium, or low.")
        return

    match priority:
        case "high":
            reminder = f"'{task}' is a high priority task."
        case "medium":
            reminder = f"'{task}' is a medium priority task."
        case "low":
            reminder = f"'{task}' is a low priority task."

    if time_bound == "yes":
        reminder += " It requires immediate attention today!"
    elif time_bound == "no":
        reminder += " Consider completing it when you have free time."
    else:
        print("Invalid input for time-bound status. Please restart the program and enter yes or no.")
        return

    
    print("\nReminder:", reminder)

daily_reminder()
