risposta = ""
n = 1
while risposta.lower() != "no":
    print(f"Il quadrato di {n} è {n**2}")
    risposta = input("Vuoi continuare? ")
    n += 1
