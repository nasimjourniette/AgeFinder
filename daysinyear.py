import datetime

months = [
    {"month": 1, "days": 31},
    {"month": 2, "days": 28},
    {"month": 3, "days": 31},
    {"month": 4, "days": 30},
    {"month": 5, "days": 31},
    {"month": 6, "days": 30},
    {"month": 7, "days": 31},
    {"month": 8, "days": 31},
    {"month": 9, "days": 30},
    {"month": 10, "days": 31},
    {"month": 11, "days": 30},
    {"month": 12, "days": 31},
]


def main():
    print(find_days_in_current_year())


def find_days_in_current_year():
    date, time = str(datetime.datetime.now()).split(" ")
    date_year, date_month, date_day = date.split("-")
    amount_months = [month for month in months if int(month["month"]) <= int(date_month) - 1]
    amount_days = []
    for days in amount_months:
        amount_days.append(int(days["days"]))

    return int(sum(amount_days) + int(date_day))


if __name__ == "__main__":
    main()
