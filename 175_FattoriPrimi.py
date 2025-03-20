num = int(input("Inserisci un numero da scomporre: "))
i = 2
fattori = []
while num > 1:
    while num % i == 0:
        fattori.append(i)
        num //= i
    i += 1
print(f"Fattori primi: {fattori}")
