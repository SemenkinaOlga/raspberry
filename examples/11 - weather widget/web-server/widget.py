import requests, json
 
url = "http://api.openweathermap.org/data/2.5/forecast"

keyFileName = "openweathermap_api_key.txt"
keyFile = open(keyFileName, "r")
key = keyFile.read()
 
payload = {
    "lat": "56",
    "lon": "92",
    "units": "celsius",
    "appid": key,
}
 
res = requests.get(url, params=payload)
data = json.loads(res.text)
 
weather = data["list"][0]
 
 
def pars_weather(weatherType, timeRange, measurementUnits):
    if (weatherType in weather) and (
        timeRange in weather[weatherType].keys()
    ):
        print(
            weatherType,
            ": ",
            weather[weatherType][timeRange],
            measurementUnits,
        )
    else:
        print(weatherType, ": ", "none")
 
 
pars_weather("clouds", "all", "%")
pars_weather("rain", "3h", "mm")
pars_weather("snow", "3h", "mm")
print("temp:", weather["main"]["temp"], "C")