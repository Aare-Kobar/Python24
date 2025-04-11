# 8. arved.json
# •	Leia makstud ja tasumata arvete arv.
# •	Leia kogusumma kõikidest makstud arvetest.
# •	Leia keskmine arvete summa.
# •	Leia, mitu arvet on maksetähtajaga järgmise 30 päeva jooksul.
# •	Loetle kõik tasumata arved, mille tähtaeg on juba möödunud.
from datetime import datetime, timedelta
import requests

response = requests.get("https://www.metshein.com/kordamine/json/arved.json")
data = response.json()
arved = data["arved"]

if response.status_code == 200:

# •	Leia makstud ja tasumata arvete arv.
    def makstud_tasumata_arved():
        makstud_arved = []
        tasumata_arved = []

        for arve in arved:
            if arve["makstud"] == False:
                tasumata_arved.append(arve["makstud"])
            if arve["makstud"] == True:
                makstud_arved.append(arve["makstud"])

        print(f" Tasumata arvete arv on: {len(tasumata_arved)}")
        print(f" Makstud arvete arv on: {len(makstud_arved)}")

# •	Leia kogusumma kõikidest makstud arvetest.
    def makstud_arvete_kogusumma():
        makstud_arvete_summad = []
        for arve in arved:
            if arve["makstud"] == True:
                makstud_arvete_summad.append(arve["summa"])
    
        print(f"Kõikide arvete kogusumma on: {sum(makstud_arvete_summad)}")

# •	Leia keskmine arvete summa.
    def keskmine_arvete_summa():
        import statistics

        arvete_summad = []

        for arve in arved:
            arvete_summad.append(arve["summa"])
            
        print(f"Keskmine arvete summa on: {statistics.mean(arvete_summad)}")

# •	Leia, mitu arvet on maksetähtajaga järgmise 30 päeva jooksul.
    def arved_maksetahtajaga30():
        tanane_kuupaev = datetime.now()
        piir_kuupaev = tanane_kuupaev + timedelta(days=30)
        
        arved_maksetahtajaga_30 = []

        for arve in arved:
            arve_kp = datetime.strptime(arve["tähtaeg"], "%Y-%m-%d")
            if tanane_kuupaev < arve_kp < piir_kuupaev:
                arved_maksetahtajaga_30.append(arve)
                
        print(f"{len(arved_maksetahtajaga_30)} arvet on maksetähtajaga järgmise 30 päeva jooksul")

# •	Loetle kõik tasumata arved, mille tähtaeg on juba möödunud.
    def moodunud_tahtaeg():
        print("Kõik tasumata arved, mille tähtaeg on möödunud:")
        tanane_kuupaev = datetime.now()
        tasumata_arved = []
        for arve in arved:
            if arve["makstud"] == False:
                tasumata_arved.append(arve)
        for arve in tasumata_arved:
            arve_kp = datetime.strptime(arve["tähtaeg"], "%Y-%m-%d")
            if arve_kp < tanane_kuupaev:
                print(arve)
    
    def kood():
        while True:
            try:
                valik = int(input("Vali arv et kuvada andmed (1,2,3,4,5):"))
                if valik == 1:
                    makstud_tasumata_arved()
                elif valik == 2:
                    makstud_arvete_kogusumma()
                elif valik == 3:
                    keskmine_arvete_summa()
                elif valik == 4:
                    arved_maksetahtajaga30()
                elif valik == 5:
                    moodunud_tahtaeg()
                else:
                    print("Viga! sisesta täisarv")
            except:
                print("Viga! sisesta täisarv")
    kood()

else:
    print(f"Päring ebaõnnestus: {response.status_code}")