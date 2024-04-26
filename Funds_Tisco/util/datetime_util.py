from datetime import timedelta, date, datetime

def get_weekdays(start_date, end_date):
    weekdays = []
    current_date = start_date
    while current_date <= end_date:
        if current_date.weekday() < 5:
            weekdays.append(current_date)
        current_date += timedelta(days=1)
    return weekdays

def get_last_working_day():
    t = date.today()
    return get_weekdays(t - timedelta(days = 14), t - timedelta(days=1))[-1]

