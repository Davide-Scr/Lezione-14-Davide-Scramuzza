import random
minimo = int(input("Inserisci il valore minimo (0-100): "))
massimo = int(input("Inserisci il valore massimo (0-100): "))
contatore = 0
generati = []
while len(generati) < 10:
    num = random.randint(0, 100)
    contatore += 1
    if minimo <= num <= massimo:
        generati.append(num)
print(f"Numeri generati: {generati}")
print(f"Numeri totali generati: {contatore}")
