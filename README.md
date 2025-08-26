# NBA App - Projet Compensatoire B2

Une application web Flask pour consulter les données NBA via l'API BallDontLie.

## 🏀 Fonctionnalités

- **Authentification** : Système de connexion et création de compte
- **Joueurs** : Liste et détails complets des joueurs NBA avec toutes leurs statistiques
- **Équipes** : Liste et détails des équipes NBA avec leurs joueurs
- **Matchs** : Liste et détails des matchs NBA avec navigation complète
- **🔍 Recherche avancée** : 
  - Recherche de joueurs par nom ou prénom
  - Recherche d'équipes par nom, ville ou abréviation  
  - Recherche de matchs par date (plusieurs formats supportés)
- **📱 Interface moderne** : Design responsive avec Bootstrap 5
- **🧭 Navigation intelligente** : Système de curseur pour parcourir toutes les données
- **📊 Informations détaillées** : Positions expliquées, données draft, universités, etc.

## 🚀 Installation

1. **Cloner le projet**
   ```bash
   git clone <url-du-projet>
   cd NBA-Projet-compensatoire
   ```

2. **Installer les dépendances**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configuration de l'API**
   - Créer un compte sur [BallDontLie](https://www.balldontlie.io/)
   - Obtenir votre clé API
   - Créer un fichier `.env` basé sur `env_example.txt`
   - Remplacer `your-api-key-here` par votre vraie clé API

4. **Lancer l'application**
   ```bash
   python run_app.py
   ```
   ou
   ```bash
   python app.py
   ```

5. **Accéder à l'application**
   - Ouvrir votre navigateur sur `http://localhost:5000`
   - Créer un compte ou se connecter

## 📁 Structure du projet

```
NBA-Projet-compensatoire/
├── app.py                 # Application Flask principale
├── run_app.py            # Script de démarrage recommandé
├── test_app.py           # Tests de l'application
├── requirements.txt       # Dépendances Python
├── .env                  # Configuration API (à créer)
├── env_example.txt       # Exemple de configuration
├── README.md             # Documentation
├── INSTRUCTIONS.md       # Guide d'utilisation détaillé
└── templates/            # Templates HTML
    ├── base.html         # Template de base
    ├── login.html        # Page de connexion
    ├── register.html     # Page d'inscription
    ├── players.html      # Liste des joueurs
    ├── player_detail.html # Détail d'un joueur
    ├── teams.html        # Liste des équipes
    ├── team_detail.html  # Détail d'une équipe
    ├── games.html        # Liste des matchs
    └── game_detail.html  # Détail d'un match
```

## 🔧 Technologies utilisées

- **Backend** : Flask (Python)
- **Base de données** : SQLite avec SQLAlchemy
- **Authentification** : Flask-Login
- **Frontend** : Bootstrap 5
- **API** : BallDontLie NBA API

## 📝 Utilisation

1. **Connexion** : Créer un compte ou se connecter
2. **Navigation** : Utiliser le menu pour naviguer entre les sections
3. **🔍 Recherche** : 
   - **Joueurs** : Rechercher par prénom ou nom (ex: "Stephen", "Curry")
   - **Équipes** : Rechercher par nom, ville ou abréviation (ex: "Lakers", "Boston", "GSW")
   - **Matchs** : Rechercher par date (ex: "2024-01-15", "15/01/2024")
4. **📊 Détails** : Cliquer sur les cartes pour voir les informations complètes
5. **🧭 Navigation** : Utiliser "Suivant" pour parcourir toutes les données disponibles

## ⚠️ Notes importantes

- L'API BallDontLie peut avoir des limitations de taux (5 requêtes par minute en gratuit)
- Certaines données peuvent ne pas être disponibles pour tous les éléments
- L'application fonctionne en mode local (pas d'hébergement requis)
- Pour plus de détails, consulter `INSTRUCTIONS.md`

## 🎮 Fonctionnalités avancées

- **Positions expliquées** : G (Guard/Meneur), F (Forward/Ailier), C (Center/Pivot)
- **Données complètes** : Université, pays, année de draft, position de draft
- **Navigation croisée** : Cliquer sur une équipe depuis un joueur, etc.
- **Interface responsive** : Fonctionne sur mobile et desktop
- **Recherche intelligente** : Préserve les filtres lors de la navigation

## 🎯 Projet réalisé dans le cadre

**Ynov Basket – Projet Compensatoire B2**

Application développée pour répondre aux exigences du projet compensatoire, permettant d'afficher, trier et utiliser efficacement les données de l'API BallDontLie dans une interface web moderne et intuitive.
