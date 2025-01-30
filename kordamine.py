# Iseseisev Töö 1
# 1.1 - Koostada programm, mis väljastaks ekraanile teksti Tere, maailm! täpselt sellisel kujul - koma ja hüüumärgiga.

"""print("Tere, maailm!")"""

# 1.2. Aasta liblikas
# Koostada programm, mille
# 1. real luuakse muutuja nimega aasta ning antakse sellele väärtuseks 2020 (arvuna);
# 2. real luuakse muutuja nimega liblikas ning antakse sellele väärtuseks "teelehe-mosaiikliblikas" (sõnena);
# 3. real luuakse muutuja nimega lause_keskosa ning antakse sellele väärtuseks ". aasta liblikas on " (sõnena);
# 4. real luuakse muutuja nimega lause, mille väärtuse saamiseks ühendatakse üheks sõnaks muutujad aasta, lause_keskosa ja liblikas (vajadusel tuleb kasutada funktsiooni, mis teisendab arvu sõneks);
# 5. real väljastatakse muutuja lause väärtus ekraanile.
"""
aasta = 2020
liblikas = "teelehe-mosaiikliblikas"
lause_keskosa = ". aasta liblikas on "
lause = str(aasta) + lause_keskosa + liblikas
print(lause)
"""
# 1.3. Pilved
# Pilvede alumise pinna (aluse) kõrguse järgi liigitatakse pilvi ülemise, keskmise ja alumise kihi pilvedeks. 
# Ülemiste pilvede alus on kõrgemal kui 6 km, keskmistel pilvedel on 2-6 km kõrgusel, alumistel pilvedel on madalamal kui 2 km. Koostada programm, mis
# - küsib kasutajalt pilvede aluse kõrgust (kilomeetrites),
# - väljastab ekraanile Need on ülemised pilved, kui sisestatu on üle 6,0 km,
# - väljastab Need ei ole ülemised pilved, kui kõrgus on 6,0 km või alla selle.
# Kasutaja peab saama sisestada pilvede kõrgust nii täisarvuna kui ka ujukomaarvuna, nt 7.5.
"""
korgus =float(input("Siseta pilvede kõrgus: "))
if korgus > 6:
    print("Ülemised")
elif korgus >= 2 and korgus <= 6:
    print("Keskmised")
else:
    print("Alumised")
print(korgus)"""

# 1.4. Bussid
# Meil on vaja transportida teatud arv inimesi mingi arvu identsete bussidega. Eeldame, et reisijaid on vähemalt üks. 
# Koostada programm, mis küsib transporditavate inimeste arvu ja ühe bussi kohtade arvu (just sellises järjekorras) 
# ning väljastab ekraanile, mitu bussi on vaja ja mitu inimest on viimases bussis (eeldusel, et kõik eelnevad bussid on täis).
# Võib-olla on abi nendest tehetest
# // täisarvuline jagamine, 36 // 10 → 3
# % jäägi leidmine 36 % 10 → 6
# Testige oma programmi muuhulgas järgmiste algandmetega:
# inimeste arv: 60, kohtade arv: 40;
# inimeste arv: 80, kohtade arv: 40;
# inimeste arv: 20, kohtade arv: 40;
# inimeste arv: 40, kohtade arv: 40.
# Püüdke ka mõista, miks just sellised testandmed valiti.
"""
import math
inimesed = 80
koht = 40

jaak = inimesed%koht

if jaak > 0:
    busside_arv = (inimesed // koht) + 1
else:
    busside_arv = (inimesed // koht)

if jaak == 0:
    jaak = koht

print(f"Busside arv: {busside_arv}")
print(f"Viimases bussis on inimesi: {jaak}")

"""

#2.1 Äratus 
# Küsib kasutajalt, mitu korda äratus heliseb ning
# väljastab sama arv kordi ekraanile Tõuse ja sära!.
"""
kordadearv = int(input("Kordade arv: "))

for _ in range(kordadearv):
    print("Tõuse ja sära!")
else:
    print("Viga")
"""
# 2.2 MURELIKUD LAPSEVANEMAD
# Jänesevanemad on mures, et lapsed ei liigu piisavalt. 
# Laste motiveerimiseks mõtlesid nad välja süsteemi, kus 2. metsaringi läbimisel saab jänesepoeg 2 porgandit, 
# 4. metsaringi läbimisel 4 porgandit juurde, 6. metsaringi läbimisel 6 porgandit juurde jne. Paarituarvulistel ringidel porgandeid juurde ei saa. 
# Koostada programm, mis küsib kasutajalt ringide arvu (mittenegatiivne täisarv);
# arvutab while-tsükli abil saadavate porgandite koguarvu;
# väljastab saadavate porgandite koguarvu ekraanile.
""""
porgandid = 0
Ringide_arv = 6

while Ringide_arv > 0:
    #print(Ringide_arv)
    if Ringide_arv % 2 == 0:
        porgandid += Ringide_arv
    Ringide_arv = Ringide_arv - 1

print(porgandid)
"""
#2.5 ÕUNAD
#Lumivalgekesel oli 14 õuna ja ta tahtis neid pöialpoistega jagada. 
# Ta sai aru, et kui kõik seitse pöialpoissi tahavad õunu ja ta annaks kõigile kaks õuna, jääks ta ise üldse ilma. 
# Nüüd otsustas ta õunu jagada nii, et küsib, mitu pöialpoissi tahab õunu, ja seejärel loosib iga soovija korral, kas anda talle üks või kaks õuna. 
# Koostada programm, mis
# - küsib kasutajalt, mitu pöialpoissi tahab õunu (võib eeldada, et sisestatakse täisarv lõigust [0; 7]);
# - leiab ja väljastab eraldi ridadele, mitu õuna saab iga pöialpoiss (programm genereerib iga kord juhuslikult arvu 1 või 2);
# - leiab ja väljastab eraldi reale, mitu õuna jääb Lumivalgekesele.
"""
import random
ounad = 14
pp = int(input("Mitu PP tahab õuna: "))

for i in range(pp):
    suv_oun = random.randint(1,2)
    print(suv_oun)
    ounad -= suv_oun

print(f"Lumivalgekesele jäi {ounad} õuna.")
"""
#3.1 Ülikooli vastuvõetud
# Ülikooli I õppeastmesse (bakalaureuseõpe jm) võetakse igal aastal vastu sadu inimesi. 
# Viimastel aastatel vastuvõetud inimeste arvud on aastate kaupa failis rebased.txt, kus esimesel real on 2011. aastal vastuvõetute arv, teisel real 2012. aastal vastuvõetute arv kuni viimasel real on 2019. aastal vastuvõetute arv. 
# Koostada programm, mis
# - loeb failist registreeritud vastuvõetute andmed aastate järgi järjendisse;
# - Failist järjendisse saab lugeda järgmise programmijupi abil:

# küsib kasutajalt aastat
# võib eeldada, et sisestatakse täisarv, mis kuulub lõiku [2011; 2019].
# väljastab, mitu inimest sel aastal vastu võeti.
"""
fail = open("rebased.txt", encoding="UTF-8")
vastuvõetud = []

for rida in fail:
    #print(rida,end="")
    vastuvõetud.append(int(rida))

fail.close

aasta = input("Lisa aasta 2011-2019: ")
print(aasta[3])
print(vastuvõetud[int(aasta[3])-1])
"""

# 3.3 Sissetulekud
# Failis konto.txt on kirjas ujukomaarvudena pangakonto tehingud (kus positiivsed arvud on sissetulekud ja negatiivsed arvud on väljaminekud). 
# Iga arv on eraldi real. Tekstifaili kasutamiseks programmi sees peab fail asuma programmifailiga samas kaustas.
# Koostada programm, mis
# loeb failist nimega konto.txt andmed;
# väljastab ekraanile kõik sissetulekud ehk failist leitud positiivsed arvud. 
# Iga arv peab olema eraldi real ja positiivsete arvude omavaheline järjekord peab jääma samaks nagu failis. 
"""
fail = open("konto.txt", encoding="UTF-8")

for kirje in fail:
    if float(kirje) > 0:
        print(float(kirje), end="\n")


fail.close()
"""

# 3.4 Jukebox
# Ada tahab valida plaadiautomaadist laulu ja uurib, milliseid laule masin mängib. Muusikapalad on kirjas failis, kus iga laul on eraldi real.
# Programmi testimiseks kasutatakse järgmisi faile, mida võite salvestada või koostada ise mõne tekstiredaktoriga (nt Notepad):
#  - jukebox.txt
#  - 80ndad.txt
#  - eesti_muusika.txt 
#  - edm.txt
# Koostada programm, mis
# küsib kasutajalt failinime (kasutaja sisestab failinime koos laiendiga, nt jukebox.txt);
# loeb sisestatud nimega failist andmed;
# näitab kõiki laule koos järjekorranumbritega (alates 1);
# küsib kasutajalt, mitmendat laulu ta soovib (kasutaja sisestab alati täisarvu);
# väljastab ekraanile vastavalt valitud arvule muusikapala

#Näita kõiki lugusid

musa = "edm.txt"
fail = open(musa, encoding="UTF-8")
nr = 1
for track in fail:
    print(str(nr)+". "+track, end="")
    nr+=1

# Kuva valitud lugu

print()
fail = open(musa, encoding="UTF-8")
valik = int(input("Vali lugu: "))
fail.seek(0)
mangin = 1
for track in fail:
    if valik == mangin:
        print(f" Mängin lugu: ",track, end="")
    mangin+=1

fail.close()
