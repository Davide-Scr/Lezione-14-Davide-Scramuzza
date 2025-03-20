import random
num_pari = int(input("Inserisci il numero di numeri pari da generare: "))
generati = []
totale = 0
while len(generati) < num_pari:
    num = random.randint(40, 90)
    totale += 1
    if num % 2 == 0:
        generati.append(num)
print(f"Numeri generati: {generati}")
print(f"Totale numeri generati: {totale}")
