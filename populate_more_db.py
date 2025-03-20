import psycopg2
import time

time.sleep(5)  # Optionnel : donne à PostgreSQL le temps de se lancer

conn = psycopg2.connect(
    host="localhost",
    port=5432,
    user="myuser",
    password="mypassword",
    database="mydb"
)

cur = conn.cursor()

# Insertion de nouvelles données
cur.execute("INSERT INTO users (name, age) VALUES (%s, %s)", ("Charlie", 40))
cur.execute("INSERT INTO users (name, age) VALUES (%s, %s)", ("David", 35))

conn.commit()
cur.close()
conn.close()

print("Nouvelles données insérées dans la base de données.") # noqa