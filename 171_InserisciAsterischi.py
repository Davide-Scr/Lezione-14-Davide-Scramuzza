conta_asterischi = 0
totale = 0
while conta_asterischi < 10:
    carattere = input("Inserisci un carattere: ")
    totale += 1
    if carattere == "*":
        conta_asterischi += 1
print(f"Numero totale di caratteri inseriti: {totale}")
