import smtplib
import datetime as dt
import random

my_email = "pythontestberry@gmail.com"
# password from app generator on gmail
password = "dluhzayjhamxzxbj"
other_email = "berrypythontest@yahoo.com"

with open("./quotes.txt") as quotes:
    quotes_txt = quotes.readlines()
    # get current date and time
    now = dt.datetime.now()
    day_of_week = now.weekday()
    random_quote = random.choice(quotes_txt)
    # if day_of_week equals Monday(0) then it will automatically send a random quote to the email
    if day_of_week == 0:
        # connect to smtp provider
        with smtplib.SMTP("smtp.gmail.com") as connection:
            # start transport layer security to secure the connection to the email server
            connection.starttls()
            # login process
            connection.login(user=my_email, password=password)
            # sending the email from one address to the other with message...adding subject and /n to make
            # sure it doesn't go into spam box
            connection.sendmail(from_addr=my_email, to_addrs=other_email,
                                msg=f"Subject:Motivational Monday\n\n{random_quote}")










