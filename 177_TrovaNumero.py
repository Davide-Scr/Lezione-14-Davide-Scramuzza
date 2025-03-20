import random
listanum = [random.randint(1, 100) for _ in range(20)]
target = int(input("Inserisci un numero da cercare: "))
if target in listanum:
    print(f"Numero trovato dopo {listanum.index(target)} elementi.")
else:
    print(f"Numero non presente. La lista ha {len(listanum)} elementi.")
