# _MotiQuoteSender_

#### This Python script scrapes motivational quotes from a website and sends a random quote via email only on weekdays (Monday to Friday).

#### Features
- Utilizes Selenium to scrape motivational quotes from a specified website.
- Sends a random motivational quote via email using Gmail SMTP.
- Customizable email sender, recipient, and URL of the website to scrape.


#### Usage
1. Open `main.py` in a text editor.
2. Configure the `sender_email`, `password`, and `recipient_email` variables with your Gmail credentials and recipient email address.
3. Replace the `url` variable with the URL of the website containing motivational quotes.
4. Run the script.

## Dependencies
- Selenium
- smtplib