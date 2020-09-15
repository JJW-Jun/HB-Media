#Calendar Month Program
terminate = False


#Program greeting
print('This program is a calendar month between 1800 and 2099')

while not terminate :
    #get month
    month_year = range(1, 13)
    month = int(input('Enter month 1-12 :  '))

    if month not in month_year :
        print('INVALID - Enter month 1-12! :  ')
        continue

    else :
        print(month)

    break


while month in month_year :
    #get year
    year_year = range(1800, 2100)
    year = int(input('Enter year 1800-2100 :  '))

    if year not in year_year :
        print('INVALID - Enter year 1800-2100! :  ')
        continue

    else :
        print(month, year)

    break


#determine month days
    if year == True :
        if (year % 4 == 0) and (not (year % 100 == 0) or (year % 400 == 0)) :
            leap_year = True
        else :
            leap_year = False


    year_month_even = [2, 4, 6, 8, 10, 12]
    year_month_odd = [1, 3, 5, 7, 9, 11]
    num_days_in_month = 0

    if month in year_month_even :
        num_days_in_month = 31

    elif month in year_month_odd :
        num_days_in_month = 30

    elif leap_year :
        num_days_in_mounth = 29

    else :
        num_days_in_month = 28


    #determine day of the week
    century_digits = year // 100
    year_digits = year % 100
    value = year_digits + (year_digits // 4)


    if century_digits == 18 :
        value = value + 2

    elif century_digits == 20 :
        value = value + 6



