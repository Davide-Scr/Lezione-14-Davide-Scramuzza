password_corretta = "segreta"
attempts = 0
while attempts < 3:
    password = input("Inserisci la password: ")
    if password == password_corretta:
        print("Accesso consentito!")
        break
    else:
        attempts += 1
        print("Password errata.")
if attempts == 3:
    print("Accesso negato!")
