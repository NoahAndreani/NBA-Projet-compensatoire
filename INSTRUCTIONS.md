# 🏀 Instructions d'utilisation - NBA App

## 🚀 Démarrage rapide

### 1. Installation
```bash
# Installer les dépendances
pip install -r requirements.txt
```

### 2. Lancement de l'application
```bash
# Option 1: Script de démarrage (recommandé)
python run_app.py

# Option 2: Démarrage direct
python app.py
```

### 3. Accès à l'application
- Ouvrir votre navigateur
- Aller sur: **http://localhost:5000**

## 📋 Première utilisation

### 1. Création de compte
- Cliquer sur "Créer un compte"
- Choisir un nom d'utilisateur (4 caractères minimum)
- Choisir un mot de passe (6 caractères minimum)
- Confirmer le mot de passe

### 2. Connexion
- Utiliser vos identifiants créés
- Vous serez redirigé vers la page des joueurs (page d'accueil)

## 🧭 Navigation

### Menu principal
- **Joueurs** : Liste de tous les joueurs NBA
- **Équipes** : Liste de toutes les équipes NBA  
- **Matchs** : Liste de tous les matchs NBA

### Fonctionnalités par page

#### 🏀 Joueurs
- **Liste** : Cartes avec nom et prénom de chaque joueur
- **Détail** : Cliquer sur une carte pour voir :
  - Informations personnelles (taille, poids, position, etc.)
  - Carte de l'équipe (cliquable)

#### 🏟️ Équipes
- **Liste** : Cartes avec nom de chaque équipe
- **Détail** : Cliquer sur une carte pour voir :
  - Informations de l'équipe (ville, conférence, division)
  - Liste des joueurs de l'équipe (cartes cliquables)

#### 🏀 Matchs
- **Liste** : Cartes avec "ÉQUIPE vs ÉQUIPE" et date
- **Détail** : Cliquer sur une carte pour voir :
  - Score du match (si disponible)
  - Informations détaillées
  - Cartes des deux équipes (cliquables)

## 🔑 Configuration API (Optionnel)

Pour accéder aux vraies données de l'API BallDontLie :

1. **Obtenir une clé API**
   - Aller sur https://www.balldontlie.io/
   - Créer un compte gratuit
   - Obtenir votre clé API

2. **Configuration**
   - Copier `env_example.txt` vers `.env`
   - Remplacer `your-api-key-here` par votre vraie clé
   - Redémarrer l'application

## ⚠️ Notes importantes

### Limitations de l'API
- L'API gratuite a des limitations de taux
- Certaines données peuvent être indisponibles
- En cas d'erreur API, l'application affiche un message d'erreur

### Performance
- Le chargement des joueurs d'une équipe peut prendre du temps
- La pagination est disponible pour les grandes listes
- L'application fonctionne entièrement en local

### Résolution de problèmes

#### L'application ne démarre pas
```bash
# Vérifier les dépendances
python test_app.py

# Réinstaller les dépendances
pip install -r requirements.txt --force-reinstall
```

#### Port déjà utilisé
- Fermer les autres applications sur le port 5000
- Ou modifier le port dans `run_app.py`

#### Problèmes de base de données
- Supprimer le fichier `nba_app.db`
- Redémarrer l'application

## 🎯 Fonctionnalités complètes

### ✅ Implémenté
- [x] Système d'authentification complet
- [x] Page Joueurs avec liste et détails
- [x] Page Équipes avec liste et détails
- [x] Page Matchs avec liste et détails
- [x] Navigation fluide entre toutes les pages
- [x] Interface responsive avec Bootstrap
- [x] Gestion des erreurs API
- [x] Pagination pour les grandes listes

### 📱 Interface
- Design moderne avec Bootstrap 5
- Cartes cliquables avec animations
- Navigation intuitive
- Messages d'erreur informatifs
- Responsive design (mobile/desktop)

## 🏆 Projet réalisé

**Ynov Basket – Projet Compensatoire B2**

Cette application répond à toutes les exigences du projet :
- ✅ Formulaire de login et création de compte
- ✅ Accès restreint aux utilisateurs connectés
- ✅ Menu de navigation en haut de page
- ✅ Page Joueurs (homepage) avec cartes nom/prénom
- ✅ Page Équipes avec cartes nom d'équipe
- ✅ Page Matchs avec cartes "ÉQUIPE vs ÉQUIPE + date"
- ✅ Pages détaillées pour chaque élément
- ✅ Navigation croisée entre joueurs/équipes/matchs
- ✅ Utilisation de l'API BallDontLie
- ✅ Technologies autorisées (Python/Flask)
