import pandas as pd
import datetime as dt
import random
import smtplib

my_email = "loooksoook@gmail.com"
my_pass = "143Muller"
# 1. Update the birthdays.csv
PLACEHOLDER = "[NAME]"
data = pd.read_csv('birthdays.csv')
list_name = data['name'].tolist()
name = list_name[0]
list_month = data['month'].tolist()
month = list_month[0]
list_day = data['day'].tolist()
day = list_day[0]

letter1 = open('letter_templates/letter_1.txt')
letter1_new = letter1.read().replace(PLACEHOLDER, name)
letter2 = open('letter_templates/letter_2.txt')
letter2_new = letter2.read().replace(PLACEHOLDER, name)
letter3 = open('letter_templates/letter_3.txt')
letter3_new = letter3.read().replace(PLACEHOLDER, name)
letter = [letter1_new, letter2_new, letter3_new]

today = dt.datetime.now()
month_today = today.month
day_today = today.day

if month_today == month:
    if day_today == day:
        with open('quotes.txt') as quotes_file:
            rand_letter = random.choice(letter)
            print(rand_letter)
            with smtplib.SMTP('smtp.gmail.com') as connection:
                connection.starttls()
                connection.login(user=my_email, password=my_pass)
                connection.sendmail(from_addr=my_email, to_addrs='sonishkhanal@gmail.com',
                                    msg=f'Subject:Happy Birthday\n\n{rand_letter}')

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.




