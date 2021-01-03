import requests
from twilio.rest import Client


# ------------------------------------ CONSTANTS -------------------------- #
# FOR WEATHER
OMW_ENDPOINT = "https://api.openweathermap.org/data/2.5/onecall"
API_KEY = "2a41d0949ad5afb3918e55993e5069c8"
MY_LAT = 49.268790
MY_LONG = -122.738070

# FOR TEXT
ACCOUNT_SID = "AC844614f5dc6edd6132a988c6499f986d"
AUTH_TOKEN = "INSERT YOUR OWN AUTH TOKEN AFTER REGISTERING"
CODE_PHONENUMBER = "+16614898215"
RECEIVER_PHONENUMBER = INSERT YOUR OWN AUTH PHONE NUMBER"

# Uses the twilio api to send a text message
def send_message():
    client = Client(ACCOUNT_SID, AUTH_TOKEN)
    message = client.messages \
        .create(
        body="It will rain today. Keep an umbrella",
        from_=CODE_PHONENUMBER,
        to=RECEIVER_PHONENUMBER
    )

    print(message.status)

parameters = {
    "appid" : API_KEY,
    "lat" : MY_LAT,
    "lon" : MY_LONG,
    "exclude" : "current,minutely,daily"

}

# Uses the weather api to obtain the weather data 
response = requests.get(url=OMW_ENDPOINT, params= parameters)
response.raise_for_status()
weather_data = response.json()
# Slices the data to only next 12 hours
weather_data_slice = weather_data["hourly"][0:12]


will_rain = None

# Checks if there is rain in the next 12 hours
for hour_data in weather_data_slice:
    code = hour_data["weather"][0]["id"]
    if code < 700:
        will_rain = True
        
# Sends a text message if there is rain
if will_rain:
    send_message()
