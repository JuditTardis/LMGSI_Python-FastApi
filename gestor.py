### Imports ##################################################
import os
import json
### Variables ################################################
nom_fitxer = "alumnes.json"
alumnes = []
ultim_id = 0

### Funcions auxiliars #######################################

def carregar_fitxer():
    """
    Carrega els alumnes des del fitxer JSON i actualitza l'últim ID.
    """
    global alumnes, ultim_id
    try:
        with open(nom_fitxer, 'r', encoding='utf-8') as f:
            alumnes = json.load(f)
            ids = [a["id"] for a in alumnes]
            ultim_id = max(ids) if ids else 0
        print("Fitxer carregat correctament.")
    except FileNotFoundError:
        print("No s'ha trobat el fitxer. Es començarà amb la llista buida.")
        alumnes.clear()
    except json.JSONDecodeError:
        print("ERROR: Format del fitxer JSON incorrecte.")
        alumnes.clear()

def desar_fitxer():
    """
    Desa la llista d'alumnes actual al fitxer JSON.
    """
    with open(nom_fitxer, 'w', encoding='utf-8') as f:
        json.dump(alumnes, f, indent=4)
    print(f"Dades desades a {nom_fitxer}")

def generar_id():
    """
    Retorna un ID únic incrementant l’últim ID global.
    """
    global ultim_id
    ultim_id += 1
    return ultim_id


# Mostrar llistat reduït
def mostrar_llistat():
    """
    Mostra un llistat reduït amb ID, nom i cognom de cada alumne.
    """
    if not alumnes:
        print("No hi ha alumnes registrats.")
    else:
        for alumne in alumnes:
            print(f"{alumne['id']}: {alumne['nom']} {alumne['cognom']}")

def veure_alumne():
    """
    Mostra la informació detallada d’un alumne a partir del seu ID.
    """
    try:
        id_buscat = int(input("Introdueix l'ID de l'alumne: "))
        alumne = next((a for a in alumnes if a["id"] == id_buscat), None)
        if alumne:
            print(json.dumps(alumne, indent=4))
        else:
            print("Alumne no trobat.")
    except ValueError:
        print("ID invàlid. Ha de ser un número enter.")

# Afegeix un alumne nou
def afegir_alumne():
    """
    Demana dades per afegir un alumne nou i l’afegeix a la llista.
    """
    nom = input("Nom: ")
    cognom = input("Cognom: ")

    try:
        dia = int(input("Dia de naixement: "))
        mes = int(input("Mes de naixement: "))
        any = int(input("Any de naixement: "))
    except ValueError:
        print("Data invàlida.")
        return

    email = input("Email: ")
    feina = input("Treballa? (s/n): ").strip().lower() == 's'
    curs = input("Curs: ")

    nou_alumne = {
        "id": generar_id(),
        "nom": nom,
        "cognom": cognom,
        "data": {"dia": dia, "mes": mes, "any": any},
        "email": email,
        "feina": feina,
        "curs": curs
    }

    alumnes.append(nou_alumne)
    print(f"Alumne {nom} {cognom} afegit correctament amb ID {nou_alumne['id']}.")



def esborrar_alumne():
    """
    Esborra un alumne pel seu ID.
    """
    try:
        id_esborrar = int(input("ID de l'alumne a esborrar: "))
        alumne = next((a for a in alumnes if a["id"] == id_esborrar), None)
        if alumne:
            alumnes.remove(alumne)
            print("Alumne esborrat correctament.")
        else:
            print("No s'ha trobat cap alumne amb aquest ID.")
    except ValueError:
        print("ID invàlid. Ha de ser un número enter.")

# Menú principal
def menu():
    """
    Mostra el menú principal i retorna l'opció escollida.
    """
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Gestió d'alumnes - Institut TIC de Barcelona")
    print("--------------------------------------------")
    print("1. Mostrar alumnes")
    print("2. Afegir alumne")
    print("3. Veure alumne")
    print("4. Esborrar alumne")
    print("5. Desar a fitxer")
    print("6. Llegir fitxer")
    print("0. Sortir")
    return input("> ")

### Programa principal ########################################

if __name__ == "__main__":
    while True:
        opcio = menu()
        if opcio == "1":
            mostrar_llistat()
        elif opcio == "2":
            afegir_alumne()
        elif opcio == "3":
            veure_alumne()
        elif opcio == "4":
            esborrar_alumne()
        elif opcio == "5":
            desar_fitxer()
        elif opcio == "6":
            carregar_fitxer()
        elif opcio == "0":
            desar_fitxer()
            print("Fins aviat!")
            break
        else:
            print("Opció incorrecta.")
        input("\nPrem Enter per continuar...")