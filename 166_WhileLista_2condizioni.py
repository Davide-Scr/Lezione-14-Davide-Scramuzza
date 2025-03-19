lista_numeri = []
risposta = ""
while risposta != "no" and len(lista_numeri) < 5:
    n = int(input("Inserisci numero: "))
    lista_numeri.append(n)
    if len(lista_numeri) < 5:  
        risposta = input("Vuoi inserire altri numeri? ")

print(lista_numeri)
