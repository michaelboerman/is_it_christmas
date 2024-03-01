import datetime

def is_it_christmas():

    # Get the current date and time in the user's timezone
    current_datetime = datetime.datetime.now(datetime.timezone.utc).astimezone()

    # Get the user's timezone
    user_timezone = current_datetime.tzinfo

    # Get the current year
    current_year = current_datetime.year

    # Define Christmas date
    christmas_date = datetime.datetime(current_year, 12, 25)

    # Check if today is Christmas
    if current_datetime.date() == christmas_date.date():
        print("YES")
    else:
        print("NO")

# option to run it
if __name__ == "__main__":
    is_it_christmas()