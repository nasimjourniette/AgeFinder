# import time
import datetime
from daysinyear import find_days_in_current_year


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


# find the date and time for today
date, time = str(datetime.datetime.now()).split(" ")
date_year, date_month, date_day = date.split("-")

def main():
    while True:
        try:
            birthday = input("What's your birthday in yyyy/mm/dd format? ")
            convert_birthday(birthday)
        except ValueError:
            print("Not the right format")
        else:
            print(check_birthday_with_today_date(convert_birthday(birthday)))
            break

# check for valid birthdates and 

def convert_birthday(birthdate):
    if "/" in birthdate and len(birthdate.split("/")) == 3:
        year, month, day = birthdate.split("/")
        if (
            len(year) < 4
            or int(year) > int(date_year)
            or int(month) > 12
            or int(day) > 31
        ):
            raise ValueError
        if len(month) == 1:
            month = month.zfill(2)
        if len(day) == 1:
            day = day.zfill(2)
        
    elif birthdate.isalnum() is False:
        raise ValueError
    else:
        raise ValueError

    return (year, month, day)


# if today's date equals birthday find out the year of birthday
# else find how many days are in between the date and the birthday


def check_birthday_with_today_date(birthday):
    y, m, d = birthday[0], birthday[1], birthday[2]
    if m == date_month and d == date_day:
        return (
            f"{(int(date_year) - int(y)) * 365.25} days old\n"
            f"{(int(date_year) - int(y)) * 12 * 4.34819} days old\n"
            f"{(int(date_year) - int(y)) * 12} months old\n"
            f"{int(date_year) - int(y)} years old"
        )
    else:
        amount_months = [month for month in months if int(month["month"]) <= int(m)]

    amount_days = []

    for days in amount_months:
        amount_days.append(int(days["days"]))
    
    #counts every day in the year until your birthday by adding every day in each month stopping at your birth month
    #then it subtracts by the number of days in your birth month minus your birthday number; e.g Jan 5 = 31 - (31 - 5)
    amount_days = sum(amount_days) - (int(amount_days.pop()) - int(d))
    
    #calculate for leap years
    # convert the number of years to days and find out how many days old at this moment
    # do the same with months and weeks too
    if (int(date_year) - int(y)) > 4:
        return (
            f"{float((int(date_year) - int(y) - 1) * 365.25 + (365 - amount_days + find_days_in_current_year()))} days old\n"
            f"{round(((int(date_year) - int(y)) * 12 - (int(m) - int(date_month)) + round((int(date_day) - int(d)) / 30.437, 3)) * 4.34819,3)} weeks old\n"
            f"{(int(date_year) - int(y)) * 12 - (int(m) - int(date_month)) + round((int(date_day)-int(d))/30.437,3)} months old\n"
            f"{int(date_year) - int(y) - 1 + round((365 - amount_days + find_days_in_current_year())/365,3)} years old"
        )

    else:
        return (
            f"{(int(date_year) - int(y) - 1) * 365 + (365 - amount_days + find_days_in_current_year())} days old\n"
            f"{round(((int(date_year) - int(y)) * 12 - (int(m) - int(date_month)) + round((int(date_day) - int(d)) / 30.437, 3)) * 4.34819,3)} weeks old\n"
            f"{(int(date_year) - int(y)) * 12 - (int(m) - int(date_month)) + round((int(date_day) - int(d)) / 30.437, 3)} months old\n"
            f"{round(int(date_year) - int(y) - 1 + (365 - amount_days + find_days_in_current_year())/365,3)} years old"
        )

if __name__ == "__main__":
    main()
