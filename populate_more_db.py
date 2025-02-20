import psycopg2
import time

time.sleep(5)

conn = psycopg2.connect(
    host="localhost", # ou "database" si le script est dans un conteneur sur le même réseau docker
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

print("Nouvelles données insérées dans la base de données.")