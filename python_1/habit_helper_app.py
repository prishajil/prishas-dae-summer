habit_list = ["Sleep", "Hydration", "Reading", "Exercise"]

habit_goals = {"Sleep": 8, "Hydration": 8, "Reading": 1, "Exercise": 1}
habit_completed = {}

def check_progress(habit_name, actual_value):
    goal = habit_goals[habit_name]
    if actual_value > goal:
        return "Goal exceeded"
    elif actual_value==goal:
        return "Goal met"
    elif actual_value >= 0.75 * goal:
        return "Almost there!"
    else:
        return False


for habit in habit_list:
    print(f"\nTracking: {habit}")
    user_input = int(input(f"How much {habit.lower()} did you have/do today?"))
    habit_completed[habit] = check_progress(habit, user_input)


def display_summary():
    print("\n\033[1mHabit Summary:\033[0m")
    for habit, status in habit_completed.items():
        if status == "Goal exceeded":
            print(f"Nice work -- You've exceeded your goal for {habit}!")
        elif status == "Goal met":
            print (f"You've met your goal for {habit}! Great job!")
        elif status == "Almost there!":
            print(f"You're almost at your goal for {habit}! Keep perservering!")
        else: 
            print(f"You missed your goal for {habit} today. Keep going and try again tomorrow. :)")

display_summary()
