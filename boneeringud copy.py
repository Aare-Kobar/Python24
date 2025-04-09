# 2. broneeringud.json
# •	Leia, kui palju on broneeringuid teenusele "Massaaž".
# •	Leia kõik broneeringud, mis toimuvad pärast kella 12:00.
# •	Leia kliendid, kelle broneeringud on nädalavahetusel.
# •	Leia päev, millel on kõige rohkem broneeringuid.
# •	Loetle unikaalsed teenused ja mitu korda neid broneeriti.
from datetime import datetime
from collections import Counter
import requests

response = requests.get("https://www.metshein.com/kordamine/json/broneeringud.json")
data = response.json()
broneeringud = data["broneeringud"]

if response.status_code == 200:
    
# •	Leia, kui palju on broneeringuid teenusele "Massaaž".

    # massaaz_bron = []

    # for bronn in broneeringud:
    #     if bronn["teenus"] == "Massaaž":
    #         massaaz_bron.append(bronn)
    
    # print(f"{len(massaaz_bron)} broneeringuid on teenusele 'Massaaž'")

# •	Leia kõik broneeringud, mis toimuvad pärast kella 12:00.

    # piiraeg = datetime.strptime("12:00", "%H:%M")

    # for bronn in broneeringud:
    #     br_aeg = datetime.strptime(bronn["aeg"], "%H:%M")
    #     if br_aeg > piiraeg:
    #         print(bronn)

# •	Leia kliendid, kelle broneeringud on nädalavahetusel.

    # print("Kliendid, kelle broneeringud on nädalavahetusel:")
    
    # for bronn in broneeringud:
    #     kuupaev = datetime.strptime(bronn["kuupäev"], "%Y-%m-%d")
    #     if kuupaev.weekday() >= 5:
    #         print(bronn["klient"])

# •	Leia päev, millel on kõige rohkem broneeringuid.





# •	Loetle unikaalsed teenused ja mitu korda neid broneeriti.

    # unikaalsed_teenused = []
    # teenused = []
    # spa = []
    # kosmeetika = []
    # juuksur = []
    # massaaz = []

    # for bronn in broneeringud:
    #     teenused.append(bronn["teenus"])
        
    # for teenus in teenused:
    #     if teenus == "Kosmeetika":
    #         kosmeetika.append(teenus)
    #     if teenus == "Spa":
    #         spa.append(teenus)
    #     if teenus == "Juuksur":
    #         juuksur.append(teenus)
    #     if teenus == "Massaaž":
    #         massaaz.append(teenus)

    
    # print(f"{len(kosmeetika)} korda broneeriti kosmeetika teenust")


    teenuste_list = []

    for bronn in broneeringud:
        teenuste_list.append(bronn["teenus"])
    
    teenuste_statistika = Counter(teenuste_list)

    for teenus, teenuste_arv in teenuste_statistika.items():
        print(f"{teenus}: {teenuste_arv} broneeringut")

  


else:
    print(f"Päring ebaõnnestus {response.status_code}")   