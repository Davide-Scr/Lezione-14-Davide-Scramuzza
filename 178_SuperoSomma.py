import random 
listanum = [random.randint(1, 100) for _ in range(20)]
soglia = int(input("Inserisci la somma da superare: "))
somma = 0
count = 0
for num in listanum:
    somma += num
    count += 1
    if somma >= soglia:
        break
print(f"Servono {count} numeri per superare la somma {soglia}.")

