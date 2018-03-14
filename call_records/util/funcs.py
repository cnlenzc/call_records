import datetime


def get_last_month():
    year_today, month_today = datetime.date.today().timetuple()[:2]
    year_last = year_today
    month_last = month_today - 1
    if month_last == 0:
        month_last = 12
        year_last -= 1

    dt = datetime.date(year_last, month_last, 1)
    period_last = dt.strftime('%Y-%m')

    return period_last
