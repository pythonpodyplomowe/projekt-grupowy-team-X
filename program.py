# v.1.0 dzialajacej aplikacji

wiek = input("Podaj wiek uzytkownika: ")
#sprawdzenie czy wiek jest liczba calkowitą
if wiek.isdigit() == False:
    exit("Wiek musi byc liczba calkowita. Zamykam aplikację")
wiek=int(wiek)
if wiek>=18 and wiek<=50:
    print("Witamy w apce. Mozesz kupować u nas energetyki")
elif wiek>50 and wiek<=130:
    print("Witamy w apce. Mozesz kupować u nas energetyki")
    print("Uwaga: Uwazaj na serce przy spozywaniu takich napojow")
elif wiek>130:
    print("Wiek nieprawidłowy. W tym wieku prawodopodbnie nie żyjesz ;)")
else:
    exit("Jestes za mlody/a na energetyki. Zapraszamy na disney.com:) ")
