task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")
reminder = f"Reminder: Your task '{task}' has a {priority} priority"
match priority:
    case "high":
        reminder += ". This is very important."
    case "medium":
        reminder += ". You should work on this soon."
    case "low":
        reminder += ". Do this whenever you have free time."
    case _:
        reminder += ". (Unknown priority level provided.)"
if time_bound == "yes":
    reminder += ". It is time-bound and requires immediate attention!"
print(reminder)