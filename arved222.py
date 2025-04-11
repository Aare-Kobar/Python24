# 8. arved.json
# •	Leia makstud ja tasumata arvete arv.
# •	Leia kogusumma kõikidest makstud arvetest.
# •	Leia keskmine arvete summa.
# •	Leia, mitu arvet on maksetähtajaga järgmise 30 päeva jooksul.
# •	Loetle kõik tasumata arved, mille tähtaeg on juba möödunud.

import requests
from collections import Counter
import statistics
from datetime import datetime, timedelta


response = requests.get("https://www.metshein.com/kordamine/json/arved.json")
data = response.json()
arved = data["arved"]

# •	Leia makstud ja tasumata arvete arv.

# makstud_arved = []
# tasumata_arved = []

# for arve in arved:
#     if arve["makstud"] == False:
#         tasumata_arved.append(arve)
#     if arve["makstud"] == True:
#         makstud_arved.append(arve)

# print(f"Tasumata arvete arv on: {len(tasumata_arved)}")
# print(f"Makstud arvete arv on: {len(makstud_arved)}")

# •	Leia kogusumma kõikidest makstud arvetest.

arvete_summad = []

for arve in arved:
    if arve["makstud"] == True:
        arvete_summad.append(arve["summa"])

print(f"Kõikide makstud arvete kogusumma on: {sum(arvete_summad)}")

# •	Leia keskmine arvete summa.

koik_arve_summad = []

for arve in arved:
    koik_arve_summad.append(arve["summa"])

print(f" Keskmine arvete summa on {statistics.mean(koik_arve_summad)}")


# •	Leia, mitu arvet on maksetähtajaga järgmise 30 päeva jooksul.

# praegune_kuupaev = datetime.now()
# praegune_kuupaev_plus30 = praegune_kuupaev + timedelta(days=30)

# arved_maksetahtajaga_30 = []

# for arve in arved:
#     arve_tahtaeg = datetime.strptime(arve["tähtaeg"], "%Y-%m-%d")
#     if praegune_kuupaev < arve_tahtaeg < praegune_kuupaev_plus30:
#         arved_maksetahtajaga_30.append(arve["tähtaeg"])

# print(arved_maksetahtajaga_30)
# print(f" Arved mille maksetähtaeg on järgmise 30 päeva jooksul: {len(arved_maksetahtajaga_30)}")

# •	Loetle kõik tasumata arved, mille tähtaeg on juba möödunud.

tasumata_arved = []
tanane_kuupaev = datetime.now()

for arve in arved:
    if arve["makstud"] == False:
        tasumata_arved.append(arve["tähtaeg"])

print("Tasumata arved, mille tähtaeg on juba möödunud: ")
for arve in tasumata_arved:
    arve_kp = datetime.strptime(arve, "%Y-%m-%d")
    if arve_kp < tanane_kuupaev:
        print(arve_kp.strftime("%Y-%m-%d"))
      