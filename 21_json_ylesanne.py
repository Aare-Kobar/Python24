	
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
from datetime import datetime
from collections import Counter
import calendar
import locale 
locale.setlocale(locale.LC_TIME, 'et_EE.UTF-8') 

url = "https://www.metshein.com/kordamine/json/uritused.json"
response = requests.get(url) # Funktsioon saadab HTTP GET päringu määratud URL-ile. Serveri vastus salvestatakse muutujasse.

if response.status_code == 200: # Kontrollib, kas HTTP vastuse olekukood on 200, mis tähendab, et päring oli edukas.
    data = response.json() # Võtab serverist saadud vastuse ja teisendab selle JSON-formaadist Python'i andmeteks

    uritused = data["uritused"] # Võtab sündmuste andmed JSON failist, kasutadaes võtmesõna "uritused"

    # Leian mitu üritust toimub Tallinnas
    tallinn_uritus = 0 # Ürituste arv mis toimub Tallinnas

    for uritus in uritused: # Tsükkel käib läbi kõik üritused
        if uritus["koht"] == "Tallinn":
            tallinn_uritus +=1 # Kui üritus toimub Tallinnas, siis suurendab tallinn_uritus loendurit ühe võrra

    print(f"{tallinn_uritus} üritust toimub Tallinnas")

    #Leian kõik üritused mis toimuvad pärast kellaaega 18:00.
    ohtused_uritused = [] # Loob tühja nimekirja hiliste ürituste jaoks

    for uritus in uritused:
        urituse_aeg = datetime.strptime(uritus["kellaaeg"], "%H:%M").time() # Teisendab kallaaja stringi datetime objektiks
        ohtu_aeg = datetime.strptime("18:00", "%H:%M").time() # Võtab kellaaja 18:00 võrdluseks
        
        if urituse_aeg > ohtu_aeg: # Kontrollib, kas üritus toimub pärast 18:00
            ohtused_uritused.append(uritus) # Lisab sobiva ürituse nimekirja

    print("Üritused pärast kellaaega 18:00:") # Kuvab kõik leitud õhtused üritused
    for uritus in ohtused_uritused:
        print(uritus)


    # Leian kuu, kus toimub kõige rohkem üritusi
    kuu_loendur = Counter() # Loendur kuude arvestamiseks

    for uritus in uritused:
        kuupaev = datetime.strptime(uritus["kuupäev"], "%Y-%m-%d") # Muudab ürituse kuupäeva datetime objektiks
        kuu_loendur[kuupaev.month] += 1 # Loendab üritusi iga kuu kohta
    
    koige_rohkem_uritusi_kuu, urituste_arv = kuu_loendur.most_common(1)[0] # Leiab kõige sagedamini esineva kuu ja ürituste arvu
    kuu_nimi = calendar.month_name[koige_rohkem_uritusi_kuu] # Teisendab kuu numbri nimeks

    print(f"Kõige rohkem üritusi toimub kuus {kuu_nimi} ({urituste_arv} üritust).")
    
else: 
    print(f"Päring ebaõnnestus. Staatuskood: {response.status_code}")