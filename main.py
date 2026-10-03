##################### Extra Hard Starting Project ######################

#TODO 1. Update the birthdays.csv
    #Read from .csv using pandas
    #You will have the dataframe

#TODO 2. Check if today matches a birthday in the birthdays.csv
    #check from dataframe day and month

#TODO 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
    #use replace()
#TODO 4. Send the letter generated in step 3 to that person's email address.

import pandas as pd
import smtplib
import datetime as dt
import random
import os
from dotenv import load_dotenv
load_dotenv()

MY_EMAIL = os.environ.get("MY_EMAIL")
MY_PASSWORD = os.environ.get("MY_PASSWORD")

today = dt.datetime.now()
today_tuple = (today.month, today.day)

data = pd.read_csv("birthdays.csv")
birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}
if today_tuple in birthdays_dict:
    birthday_person = birthdays_dict[today_tuple]
    file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]", birthday_person["name"])

    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=birthday_person["email"],
            msg=f"Subject:Happy Birthday!\n\n{contents}"
        )
    print(f"Email sent to {birthday_person['name']}")
else:
    print("No birthdays today.")