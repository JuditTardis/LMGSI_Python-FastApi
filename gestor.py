import json

# Llista d'alumnes en memòria
alumnes = []
# ID inicial
id_actual = 1

# Carrega el fitxer JSON, si existeix
def carregar_alumnes():
    global alumnes, id_actual
    try:
        with open("alumnes.json", "r", encoding="utf-8") as fitxer:
            alumnes = json.load(fitxer)
            # Troba l'id més alt per continuar des d'allà
            if alumnes:
                id_actual = max(alumne["id"] for alumne in alumnes) + 1
    except FileNotFoundError:
        alumnes = []

# Desa els alumnes al fitxer JSON
def desar_alumnes():
    with open("alumnes.json", "w", encoding="utf-8") as fitxer:
        json.dump(alumnes, fitxer, indent=4)

# Mostrar llistat reduït
def mostrar_llistat():
    print("\nLlistat d’alumnes:")
    for alumne in alumnes:
        print(f"{alumne['id']}: {alumne['nom']} {alumne['cognom']}")

# Afegeix un alumne nou
def afegir_alumne():
    global id_actual
    nom = input("Nom: ")
    cognom = input("Cognom: ")
    dia = int(input("Dia de naixement: "))
    mes = int(input("Mes de naixement: "))
    any = int(input("Any de naixement: "))
    email = input("Email: ")
    feina = input("Té feina? (s/n): ").lower() == 's'
    curs = input("Curs: ")

    nou_alumne = {
        "id": id_actual,
        "nom": nom,
        "cognom": cognom,
        "data": {
            "dia": dia,
            "mes": mes,
            "any": any
        },
        "email": email,
        "feina": feina,
        "curs": curs
    }

    alumnes.append(nou_alumne)
    print(f"Alumne amb id {id_actual} afegit correctament.")
    id_actual += 1

# Mostrar detalls d’un alumne per id
def veure_alumne():
    id_cercat = int(input("ID de l’alumne: "))
    for alumne in alumnes:
        if alumne["id"] == id_cercat:
            print(json.dumps(alumne, indent=4))
            return
    print("Alumne no trobat.")

# Esborrar alumne per id
def esborrar_alumne():
    id_esborrar = int(input("ID de l’alumne a esborrar: "))
    for alumne in alumnes:
        if alumne["id"] == id_esborrar:
            alumnes.remove(alumne)
            print("Alumne esborrat correctament.")
            return
    print("No s’ha trobat cap alumne amb aquest ID.")

# Menú principal
def menu():
    carregar_alumnes()
    while True:
        print("\n1. Mostrar alumnes")
        print("2. Afegir alumne")
        print("3. Veure alumne")
        print("4. Esborrar alumne")
        print("5. Desar fitxer")
        print("6. Sortir")

        opcio = input("Opció: ")
        if opcio == '1':
            mostrar_llistat()
        elif opcio == '2':
            afegir_alumne()
        elif opcio == '3':
            veure_alumne()
        elif opcio == '4':
            esborrar_alumne()
        elif opcio == '5':
            desar_alumnes()
        elif opcio == '6':
            desar_alumnes()
            print("Sortint del programa.")
            break
        else:
            print("Opció no vàlida.")

if __name__ == "__main__":
    menu()
