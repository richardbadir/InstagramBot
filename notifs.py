from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import time
import re
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Initialize a web driver
driver = webdriver.Chrome()#executable_path="C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Google Chrome.lnk")

# Log in to Instagram
username = "username"
password = "password"
driver.get("https://www.instagram.com/accounts/login/")
time.sleep(2)  # Wait for the page to load

username_input = driver.find_element(By.NAME,"username")#, value="username")
password_input = driver.find_element(By.NAME,"password")

username_input.send_keys(username)
password_input.send_keys(password)
password_input.send_keys(Keys.RETURN)
time.sleep(5)  # Wait for the login to complete

# Navigate to the dms page 
driver.get("https://www.instagram.com/direct/inbox/")

# Wait for the notifications page to load
time.sleep(5)

# scrape
soup = BeautifulSoup(driver.page_source, "html.parser")

# Find and extract the title elements
messages = soup.find_all("title")

dms=messages[0]

integer_pattern = r'\d+'  # matches one or more digits

match = re.findall(integer_pattern, str(dms))

if match:
    number=''.join(match)
    #print(f"You have {number} new dm(s)!")
    # Email configuration
    sender_email = 'email@gmail.com'
    receiver_email = 'email@example.com'
    subject = 'New Instragram DM(s)'
    message = f'You have {number} new DM(s) on Instagram!'

    # SMTP server configuration (for Gmail)
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587  # Port for TLS (587 for Gmail)

    # Your email login credentials
    username = 'email@gmail.com'
    password = 'password'

    # Create a MIMEText object to represent the email
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject
    msg.attach(MIMEText(message, 'plain'))

    # Connect to the SMTP server and send the email
    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()  # Upgrade the connection to a secure TLS connection
        server.login(username, password)
        server.sendmail(sender_email, receiver_email, msg.as_string())
        print('Email sent successfully')
    except Exception as e:
        print(f'Error: {str(e)}')
    finally:
        server.quit()  # Close the SMTP server connection
    

# Close the browser
driver.quit()
