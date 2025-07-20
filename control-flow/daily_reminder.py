# daily_reminder.py

task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

match priority:
    case "high" | "medium":
        message = f"Reminder: '{task}' is a {priority} priority task"
        if time_bound == "yes":
            message += " that requires immediate attention today!"
        else:
            message += "."
    case "low":
        if time_bound == "no":
            message = f"Note: '{task}' is a low priority task. Consider completing it when you have free time."
        else:
            message = f"Note: '{task}' is a low priority task."
    case _:
        # fallback for undefined priorities
        if time_bound == "yes":
            message = f"Reminder: '{task}' is a task that requires immediate attention today!"
        else:
            message = f"Note: '{task}' is a task with undefined priority."

print(message)
