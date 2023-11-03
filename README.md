# WeatherAlert
Every morning, WeatherAlert sends you a personalized text message with the current temperature
in Orlando and how it feels outside. It also provides a tailored recommendation on whether or
not to wear a jacket, ensuring you step out prepared for the day's weather conditions.

Code Description:
The provided Python code is a script named "WeatherAlert" that combines various functionalities
to fetch weather data from the OpenWeatherMap API, process it, and send customized weather alerts
via email. Here's a detailed breakdown of its features:

API Integration:
The code establishes a connection to the OpenWeatherMap API, using a predefined API key
and specifying the location (Orlando) from which to fetch weather data from.

Temperature Conversion Functions:
Two functions convert temperatures from Kelvin to Fahrenheit. These functions are used to
process temperature data obtained from the API response.

API Request and Response Handling:
The code sends a request to the OpenWeatherMap API using the constructed URL and receives the
response in JSON format. It extracts temperature and "feels like" temperature values.

Email Alert Function (email_alert):
This function sends an email alert with a customizable subject, body, and recipient. It uses the
"smtplib" library for email/text functionality.

Weather Advisory Function:
This function provides a recommendation on whether to wear a jacket based on the "feels like"
temperature. If the temperature is below 68°F, it advises wearing a jacket.

Text Message:
This function combines the temperature data, "feels like" temperature, and jacket recommendation
into a message. It then sends this message as both a text message to a specified phone number and
prints it to the console.

Scheduling:
The code uses the schedule library to set up recurring tasks. It schedules the "text_send" function
to run at specific times on different days of the week. This ensures that weather alerts are sent
out regularly.

Continuous Execution:
The code enters a loop to continuously check and execute scheduled tasks. It sleeps for one second
between checks to avoid excessive CPU usage.

Usage:
This code serves as a personalized weather alert system. It fetches current weather data for Orlando 
from the OpenWeatherMap API, converts temperature values, provides recommendations on wearing a jacket, 
and sends customized alerts via email. The schedule module ensures that alerts are sent regularly at 
specified times, allowing the user to receive timely weather updates.
