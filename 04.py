# 4. ülesanne
# Aare 5.12.24

# 4.4
""""
Kingituste pakkimine
Sa töötad kingipoes ja sinu ülesanne on pakkida kingitusi.
Igasse kinkekarpi mahub täpselt 5 kingitust.
Sinu ülesandeks on arvutada, mitu täis kinkekasti saad teha ja mitu kingitust jääb üle, kui need kõik ei mahu karpidesse.
Loo programm, mis küsib kasutajalt, mitu kingitust on vaja pakkida.
Programm peaks seejärel arvutama, mitu täis kinkekasti saab teha ja mitu kingitust jääb üle. Kasuta täisarvulist jagamist (//) kinkekarpide arvu leidmiseks ja jäägi (%) operaatorit ülejäävate kingituste arvu leidmiseks.
Kasuta veakontrolli ja vastuse vormindamist
Näide:
Kasutaja sisestab: 23
Programm väljastab: Saad teha 4 täis kinkekasti. Üle jääb 3 kingitust. """

try:
    karbi_suurus = 5
    kingitused = int(input("Lisa kingituste arv: "))
    kastid = kingitused // karbi_suurus
    jaak = kingitused % karbi_suurus
    print(f"Saad teha {kastid} täis kinkekasti. Üle jääb {jaak} kingitust!")
except:
    print("Jälle tekitad probleeme!")
    


# 4.1
"""
Aia pikkus
Kirjuta programm, mis aitab aiapidajal arvutada aia ümbermõõtu.
Aed on ristküliku kujuline.
Programm peaks küsima kasutajalt kahe aiaosa pikkused meetrites ja seejärel arvutama aia kogupikkuse.
Väljasta lause, kasutades f-string vormindamist.
Näide:
Kasutaja sisestab: 4 ja 5
Programm väljastab: Aia kogupikkus on 18 meetrit.
"""

# int muudab a/b täisarvuks
a = int(input("Sisesta külg 1: "))
b = int(input("Sisesta külg 2: "))

ymbermoot = 2*(a+b)
print(f"Aia kogupikkus on {ymbermoot} meetrit. ")
