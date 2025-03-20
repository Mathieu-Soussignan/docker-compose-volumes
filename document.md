# Documentation : Résolution des Problèmes de Persistance des Données avec PostgreSQL et Docker

## 1. Contexte et Problème Rencontré
L'objectif était de mettre en place un conteneur PostgreSQL avec Docker Compose tout en assurant la **persistance des données**.
Cependant, plusieurs problèmes ont été rencontrés :

1. **Erreur :** `FATAL: role "myuser" does not exist`
2. **Erreur :** `Did not find any relations` dans `psql` (aucune table trouvée)
3. **Les données disparaissaient après un redémarrage du conteneur**

Ces problèmes étaient causés par une mauvaise configuration de Docker et de PostgreSQL.

---

## 2. Diagnostic et Analyse des Problèmes

### **2.1. Erreur "role 'myuser' does not exist"**
Cette erreur survient lorsque PostgreSQL ne trouve pas l'utilisateur spécifié dans `POSTGRES_USER`.

#### **Vérification des logs du conteneur PostgreSQL**
Commande :
```bash
docker logs my_postgres_db
```
> **Problème trouvé :** L'utilisateur `myuser` n'avait pas été créé correctement lors de l'initialisation de la base.

#### **Solution appliquée :**
1. Suppression du volume Docker existant (il contenait des données incorrectes)
   ```bash
   docker-compose down -v
   ```
2. Redémarrage du conteneur avec le bon utilisateur PostgreSQL
   ```bash
   docker-compose up -d
   ```
3. Vérification de la présence de `myuser`
   ```bash
   docker exec -it my_postgres_db psql -U myuser -d mydb
   \\du  # Liste des utilisateurs PostgreSQL
   ```
   ✅ L'utilisateur `myuser` était bien créé après cette manipulation.

---

### **2.2. Problème : Aucune table n'existe dans la base**
#### **Diagnostic :**
Vérification dans `psql` :
```sql
\dt  # Liste des tables
```
> **Problème trouvé :** Le script `create_tables_and_populate_db.py` n'avait pas été exécuté ou avait échoué.

#### **Solution appliquée :**
1. **Lancer le script d'insertion des données**
   ```bash
   python create_tables_and_populate_db.py
   ```
2. **Vérifier dans PostgreSQL si la table est bien créée**
   ```sql
   \dt
   SELECT * FROM users;
   ```
✅ La table `users` était maintenant bien présente.

---

### **2.3. Problème : Les données disparaissent après redémarrage du conteneur**
#### **Diagnostic :**
1. Arrêt du conteneur PostgreSQL
   ```bash
   docker-compose down
   ```
2. Redémarrage du conteneur
   ```bash
   docker-compose up -d
   ```
3. Vérification des données
   ```sql
   SELECT * FROM users;
   ```
   > **Problème trouvé :** Les données avaient disparu, indiquant que PostgreSQL n'était pas configuré pour utiliser un volume Docker persistant.

#### **Solution appliquée :**
Ajout d'un volume persistant dans `docker-compose.yml` :

```yaml
services:
  database:
    image: postgres:13
    container_name: my_postgres_db
    environment:
      POSTGRES_USER: myuser
      POSTGRES_PASSWORD: mypassword
      POSTGRES_DB: mydb
    ports:
      - "5432:5432"
    volumes:
      - db_data:/var/lib/postgresql/data

volumes:
  db_data:
```

Vérification du volume existant :
```bash
docker volume ls
```
✅ Après cette correction, les données restaient bien en place après un redémarrage.

---

## 3. Conclusion

**Problèmes résolus :**
✅ `myuser` est bien créé au démarrage.
✅ Les tables sont bien créées et les scripts Python fonctionnent.
✅ Les données sont maintenant **persistantes** grâce à un volume Docker bien configuré.

### **Prochaines étapes possibles :**
- **Optimiser la sécurité** de PostgreSQL (authentification, règles d'accès)
- **Exposer PostgreSQL via une API Flask/FastAPI** pour accéder aux données
- **Automatiser l'insertion de données** via des fichiers CSV ou une API externe
- **Sauvegarder et restaurer la base de données** (pg_dump / pg_restore)

