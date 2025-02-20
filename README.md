## Table des matières:

- [Installation et Exécution de l'Application avec Docker Compose](#installation-et-exécution-de-lapplication-avec-docker-compose)
  - [Prérequis](#prérequis)
  - [Installation](#installation)
  - [Exécution](#exécution)
  - [Scripts Python](#scripts-python)
  - [Fichiers de Configuration](#fichiers-de-configuration)
  - [Instructions additionnelles](#instructions-additionnelles)
  - [Tester la persistance des données](#tester-la-persistance-des-données)
  - [🛠️ Built With](#️-built-with)
    - [Top contributors:](#top-contributors)
  - [📄 Licence](#-licence)
---

# Installation et Exécution de l'Application avec Docker Compose

Ce fichier README explique comment installer et exécuter l'application en utilisant Docker Compose et un environnement virtuel Python (`.venv`).

---


<p align="right">(<a href="#table-des-matières">back to top</a>)</p>

## Prérequis

Avant de commencer, assurez-vous d'avoir les éléments suivants installés :

*   **Docker:** [https://www.docker.com/](https://www.docker.com/)
*   **Docker Compose:** [https://docs.docker.com/compose/install/](https://docs.docker.com/compose/install/)
*   **Python 3:** [https://www.python.org/](https://www.python.org/)

<p align="right">(<a href="#table-des-matières">back to top</a>)</p>

## Installation

1.  **Cloner le dépôt:**

    ```bash
    git clone <URL_du_dépôt>
    cd <nom_du_dépôt>
    ```

2.  **Créer un environnement virtuel (recommandé):**

    ```bash
    python -m venv .venv
    ```

3.  **Activer l'environnement virtuel:**

    *   **Linux/macOS:**

        ```bash
        source .venv/bin/activate
        ```

    *   **Windows:**

        ```bash
        .venv\Scripts\activate
        ```

4.  **Installer les dépendances Python (si nécessaire):**

    Si votre application Python a des dépendances, installez-les dans l'environnement virtuel:

    ```bash
    pip install -r requirements.txt
    ```

<p align="right">(<a href="#table-des-matières">back to top</a>)</p>

## Exécution

1.  **Démarrer les conteneurs avec Docker Compose:**

    ```bash
    docker-compose up -d
    ```

    Cette commande va construire les images Docker (si nécessaire) et démarrer les conteneurs en arrière-plan.

2.  **(Optionnel) Peupler la base de données (si nécessaire):**

    Si votre application utilise une base de données et que vous avez besoin de l'initialiser avec des données, exécutez le script prévu à cet effet :

    ```bash
    python populate_db.py
    ```

3.  **Arrêter les conteneurs (quand vous avez terminé):**

    ```bash
    docker-compose down
    ```

<p align="right">(<a href="#table-des-matières">back to top</a>)</p>

## Scripts Python

*   **`create_tables_and_populate_db.py`:** Script pour initialiser ou ajouter des données à la base de données.
*   **`read_db.py`:** Script pour lire et afficher les données de la base de données.
*   **`populate_more_db.py`:** Script pour ajouter plus de donnéesdans les données de la base de données.

<p align="right">(<a href="#table-des-matières">back to top</a>)</p>

## Fichiers de Configuration

*   **`docker-compose.yml`:** Fichier de configuration pour Docker Compose.
*   **`init.sql`:** Script SQL pour l'initialisation de la base de données (création de la base et des tables).
     
<p align="right">(<a href="#table-des-matières">back to top</a>)</p>

## Instructions additionnelles

*   Pour consulter les logs des conteneurs :

    ```bash
    docker-compose logs <nom_du_service>
    ```

*   Pour lister les conteneurs en cours d'exécution :

    ```bash
    docker-compose ps
    ```
<p align="right">(<a href="#table-des-matières">back to top</a>)</p>

## Tester la persistance des données     


démarrer le conteneur : `docker-compose up` 

- lancer le script `create_tables_and_populate_db.py` pour créer les tables et insérer des données
- lancer le script `read_db.py` pour lire les données

redémarrer le conteneur :

- Pour arrêter le conteneur : `docker-compose down`
- Pour redémarrer le conteneur : `docker-compose up` 

tester la persistance des données

- lancer le script `read_db.py` pour vérifier la persistance des données dans le `volume`.  
- lancer le script `populate_more_db.py` puis lancer le script `read_db.py` pour lire les données

redémarrer le conteneur :

- Pour arrêter le conteneur : `docker-compose down`
- lancer le script `read_db.py` pour vérifier que la connection est impossible.  
- Pour redémarrer le conteneur : `docker-compose up` 

re tester la persistance des données
- lancer le script `read_db.py` pour vérifier la persistance des données dans le `volume`.  

**CQFD**

## 🛠️ Built With

<p align="left">

  <a href="https://www.python.org/" style="text-decoration: none;">
    <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  </a>

  <a href="https://www.postgresql.org/" style="text-decoration: none;">
    <img src="https://img.shields.io/badge/PostgreSQL-4169E1?style=for-the-badge&logo=postgresql&logoColor=white" alt="PostgreSQL">
  </a>
  <a href="https://www.docker.com/products/docker-desktop/" style="text-decoration: none;">
    <img src="https://img.shields.io/badge/Docker%20Compose-2496ED?style=for-the-badge&logo=docker&logoColor=white" alt="docker-desktop">

</p>
<p align="right">(<a href="#table-des-matières">back to top</a>)</p>

### Top contributors:

<a href="https://github.com/DeVerMyst/docker-compose-volumes/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=DeVerMyst/docker-compose-volumes" alt="contrib.rocks image" />
</a>


<p align="right">(<a href="#table-des-matières">back to top</a>)</p>

## 📄 Licence

Distribué sous la licence du projet. Voir le fichier `LICENSE.txt` pour plus d'informations.


<p align="right">(<a href="#table-des-matières">back to top</a>)</p>