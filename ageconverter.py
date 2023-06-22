import datetime
from daysinyear import find_days_in_current_year

#make a dict with the months and the days in the month to iterate
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
date_year = int(date_year)
date_month = int(date_month)
date_day = int(date_day)
hour, minute, second = time.split(":")

def main():
    while True:
        #while the input is invalid ask for the input 
        birthday = input("What's your birthdate in yyyy/m/d format? ")
        try:
            separate_birthdate(birthday)
        except ValueError:
            print("Not Valid")
        else:
            print(find_age(separate_birthdate(birthday)))
            break

    exit()


def check_for_leap_year():
    #make a list to store the days in the year
    #sum is 365 on a normal year and 366 on a leap year
    days_in_the_year = []
    # iterate through all years until the current year
    for year in range(date_year):
        amount_of_days = []
        #if the year is divisible by 4 then it's a leap year and february's days get changed to 29
        if year % 4 == 0:
            for month in months:
                if month['month'] == 2:
                    month['days'] = 29
                amount_of_days.append(month['days'])
            days_in_the_year.append(sum(amount_of_days))
        else:
            for month in months:
                if month['month'] == 2:
                    month['days'] = 28
                amount_of_days.append(month['days'])
            days_in_the_year.append(sum(amount_of_days))
    return days_in_the_year


def separate_birthdate(birthdate):
    if '/' in birthdate and len(birthdate.split('/')) == 3:
        year, month, day = birthdate.split('/')
    else:
        raise ValueError
    if len(day) == 1:
        day = day.zfill(2)
    if len(month) == 1:
        month = month.zfill(2)
    # if the date that is inputted is in the future, then it's not valid
    if int(year) == date_year:
        if int(month) > date_month:
            raise ValueError
        elif int(month) == date_month and int(day) > date_day:
            raise ValueError
    #make sure month can't be over 12 and day can't be over the amount of days in the month
    if date_year % 4 == 0:
        if int(month) == 2 and int(day) > 29:
            raise ValueError
    if int(month) > 12 or int(year) > date_year:
        raise ValueError
    for numbered_month in months:
        if numbered_month['month'] == int(month):
            if int(year) % 4 == 0 and numbered_month['month'] == 2 and int(day) == 29:
                return year, month, day
            if numbered_month['days'] < int(day):
                raise ValueError

    return year, month, day


def find_age(birthday):
    #stands for number of days
    nod = []
    y, m, d = birthday[0], birthday[1], birthday[2]
    #iterate from the birthyear to the current year to find out if the birthyear is a leap year and the nod in each year
    #if so, then check if the birthday is after february 29th
    #if it is, subtract one from nod
    for i in range(int(y), date_year):
        if i % 4 == 0 and i == int(y):
            if int(m) > months[1]["month"]:
                nod.append(-1)
        nod.append(check_for_leap_year().pop(i))
    #iterate through each month until it reaches the birth month
    for _ in range(date_year):
        if date_year % 4 == 0:
            if int(m) > months[1]["month"]:
                months[1]["days"] = 29
                amount_months = [month for month in months if month["month"] <= int(m)]
        else:
            amount_months = [month for month in months if month["month"] <= int(m)]
    amount_days = []
    #iterate through each month until the birth month to find the sum of days
    for days in amount_months:
        amount_days.append(int(days["days"]))
    #find how many days the birthday is into the year
    amount_days = sum(amount_days) - (amount_days.pop() - int(d))
    days_between_bd_and_cd = 365 - amount_days + find_days_in_current_year()
    #a lot of calculations for different circumstances
    if int(m) == date_month and int(d) == date_day:
        return (f"You are {round(sum(nod) * 86400 + int(hour)*3600 + int(minute)*60 + float(second), 5)} seconds old.\n"
                f"You are {round(sum(nod) * 1440 + int(hour)*60 + int(minute) + float(second)/60, 5)} minutes old.\n"
                f"You are {round(sum(nod) * 24 + int(hour) + int(minute)/60 + float(second)/3600, 5)} hours old.\n"
                f"You are {round(sum(nod) + int(hour)/24 + int(minute)/1440, 5)} days old.\n"
                f"You are {round(sum(nod) / 7 + int(hour)/168 + int(minute)/10080, 5)} weeks old.\n"
                f"You are {round(sum(nod) / (sum(nod) / len(nod) / 12) + int(hour)/730.32 + int(minute)/43819.2, 5)} months old.\n"
                f"You are {round(len(nod) + int(hour)/8760, 5)} years old.")
    elif int(y) == date_year:
        if int(y) % 4 == 0 and amount_days > 60 or int(y) % 4 != 0:
            nod_alive = days_between_bd_and_cd - 365
            return (f"You are {round(nod_alive * 86400 + int(hour)*3600 + int(minute)*60 + float(second), 5)} seconds old.\n"
                    f"You are {round(nod_alive * 1440 + int(hour)*60 + int(minute) + float(second)/60, 5)} minutes old.\n"
                    f"You are {round(nod_alive * 24 + int(hour) + int(minute)/60 + float(second)/3600, 5)} hours old.\n"
                    f"You are {round(nod_alive + int(hour)/24 + int(minute)/1440, 5)} days old.\n"
                    f"You are {round(nod_alive / 7 + int(hour)/168 + int(minute)/10080, 5)} weeks old.\n"
                    f"You are {round(nod_alive / (365 / 12) + int(hour)/730.32 + int(minute)/43819.2, 5)} months old.\n"
                    f"You are {round(nod_alive / 365 + int(hour)/8760, 5)} years old.")
        else:
            nod_alive = days_between_bd_and_cd - 366
            return (f"You are {round(nod_alive * 86400 + int(hour)*3600 + int(minute)*60 + float(second), 5)} seconds old.\n"
                    f"You are {round(nod_alive * 1440 + int(hour)*60 + int(minute) + float(second)/60, 5)} minutes old.\n"
                    f"You are {round(nod_alive * 24 + int(hour) + int(minute)/60 + float(second)/3600, 5)} hours old.\n"
                    f"You are {round(nod_alive + int(hour)/24 + int(minute)/1440, 5)} days old.\n"
                    f"You are {round(nod_alive / 7 + int(hour)/168 + int(minute)/10080, 5)} weeks old.\n"
                    f"You are {round(nod_alive / (366 / 12) + int(hour)/730.32 + int(minute)/43819.2, 5)} months old.\n"
                    f"You are {round(nod_alive / 366 + int(hour)/8760, 5)} years old.")

    elif int(y) % 4 == 0 and amount_days > 60:
        nod_alive = (sum(nod) + sum(nod) / (len(nod) - 1) - (365 + (365 - days_between_bd_and_cd)))
        return (f"You are {round(nod_alive * 86400 + int(hour)*3600 + int(minute)*60 + float(second), 5)} seconds old.\n"
                f"You are {round(nod_alive * 1440 + int(hour)*60 + int(minute) + float(second)/60, 5)} minutes old.\n"
                f"You are {round(nod_alive * 24 + int(hour) + int(minute)/60 + float(second)/3600, 5)} hours old.\n"
                f"You are {round(nod_alive + int(hour)/24 + int(minute)/1440, 5)} days old.\n"
                f"You are {round(nod_alive / 7 + int(hour)/168 + int(minute)/10080, 5)} weeks old.\n"
                f"You are {round(nod_alive / (sum(nod)/(len(nod)-1) / 12) + int(hour)/730.32 + int(minute)/43819.2, 5)} months old.\n"
                f"You are {round(nod_alive / (sum(nod)/(len(nod)-1)+ int(hour)/8760), 5)} years old.")

    elif int(y) % 4 != 0 or int(y) % 4 == 0:
        nod_alive = (sum(nod) + sum(nod) / len(nod) - (365 + (365 - days_between_bd_and_cd)))
        return (f"You are {round(nod_alive * 86400 + int(hour)*3600 + int(minute)*60 + float(second), 5)} seconds old.\n"
                f"You are {round(nod_alive * 1440 + int(hour)*60 + int(minute) + float(second)/60, 5)} minutes old.\n"
                f"You are {round(nod_alive * 24 + int(hour) + int(minute)/60 + float(second)/3600, 5)} hours old.\n"
                f"You are {round(nod_alive + int(hour)/24 + int(minute)/1440, 5)} days old.\n"
                f"You are {round(nod_alive / 7 + int(hour)/168 + int(minute)/10080, 5)} weeks old.\n"
                f"You are {round(nod_alive / (sum(nod)/(len(nod)) / 12 + int(hour)/730.32 + int(minute)/43819.2), 5)} months old.\n"
                f"You are {round(nod_alive / (sum(nod)/len(nod) + int(hour)/8760), 5)} years old.")


if __name__ == "__main__":
    main()
