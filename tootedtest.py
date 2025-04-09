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

    # Leian mitu erinevat tootekategooriat on failis esindatud
    
    unikaalsed_tootekategooriad = []
    tootekategooriad = []

    for toode in tooted:
        tootekategooriad.append(toode["kategooria"])    
        for toode in tootekategooriad:
            if toode not in unikaalsed_tootekategooriad:
                unikaalsed_tootekategooriad.append(toode)
    print(f"Failis esindatud tootekategooriad: {unikaalsed_tootekategooriad}")
   

    # #Leian kõige odavama ja kõige kallima toote ning nende hinnad.
    
    kallim_toode = tooted[0]
    odavaim_toode = tooted[0]

    for toode in tooted:
        if toode["hind"] > kallim_toode["hind"]:
            kallim_toode = toode
        if toode["hind"] < odavaim_toode["hind"]:
            odavaim_toode = toode

    print(f"Kõige kallim toode on {kallim_toode["nimi"]} hinnaga {kallim_toode["hind"]}")
    print(f"Kõige odavam toode on {odavaim_toode["nimi"]} hinnaga {odavaim_toode["hind"]}")

    # #Leian mitu toodet kuulub kategooriasse "Toidukaubad"

    toidukaubad = []

    for toode in tooted:
        if toode["kategooria"] == "Toidukaubad":
            toidukaubad.append(toode)

    print(f"{len(toidukaubad)} toodet kuulub kategooriasse 'Toidukaubad'")

    # Leian kõigi toodete koguväärtus laoseisu järgi
    
    vaartused = []

    for toode in tooted:
        vaartus = toode["hind"] * toode["laoseis"]
        vaartused.append(vaartus)
        
    koguvaartus = sum(vaartused)
    print(f"Kõigi toodete koguvaartus on: {koguvaartus}")
    

    # Leia kõik tooted, mille laoseis on alla 10 ühiku.

#     tooted_alla_10 = []

#     for toode in tooted:
#         if toode["laoseis"] <= 10:
#             tooted_alla_10.append(toode)
#     print("Kõik tooted mille laoseis on alla 10 ühiku:")
#     print(tooted_alla_10)


else:
    print(f"Päring ebaõnnestus {response.status_code}")

