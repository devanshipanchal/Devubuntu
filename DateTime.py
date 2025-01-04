from datetime import datetime, timedelta

# Write a Python script to display the various Date Time formats.
# a) Current date and time
# b) Current year
# c) Month of year
# d) Week number of the year
# e) Weekday of the week
# f) Day of year
# g) Day of the month
# h) Day of week

now = datetime.now()
# a) Current date and time
current_date_time = now.strftime("%Y-%m-%d %H:%M:%S")
print("Current date and time:", current_date_time)
# b) Current year
current_year = now.strftime("%Y")
print("Current year:", current_year)
# c) Month of year
current_month = now.strftime("%B")
print("Month of year:", current_month)
# d) Week number of the year
week_number = now.strftime("%U")
print("Week number of the year:", week_number)
# e) Weekday of the week
weekday_name = now.strftime("%A")
print("Weekday of the week:", weekday_name)
# f) Day of year
day_of_year = now.strftime("%j")
print("Day of year:", day_of_year)
# g) Day of the month
day_of_month = now.strftime("%d")
print("Day of the month:", day_of_month)
# h) Day of week
day_of_week = now.strftime("%w")
print("Day of week:", day_of_week)

# Write a Python program to determine whether a given year is a leap year.
year = int(input("Enter a year: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("It ia leap Year", year)
else:
    print("Not a leap year")
# Write a Python program to print leap years in between 1900 to 2000 years
for year in range(1900, 2001):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print(year)

# Write a Python program to get the below output.
# Inputs :
# 	Enter Day : 20
# 	Enter Month : 3
# Enter year : 2022
# Result :
# Date is : 2022-03-20
# day = int(input("Enter Day: "))
# month = int(input("Enter Month: "))
# year = int(input("Enter Year: "))
# date = datetime.date(year, month, day)
# # Print the date in YYYY-MM-DD format
# print("Date is:", date)

# 5. Write a Python program to get the below output.
# Inputs :
# 	Enter Date[DD-MM-YYYY] : 3-12-2022
# Result :
# 	3 Dec 2022
input_date = input("Enter Date[DD-MM-YYYY]: ")
date_object = datetime.strptime(input_date, "%d-%m-%Y")
formatted_date = date_object.strftime("%-d %b %Y")
print("Result:")
print(formatted_date)

# Write a Python program to print yesterday, today, tomorrow dates.
today = datetime.today().date()
yesterday = today - timedelta(days=1)
tomorrow = today + timedelta(days=1)
print("Yesterday's date:", yesterday)
print("Today's date:", today)
print("Tomorrow's date:", tomorrow)

# Write a Python program to convert the date to datetime (midnight of the date) in Python.


# Write a Python program to find a date in a given year and number of days
input_year = int(input("Enter Year[YYYY]: "))
No_of_day = int(input("Enter no. of day: "))
start_date = datetime(year, 1, 1)  # January 1st of the given year
result_date = start_date + timedelta(days=No_of_day - 1)
formatted_date = result_date.strftime("%Y-%m-%d")
day = result_date.day
print("Result:")
print("Date Will be:", formatted_date)

# Write a Python program to print the beginning and end date of a given month and year.



# Write a Python program to print age(year,month,days) from a given date of birth.
# Inputs :
# *==== Find Age ==== *
# Enter year : 1994
# Enter month : 1
# Enter day : 11
# Result :
# 	Date of Birth : 11/1/1994
# 	Age : 28 years 1 months 22 days

birth_year = int(input("Enter year: "))
birth_month = int(input("Enter month: "))
birth_day = int(input("Enter day: "))
date_of_birth = datetime(birth_year, birth_month, birth_day)
current_date = datetime.today()

age_years = current_date.year - date_of_birth.year
age_months = current_date.month - date_of_birth.month
age_days = current_date.day - date_of_birth.day
if age_days < 0:
    age_months -= 1
    age_days += (date_of_birth.replace(month=date_of_birth.month + 1, day=1) - date_of_birth.replace(month=date_of_birth.month, day=1)).days
if age_months < 0:
    age_years -= 1
    age_months += 12
date_of_birth_str = date_of_birth.strftime("%d/%m/%Y")
print("Date of Birth:", date_of_birth_str)
print(f"Age: {age_years} years {age_months} months {age_days} days")