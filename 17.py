# Pangakonto – pangakonto.txt
# Sinu ülesandeks on kirjutada Pythoni skript, mis loeb andmeid failist pangakonto.txt. 
# Fail sisaldab eraldi ridadel pangatehingute summasid: positiivsed summad tähistavad sissetulekuid ja negatiivsed summad väljaminekuid.
#  Skript peab arvutama ja väljastama:

# kogu tehingute arvu
# positiivsete tehingute arvu
# positiivsete tehingute kogusumma
# Tulemused tuleb väljastada konsooli

tehingute_arv = 0
tehingute_arv_pos = 0
pos_arv_summa = 0

with open("pangakonto.txt") as fail:
    sisu = fail.readlines()
    for number in sisu:
        tehingute_arv +=1
        if float(number) > 0:
            tehingute_arv_pos += 1
            pos_arv_summa += float(number)

print(f"Tehingute arv: {tehingute_arv} ")
print(f"Positiivsete tehingute arv: {tehingute_arv_pos}")
print(f"Positiivsete arvude summa {pos_arv_summa}")

# Palgastatistika – palgad.txt
# Kirjuta Pythoni skript, mis loeb failist palgad.txt töötajate andmed ja arvutab eraldi
# meeste keskmised töötunnid, töötasu ning palk
# naiste keskmised töötunnid, töötasu ning palk
# Tulemused prindi konsooli

mpalgad = 0

with open("palgad.txt") as fail:
    sisu = fail.readlines()
    for i in sisu:
        tykeldus = i.split(",")
        print(tykeldus[3])
        if tykeldus[3] == "Mees":
            mpalgad +=float(tykeldus[6])

print(f" Meeste palgad: {mpalgad:.2f}")
