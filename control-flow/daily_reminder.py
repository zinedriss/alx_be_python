# daily_reminder.py

# Prompt for a Single Task
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Process the Task Based on Priority and Time Sensitivity
reminder_message = ""

match priority:
    case "high":
        reminder_message = f"'{task}' is a high priority task"
    case "medium":
        reminder_message = f"'{task}' is a medium priority task"
    case "low":
        reminder_message = f"'{task}' is a low priority task"
    case _:
        reminder_message = f"'{task}' is a task" # Default for unrecognised priority

# Modify the reminder if the task is time-bound
if time_bound == "yes":
    reminder_message += " that requires immediate attention today!"
else:
    # Add a suggestion for non-time-bound low priority tasks
    if priority == "low":
        reminder_message += ". Consider completing it when you have free time."
    else:
        reminder_message += ". Consider completing it today." # For non-time-bound high/medium

# Provide a Customized Reminder
print("\nReminder:", reminder_message)

print("\nWell done on completing this project! Let the world hear about this milestone achieved.")
print("🚀 Click here to tweet! 🚀")