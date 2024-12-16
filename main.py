import sqlite3


conn = sqlite3.connect("phones.db")
cursor = conn.cursor()


cursor.execute('''
CREATE TABLE IF NOT EXISTS phones (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    brand TEXT NOT NULL,
    model TEXT NOT NULL,
    price REAL NOT NULL
)
''')
print("Table 'phones' créée avec succès.")


phones_data = [
    ("Apple", "iPhone 14", 999.99),
    ("Samsung", "Galaxy S22", 899.99),
    ("Google", "Pixel 7", 799.99)
]

cursor.executemany('INSERT INTO phones (brand, model, price) VALUES (?, ?, ?)', phones_data)
print("Données insérées avec succès.")


cursor.execute('SELECT * FROM phones')
rows = cursor.fetchall()

print("\nListe des téléphones :")
for row in rows:
    print(row)


conn.commit()
conn.close()

def add_phone(brand, model, price):
    cursor.execute("INSERT INTO phones (brand, model, price) VALUES (?, ?, ?)", (brand, model, price))
    conn.commit()
    print(f"{brand} {model} ajouté avec succès !")


def search_phone(brand=None, model=None):
    query = "SELECT * FROM phones WHERE"
    params = []

    if brand:
        query += " brand=?"
        params.append(brand)

    if model:
        if params:
            query += " AND"
        query += " model=?"
        params.append(model)

    cursor.execute(query, params)
    phones = cursor.fetchall()

    if phones:
        for phone in phones:
            print(phone)
    else:
        print("Aucun téléphone trouvé.")


def export_to_csv():
    cursor.execute('SELECT * FROM phones')
    phones = cursor.fetchall()

    with open('phones_export.csv', 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(['ID', 'Brand', 'Model', 'Price'])
        csv_writer.writerows(phones)

    print("Les données ont été exportées dans 'phones_export.csv'.")

def menu():
    while True:
        print("\n1. Ajouter un téléphone")
        print("2. Rechercher un téléphone")
        print("3. Exporter les données vers un fichier CSV")
        print("4. Quitter")
        choice = input("Choisissez une option: ")

        if choice == "1":
            brand = input("Entrez la marque: ")
            model = input("Entrez le modèle: ")
            price = float(input("Entrez le prix: "))
            add_phone(brand, model, price)
        elif choice == "2":
            brand = input("Entrez la marque à rechercher (ou laissez vide): ")
            model = input("Entrez le modèle à rechercher (ou laissez vide): ")
            search_phone(brand, model)
        elif choice == "3":
            export_to_csv()
        elif choice == "4":
            break
        else:
            print("Option invalide. Essayez à nouveau.")


menu()
def get_valid_price():
    while True:
        try:
            price = float(input("Entrez le prix: "))
            if price <= 0:
                print("Le prix doit être supérieur à 0.")
            else:
                return price
        except ValueError:
            print("Veuillez entrer un nombre valide pour le prix.")
def search_phone(brand=None, model=None):
    query = "SELECT * FROM phones WHERE"
    params = []

    if brand:
        query += " brand LIKE ?"
        params.append(f"%{brand}%")  
    if model:
        if params:
            query += " AND"
        query += " model LIKE ?"
        params.append(f"%{model}%")

    cursor.execute(query, params)
    phones = cursor.fetchall()

    if phones:
        for phone in phones:
            print(phone)
    else:
        print("Aucun téléphone trouvé.")
def delete_phone(phone_id):
    cursor.execute("DELETE FROM phones WHERE id = ?", (phone_id,))
    conn.commit()
    print(f"Le téléphone avec l'ID {phone_id} a été supprimé.")
