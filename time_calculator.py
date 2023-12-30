def add_time(start_time, duration, start_day=None):
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    day_count = {"Monday": 0, "Tuesday": 1, "Wednesday": 2, "Thursday": 3, "Friday": 4, "Saturday": 5, "Sunday": 6}

    # Split start time into hour, minute, and AM/PM
    start_time = start_time.split(":")
    start_hour = int(start_time[0])
    start_minute = int(start_time[1].split(" ")[0])
    start_ampm = start_time[1].split(" ")[1]

    # Split duration into hour and minute
    duration = duration.split(":")
    duration_hour = int(duration[0])
    duration_minute = int(duration[1])

    # Calculate the total minutes and update hour and minute
    total_minutes = start_hour * 60 + start_minute + duration_hour * 60 + duration_minute
    result_hour = total_minutes // 60
    result_minute = total_minutes % 60

    # Adjust the result hour based on AM/PM
    if start_ampm == "PM":
        result_hour += 12
        if result_hour == 24:
            result_hour = 12
    elif start_ampm == "AM" and result_hour == 0:
        result_hour = 12

    # Handle days later
    days_later = 0
    if result_hour >= 12:
        days_later = result_hour // 24
        result_hour %= 24

    # Handle day of the week
    if start_day:
        start_day = start_day.capitalize()
        days_later += day_count[start_day]
        result_day = days[(days_later) % 7]
    else:
        result_day = ""

    # Format the result time and day
    result_time = f"{result_hour}:{str(result_minute).zfill(2)} {start_ampm}"
    result_day = f", {result_day}" if result_day else ""

    # Format the result days later
    result_days_later = ""
    if days_later > 0:
        result_days_later = f" ({days_later} days later)" if days_later > 1 else " (next day)"

    return f"{result_time}{result_day}{result_days_later}"