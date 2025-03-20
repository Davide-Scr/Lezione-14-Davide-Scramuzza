import random
listanum = [random.randint(1, 100) for _ in range(20)]
n = int(input("Quanti numeri pari vuoi copiare? "))
listapari = [x for x in listanum if x % 2 == 0][:n]
print(f"Lista numeri pari: {listapari}")
