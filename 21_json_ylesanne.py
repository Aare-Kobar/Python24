	
# https://metshein.com/kordamine/?dir=./json
# Koosta programm, mis töötleb etteantud JSON-faile otse veebist. JSON-faile ära salvesta, vaid loe neid otse URL-i kaudu.
# Lahenda vähemalt 3 ülesandes kirjeldatud nõuet. Kirjuta selge ja loetav kood, kasuta asjakohaseid kommentaare ning muutujaid nimeta arusaadavalt.
# Esita oma töö GitHubi lingina.

# 4. raamatud.json
# •	Leia, mitu raamatut ilmus enne 2000. aastat.
# •	Leia kõik raamatud, mis pole saadaval.
# •	Leia vanim raamat andmestikus.
# •	Leia žanr, mida esineb andmetes kõige sagedamini.
# •	Leia, mitu raamatut on välja antud pärast aastat 2010.

import requests

url = "https://www.metshein.com/kordamine/json/uritused.json"
response = requests.get(url)


if response.status_code == 200:
    data = response.json()
    uritused = data.get("uritused")



    for i in uritused:
        if i
        else:


else: 
    print(f"Viga! Ei suutnud andmeid laadida. Staatuskood: {response.status_code}")