# 1. tooted.json
# •	Leia, mitu erinevat tootekategooriat on failis esindatud.
# •	Leia kõige odavam ja kõige kallim toode ning nende hinnad.
# •	Leia, mitu toodet kuulub kategooriasse "Toidukaubad".
# •	Arvuta kõikide toodete koguväärtus laoseisu järgi.
# •	Leia kõik tooted, mille laoseis on alla 10 ühiku.

import requests

response = requests.get("https://www.metshein.com/kordamine/json/tooted.json")
data = response.json()
tooted = data["tooted"]
    
if response.status_code == 200:

    #Leian mitu erinevat tootekategooriat on failis esindatud

    def tootekategooriad():
        kategooriad = []
        unikaalsed_kategooriad = []

        for toode in tooted:
            kategooriad.append(toode["kategooria"])
            for toode in kategooriad:
                if toode not in unikaalsed_kategooriad:
                    unikaalsed_kategooriad.append(toode)
        print("Failis esindatud tootekategooriad:")
        print(unikaalsed_kategooriad)


    #Leian kõige odavama ja kõige kallima toote ning nende hinnad.

    def toote_hind():
        kallim_toode = tooted[0]
        odavaim_toode = tooted[0]
        for toode in tooted:
            if toode["hind"] > kallim_toode["hind"]:
                kallim_toode = toode
            if toode["hind"] < odavaim_toode["hind"]:
                odavaim_toode = toode

        print(f"Kallim toode on {kallim_toode["nimi"]} hinnaga {kallim_toode["hind"]}")
        print(f"Odavaim toode on {odavaim_toode["nimi"]} hinnaga {odavaim_toode["hind"]}")

    #Leian mitu toodet kuulub kategooriasse "Toidukaubad"
    def toidukaubad():
        toidukaubad = []

        for toode in tooted:
            if toode["kategooria"] == "Toidukaubad":
                toidukaubad.append(toode)

        print(f"{len(toidukaubad)} toodet kuulub kategooriasse 'Toidukaubad'")

    # Leian kõigi toodete koguväärtus laoseisu järgi
    def tootevaartused():    
        koguvaartus = 0

        for toode in tooted:
            vaartus = toode["hind"] * toode["laoseis"]
            koguvaartus += vaartus
        print(f"Kõigi toodete koguväärtus on {round(koguvaartus,2)}")

    # Leia kõik tooted, mille laoseis on alla 10 ühiku.
    def toodete_laoseis():
        tooted_alla_10 = []

        for toode in tooted:
            if toode["laoseis"] <= 10:
                tooted_alla_10.append(toode)
        print("Tooted mille laoseis on alla 10 ühiku:")
        print(tooted_alla_10)

    def vastus():
        while True:
            try:
                valik = int(input("Vali millised andmeid soovid kuvada (1,2,3,4,5): "))
                if valik == 1:
                    tootekategooriad()
                elif valik == 2: 
                    toote_hind() 
                elif valik == 3:
                    toidukaubad()
                elif valik == 4:
                    tootevaartused()
                elif valik == 5:
                    toodete_laoseis()
                else:
                    print("Viga sisestuses!")
            except:
                print("Viga sisestuses! Palun sisesta täisarv")
    vastus()
else:
    print(f"Päring ebaõnnestus {response.status_code}.")