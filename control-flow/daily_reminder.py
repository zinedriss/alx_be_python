# daily_reminder.py

# Prompt for a Single Task
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Process the Task Based on Priority and Time Sensitivity
reminder_message = ""

# Use a Match Case statement to react differently based on the task’s priority.
match priority:
    case "high":
        reminder_message = f"'{task}' is a high priority task"
    case "medium":
        reminder_message = f"'{task}' is a medium priority task"
    case "low":
        reminder_message = f"'{task}' is a low priority task"
    case _: # Default case for any other input
        reminder_message = f"'{task}' is a task"

# Within the Match Case or after, use an if statement to modify the reminder if the task is time-bound.
if time_bound == "yes":
    reminder_message += " that requires immediate attention today!"
else:
    # Add a specific suggestion for low priority, non-time-bound tasks
    if priority == "low":
        reminder_message += ". Consider completing it when you have free time."
    else:
        # For non-time-bound high or medium priority tasks
        reminder_message += ". Consider completing it today."

# Provide a Customized Reminder
# Print a reminder about the task that includes its priority level and whether immediate action is required.
print(f"Reminder: {reminder_message}")

print("\nWell done on completing this project! Let the world hear about this milestone achieved.")
print("🚀 Click here to tweet! 🚀")