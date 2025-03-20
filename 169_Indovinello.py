import random
numero_casuale = random.randint(1, 100)
guess = -1
while guess != numero_casuale:
    guess = int(input("Indovina il numero tra 1 e 100: "))
    if guess < numero_casuale:
        print("Troppo basso!")
    elif guess > numero_casuale:
        print("Troppo alto!")
print("Complimenti! Hai indovinato.")
