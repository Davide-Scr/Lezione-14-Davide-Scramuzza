somma = 0
n = int(input("Inserisci un numero (0 per terminare): "))
while n != 0:
    somma += n
    n = int(input("Inserisci un numero (0 per terminare): "))
print(f"Somma complessiva: {somma}")
