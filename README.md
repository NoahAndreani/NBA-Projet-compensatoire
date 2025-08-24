# NBA App - Projet Compensatoire B2

Une application web Flask pour consulter les données NBA via l'API BallDontLie.

## 🏀 Fonctionnalités

- **Authentification** : Système de connexion et création de compte
- **Joueurs** : Liste et détails des joueurs NBA
- **Équipes** : Liste et détails des équipes NBA  
- **Matchs** : Liste et détails des matchs NBA

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
   python app.py
   ```

5. **Accéder à l'application**
   - Ouvrir votre navigateur sur `http://localhost:5000`
   - Créer un compte ou se connecter

## 📁 Structure du projet

```
NBA-Projet-compensatoire/
├── app.py                 # Application Flask principale
├── requirements.txt       # Dépendances Python
├── env_example.txt       # Exemple de configuration
├── README.md             # Documentation
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
3. **Joueurs** : Consulter la liste des joueurs et cliquer pour voir les détails
4. **Équipes** : Consulter les équipes et leurs joueurs
5. **Matchs** : Voir les matchs et leurs détails

## ⚠️ Notes importantes

- L'API BallDontLie peut avoir des limitations de taux
- Certaines données peuvent ne pas être disponibles pour tous les éléments
- L'application fonctionne en mode local (pas d'hébergement requis)

## 🎯 Projet réalisé dans le cadre

**Ynov Basket – Projet Compensatoire B2**

Application développée pour répondre aux exigences du projet compensatoire, permettant d'afficher, trier et utiliser efficacement les données de l'API BallDontLie dans une interface web moderne et intuitive.
