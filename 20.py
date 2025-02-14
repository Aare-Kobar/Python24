# Ülesanne 20
# Hetke temperatuur

# Loo Pythoni programm, mis küsib kasutajalt linnanime ja kasutades OpenWeatherMap API-d, kuvab vastava linna hetketemperatuuri Celsius kraadides
# Programm peab sisaldama vigade käsitlemist, näiteks kui linn ei ole leitav, päringule pole vastust ja kui API võti on vale
# Veendu, et programm suudab käidelda ka sisestatud linnanimede erinevaid kirjapilte
# Näiteks:

# Sisesta soovitud linn: talliNN
# Hetke temperatuur: Tallinn 5°C

# minu võti 9a99df0bdcb3f176b3e15effa0395a93

import requests

# API võtme ja linna nime määramine
city = "Haapsalu"
api_key = "9a99df0bdcb3f176b3e15effa0395a93"
url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

# API päringu tegemine
response = requests.get(url)

# Vastuse kontrollimine
if response.status_code == 200:
    data = response.json()
    weather = data['weather'][0]['description']
    temperature = data['main']['temp']
    print(f"Ilma kirjeldus: {weather}")
    print(f"Temperatuur: {temperature} °C")
else:
    print("Viga andmete allalaadimisel:", response.status_code)
