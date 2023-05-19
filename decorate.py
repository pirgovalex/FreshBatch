import datetime

# Get the initial date and hour from user input
initial_datetime_str = '2000-03-07 6:35'
initial_datetime_obj = datetime.datetime.strptime(initial_datetime_str, '%Y-%m-%d %H:%M')

# Get the current date and hour
current_datetime_obj = datetime.datetime.now()

# Calculate the time difference in hours
hours_passed = (current_datetime_obj - initial_datetime_obj).total_seconds() / 3600

print(f"{hours_passed:.2f} hours have passed since {initial_datetime_obj}")
