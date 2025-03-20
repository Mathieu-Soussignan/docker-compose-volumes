import psycopg2

# Connexion à la base de données
conn = psycopg2.connect(
    host="localhost",     # Le conteneur expose 5432 vers la machine hôte
    port=5432,
    user="myuser",        # POSTGRES_USER
    password="mypassword",# POSTGRES_PASSWORD
    database="mydb"       # POSTGRES_DB
)

# Création d'un curseur
cur = conn.cursor()

# Création de la table si elle n’existe pas
cur.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id SERIAL PRIMARY KEY,
        name VARCHAR(255) NOT NULL,
        age INTEGER
    )
""")

# Insertion de données
cur.execute("INSERT INTO users (name, age) VALUES (%s, %s)", ("Alice", 30))
cur.execute("INSERT INTO users (name, age) VALUES (%s, %s)", ("Bob", 25))

# Validation des changements
conn.commit()

# Fermeture du curseur et de la connexion
cur.close()
conn.close()

print("Données insérées dans la base de données.")