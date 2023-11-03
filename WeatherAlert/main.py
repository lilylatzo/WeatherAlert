import smtplib
from email.message import EmailMessage
import requests
import schedule
import time
import signal

# Connects "Open Weather Map" API to code
BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"
API_KEY = "7bb30a8063bad3db86e5590017e194fa"
CITY = "Orlando"


# Converts Kelvin (given temperature by OWM) to Fahrenheit
def kevlin_to_fahrenheit(temp_kelvin):
    temp_celsius = temp_kelvin - 273.15
    temp_fahrenheit = temp_celsius * (9 / 5) + 32
    return temp_fahrenheit


# Converts "feels like" Kelvin (given temperature by OWM) to "feels like" Fahrenheit
def feels_like_kelvin_to_fahrenheit(feels_like_temp_kelvin):
    temp_celsius = feels_like_temp_kelvin - 273.15
    temp_fahrenheit = temp_celsius * (9 / 5) + 32
    return temp_fahrenheit


#
url = BASE_URL + "appid=" + API_KEY + "&q=" + CITY
response = requests.get(url).json()

# Sets the temperature to a variable, then calls the Fahrenheit funtion to convert it
kelvin = response['main']['temp']
fahrenheit = int(kevlin_to_fahrenheit(kelvin))
fahrenheit_string = str(fahrenheit)

# Sets the "feels like" temperature to a variable, then calls the "feels like" Fahrenheit funtion to convert it
feels_like_kelvin = response['main']['feels_like']
feels_like_fahrenheit = int(feels_like_kelvin_to_fahrenheit(feels_like_kelvin))
feels_like_fahrenheit_string = str(feels_like_fahrenheit)


# Function to calculate if I should wear a jacket or not
def wear_jacket(feels_like):
    if feels_like < 68:
        return "You should wear a jacket today."
    else:
        return "You should not wear a jacket today."


# Function to connect my email to send out the messages
def email_alert(to, subject, body):
    # Declares variables and portions of the message
    msg = EmailMessage()
    msg.set_content(body)
    msg['subject'] = subject
    msg['to'] = to

    # Links the admin email account with the program
    user = "latzoproject@gmail.com"

    msg['from'] = user

    password = "xsjy ggws qkcj ifxp"

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(user, password)
    server.send_message(msg)
    server.quit()


# Funtion to print and send out the message
def text_send():
    # Texts the message to my phone
    email_alert("7272886899@vzwpix.com", "Weather Alert",
                "Good morning Lily, the temperature outside right now is " + fahrenheit_string + ". It feels like " + feels_like_fahrenheit_string + ". " + wear_jacket(
                    feels_like_fahrenheit))
    # Prints the message to the console
    print(
        f"Good morning Lily, the temperature outside right now is {fahrenheit}. It feels like {feels_like_fahrenheit}. {wear_jacket(feels_like_fahrenheit)}")
    # This allows me to stop the code from having "Keyboard Interrupt" errors if I want to stop the code
    signal.signal(signal.SIGINT, signal.SIG_IGN)


# Main funtion
if __name__ == '__main__':
    # Runs the text send function
    text_send()

# Schedules the text to send every day at 10am
# Besides on Mondays and Wednesdays when I have class at 9am
schedule.every().sunday.at("09:55").do(text_send)
schedule.every().monday.at("07:55").do(text_send)
schedule.every().tuesday.at("09:55").do(text_send)
schedule.every().wednesday.at("07:55").do(text_send)
schedule.every().thursday.at("09:55").do(text_send)
schedule.every().friday.at("09:55").do(text_send)
schedule.every().saturday.at("09:55").do(text_send)

while 1:
    schedule.run_pending()
    time.sleep(1)
