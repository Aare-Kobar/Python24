	
# https://metshein.com/kordamine/?dir=./json
# Koosta programm, mis töötleb etteantud JSON-faile otse veebist. JSON-faile ära salvesta, vaid loe neid otse URL-i kaudu.
# Lahenda vähemalt 3 ülesandes kirjeldatud nõuet. Kirjuta selge ja loetav kood, kasuta asjakohaseid kommentaare ning muutujaid nimeta arusaadavalt.
# Esita oma töö GitHubi lingina.

# 3. uritused.json
# •	Leia, mitu üritust toimub Tallinnas.
# •	Leia kõik üritused, mis toimuvad pärast kellaaega 18:00.
# •	Leia kuu, kus toimub kõige rohkem üritusi.
# •	Leia kõige varasem ja kõige hilisem üritus kalendris.
# •	Loetle kõik üritused, mis toimuvad nädalapäeval "laupäev" või "pühapäev".
# ________________________________________

import requests

url = "https://www.metshein.com/kordamine/json/uritused.json"
response = requests.get(url)


if response.status_code == 200:
    data = response.json()

    uritused = data["uritused"]

    urituste_arv = data.count("Tallinn")

    for uritus in uritused:
        if (urituste_arv["koht"]) == "Tallinn":
            print(f"{urituste_arv} üritust toimub Tallinnas.")


else: 
    print(f"Päring ebaõnnestus. Staatuskood: {response.status_code}")