# 6. tootajad.json
# •	Leia ametikoht, mida esineb kõige rohkem.
# •	Leia kõige kõrgema ja kõige madalama palgaga töötaja.
# •	Arvuta ettevõtte keskmine töötajate palk.
# •	Loetle töötajad, kes töötavad IT-osakonnas.
# •	Leia kõik töötajad, kelle nimi algab tähega "M".
from collections import Counter
import requests

response = requests.get("https://www.metshein.com/kordamine/json/tootajad.json")
data = response.json()
tootajad = data["tootajad"]

# •	Leia ametikoht, mida esineb kõige rohkem.

ametid = []

for tootaja in tootajad: 
    ametid.append(tootaja["amet"])
    
ameti_statistika = Counter(ametid)

max_amet, max_arv = ameti_statistika.most_common(1)[0]

print(f" Kõige populaarsem ametikoht on {max_amet} mis esineb {max_arv} korda")

# •	Leia kõige kõrgema ja kõige madalama palgaga töötaja.

# kõrgem_palk = tootajad[0]
# madalam_palk = tootajad[0]

# for tootaja in tootajad:
#     if tootaja["palgatase"] > kõrgem_palk["palgatase"]:
#         kõrgem_palk = tootaja
#     if tootaja["palgatase"] < madalam_palk["palgatase"]:
#         madalam_palk = tootaja

# print(kõrgem_palk)
# print(madalam_palk)

# •	Arvuta ettevõtte keskmine töötajate palk.

import statistics

palgad = []

for tootaja in tootajad:
    palgad.append(tootaja["palgatase"])

print(f"Töötajate keskmine palk on {statistics.mean(palgad)}")

    

# •	Loetle töötajad, kes töötavad IT-osakonnas.

print("Töötajad kes töötavad IT-osakonnas:")
for tootaja in tootajad:
    if tootaja["osakond"] == "IT":
        print(tootaja["nimi"])


# •	Leia kõik töötajad, kelle nimi algab tähega "M".

print(f"Tootajad kelle nimi algab 'M' tähega")
for tootaja in tootajad:
    if tootaja["nimi"].endswith("M"):
        print(tootaja["nimi"])