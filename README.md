# Garage Auto - Système de Gestion de Garage Automobile à Madagascar

## Description
Garage Auto est une application web Django conçue pour gérer efficacement les opérations d'un garage automobile à Madagascar. Elle permet la gestion des services, des rendez-vous, des véhicules et du personnel, avec des prix affichés en Ariary. 
**Cette application nécessite une connexion internet pour charger toutes les images en ligne.**

## Fonctionnalités Principales

- Gestion des services de garage
- Prise de rendez-vous en ligne
- Gestion des véhicules des clients
- Interface d'administration pour le personnel du garage
- Page d'accueil présentant les services et avantages du garage
- Page de contact

## Technologies Utilisées

- Python 3.8+
- Django 3.2+
- Tailwind CSS 2.2.19
- HTML5
- SQLite (base de données par défaut)
- Alpine.js pour les interactions côté client

## Prérequis

- Python 3.8 ou supérieur
- pip (gestionnaire de paquets Python)
- virtualenv (recommandé)
- Django 3.2 ou supérieur

## Installation

1. Clonez le dépôt : git clone https://github.com/Tsiveriasy/GarageAuto.git

2. Accédez au répertoire du projet

3. Preparez un environnement virtuel

4. Créez des superuser pour les administrateurs :
   - python manage.py createsuperuser

6. Appliquez les migrations de base de données :
    - python manage.py makemigrations
    - python manage.py migrate


7. Démarrez le serveur de développement :
    python manage.py runserver


## Usage

Ouvrez votre navigateur et accédez à `http://127.0.0.1:8000` pour voir l'application en action. Utilisez l'interface d'administration à `http://127.0.0.1:8000/admin` pour gérer les services, rendez-vous, véhicules et personnel.
