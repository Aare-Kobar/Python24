# ÜLESANNE 11
# Kirjuta funktsioon pikim_sona(), mis võtab sisendiks sõnade listi ja tagastab pikima sõna pikkuse. Prindi tulemus konsooliaknasse.

# Kirjuta funktsioon nimega kolm_pikimat_sona(), mis analüüsib sõnade listi ja leiab kolm kõige pikemat sõna. Lisa kontroll juhuks, kui sõnade arv pole piisav.

# Kirjuta funktsioon, mis kontrollib, kas kahest sõnast koosnev sõne algab sama tähega.
# print(sarnased_esitahed('Vapper Vares')) # peaks tagastama True
# print(sarnased_esitahed('Lahe Känguru')) # peaks tagastama False

# Kilpkonn – kirjutada programm, mis lubab kasutajal valida kujundite tüübi (viisnurk, ring, ruut või suvaline) ja arvu. 
# Programm joonistab seejärel antud arvu kujundeid valitud tüübiga või juhul, kui valik on “suvaline”, valib programm ise juhuslikult kujundi tüübi iga kujundi jaoks.
# Millist kujundit soovid joonistada (viisnurk, ring, ruut, suvaline)? Suvaline
# Mitu kujundit soovid joonistada? 5

# [Joonistab 5 kujundit, igaüks juhuslikult valitud tüübiga suvalistesse kohtadesse]
# Pärast joonistamist peaks programm pakkuma võimalust sisestada uued väärtused või väljuda programmist, jättes sisendi tühjaks.

# def liitmine(a,b):
#     c = a + b
#     #print(c)
#     return c


# nr = 10
# nr2 = 20

# s = liitmine(liitmine(nr, nr2),100)
# print(s)
"""
def pikim_sona(s):
    sona = ""
    for i in s:
        if len(sona) < len(i):
            sona=i
    print(f"Pikim sõna on: "+sona)


sonad = ["vrk", "ring", "ruut", "su"]


pikim_sona(sonad)
"""
def viruvinkel(t1,t2):
    if t1[0]==t2[0]:
        return True
    else:
        return False

viruvinkel("Mario", "Mets")
print(viruvinkel("Mario", "Mets"))