from datetime import date, timedelta, datetime

def get_birthdays_per_week(users):
    today = date.today()
    weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    birthdays = {day: [] for day in weekdays}

    for user in users:
        birthday_this_year = user['birthday'].replace(year=today.year)
        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)
        days_to_birthday = (birthday_this_year - today).days
        if days_to_birthday > 7:
            continue
        weekday = weekdays[birthday_this_year.weekday()]
        if weekday in ['Saturday', 'Sunday']:
            weekday = 'Monday'
        birthdays[weekday].append(user['name'])

    # Remove empty days
    birthdays = {day: names for day, names in birthdays.items() if names}

    return birthdays

if __name__ == "__main__":
    users = [
        {"name": "Jan Koum", "birthday": datetime(1976, 1, 1).date()},
    ]

    result = get_birthdays_per_week(users)
    print(result)
    for day_name, names in result.items():
        print(f"{day_name}: {', '.join(names)}")
