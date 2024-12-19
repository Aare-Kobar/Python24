# 19.12.24
# Kobar


nimi = ["Jyri Pootsman","Mari Jyrgens","Ansambel Maali","Terminaator - Juulikuus lumi on maas"]

#print(nimi[3])
#for i in nimi:
#    print(i)

for i in range(4):
    print(f"{i+1}. {nimi[i]}")
    
valik = int(input("Vali lugu (1-4): "))
print(f"Mängin: {nimi[valik-1]}")

except:
    print("Viga sisestuses!")




    
    