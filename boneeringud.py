# 2. broneeringud.json
# •	Leia, kui palju on broneeringuid teenusele "Massaaž".
# •	Leia kõik broneeringud, mis toimuvad pärast kella 12:00.
# •	Leia kliendid, kelle broneeringud on nädalavahetusel.
# •	Leia päev, millel on kõige rohkem broneeringuid.
# •	Loetle unikaalsed teenused ja mitu korda neid broneeriti.
from datetime import datetime
import requests
from collections import Counter
response = requests.get("https://www.metshein.com/kordamine/json/broneeringud.json")
data = response.json()
broneeringud = data["broneeringud"]

if response.status_code == 200:
    
# •	Leia, kui palju on broneeringuid teenusele "Massaaž".

    # massaaz_bronn = []

    # for bronn in broneeringud:
    #     if bronn["teenus"] == "Massaaž":
    #         massaaz_bronn.append(bronn)
    # print(f"{len(massaaz_bronn)} broneeringuid on teenusele 'Massaaž'")

# •	Leia kõik broneeringud, mis toimuvad pärast kella 12:00.

    piiraeg = datetime.strptime("12:00", "%H:%M")

    print("Broneeringud mis toimuvad pärast '12:00': ")
    for bronn in broneeringud:
        bronn_aeg = datetime.strptime(bronn["aeg"], "%H:%M")
        if bronn_aeg > piiraeg:
            print(bronn)

# •	Leia kliendid, kelle broneeringud on nädalavahetusel.

    print("Kliendid, kelle broneering on nädalavahetusel:")

    for bronn in broneeringud:
        kuupaev = datetime.strptime(bronn["kuupäev"], "%Y-%m-%d")
        if kuupaev.weekday() >= 5:
            print(bronn["klient"])


#•	Leia päev, millel on kõige rohkem broneeringuid.


    kuupaevad = []

    for bronn in broneeringud:
        kuupaevad.append(bronn["kuupäev"])

    kuupaeva_statistika = Counter(kuupaevad)

    max_paev, max_arv = kuupaeva_statistika.most_common(1)[0]

    print(f"Kõige populaarsem päev on {max_paev}, millel on {max_arv} broneeringuid")

# •	Loetle unikaalsed teenused ja mitu korda neid broneeriti.

    # teenuste_list = []

    # for bronn in broneeringud:
    #     teenuste_list.append(bronn["teenus"])
    
    # teenuste_statistika = Counter(teenuste_list)

    # for x, y in teenuste_statistika.items():
    #     print(f"{x}: {y} broneeringuid")

    unikaalsed_teenused = []
    teenused = []
    spa = []
    kosmeetika = []
    juuksur = []
    massaaz = []

    for bronn in broneeringud:
        teenused.append(bronn["teenus"])
        
    for teenus in teenused:
        if teenus == "Kosmeetika":
            kosmeetika.append(teenus)
        if teenus == "Spa":
            spa.append(teenus)
        if teenus == "Juuksur":
            juuksur.append(teenus)
        if teenus == "Massaaž":
            massaaz.append(teenus)

    
    print(f"{len(kosmeetika)} korda broneeriti kosmeetika teenust")
    print(f"{len(spa)} korda broneeriti Spa teenust")

else:
    print(f"Päring ebaõnnestus {response.status_code}")   