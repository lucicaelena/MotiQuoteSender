from selenium import webdriver
from selenium.webdriver.common.by import By
import smtplib
import random
import datetime as dt


user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36 AVG/122.0.0.0"
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument(f"user-agent={user_agent}")
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
url = "https://*******" #insert url
driver.get(url)
quotes_class = driver.find_elements(By.ID,"truncationWrap")
motivational_quotes =[]
for element in quotes_class:
    quotes = element.find_elements(By.TAG_NAME, "li")
    for quote in quotes:
        quotes_text = quote.text
        motivational_quotes.append(quotes_text)

for motivational_quote in motivational_quotes:
    print(motivational_quote)

driver.quit()


sender_email = '*******'# insert email
password = '******'#insert your password from Gmail app (You need to log in to your account, then go to
# settings and search for "app",insert the name of the app and paste the password here)
recipient_email = '*****'#insert email

now = dt.datetime.now()
weekday = now.weekday()

if 0 <= weekday <= 4:
    random_quotes=random.choice(motivational_quotes).encode('utf-8')


    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=sender_email, password=password)
        connection.sendmail(
            from_addr=sender_email,
            to_addrs=recipient_email,
            msg=f"Subject:Motivational Quotes\n\n{random_quotes}.")
