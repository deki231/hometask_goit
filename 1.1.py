import datetime

def get_days_from_today(date):
    date = datetime.datetime.strptime(date, "%Y-%m-%d" ).date()
    date_now = datetime.datetime.today().date()
    difference = date - date_now 
    return difference.days

print(get_days_from_today("2026-05-19"))