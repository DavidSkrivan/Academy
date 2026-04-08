mesta = ["Praha", "Viden", "Olomouc", "Svitavy"]

ceny = (150, 200, 100, 180)

oddelovac = 36 * "*"

nabidka = """
1 - Praha   | 150
2 - Viden   | 200
3 - Olomouc | 100
4 - Svitavy | 180
"""

print("Vitejte v nasi aplikaci")
print("Vyberte si z nasledujicich destinaci")
print(oddelovac)
print(nabidka)
print(oddelovac)

destinace = input("Vyberte cislo destinace: ")

if destinace.isnumeric() and int(destinace) <= 4: 
    destinace_cislo = int(destinace)
    zvolena_cena = ceny[destinace_cislo - 1]
    print(zvolena_cena)
else:
    print("Nevlozili jste cislo")

print("Od ted Git")

    