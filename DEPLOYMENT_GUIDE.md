# 🚀 Guide de déploiement sur Render

## ✅ Prérequis (DÉJÀ FAIT !)

Ton projet est déjà prêt pour le déploiement ! Voici ce qui a été préparé :

- ✅ `Procfile` créé
- ✅ `requirements.txt` à jour
- ✅ `app.py` configuré pour la production
- ✅ Code pushé sur GitHub

## 🎯 Étapes de déploiement sur Render

### **Étape 1 : Créer un compte Render**

1. Va sur [render.com](https://render.com)
2. Clique sur **"Get Started for Free"**
3. Connecte-toi avec ton compte **GitHub**

### **Étape 2 : Créer un nouveau Web Service**

1. Sur le dashboard Render, clique **"New +"**
2. Sélectionne **"Web Service"**
3. Connecte ton repository GitHub **"NBA-Projet-compensatoire"**
4. Clique **"Connect"**

### **Étape 3 : Configuration du service**

Remplis les champs suivants :

- **Name**: `nba-app-[ton-nom]` (ex: `nba-app-jus2raisins`)
- **Region**: `Frankfurt (EU Central)`
- **Branch**: `main`
- **Root Directory**: (laisser vide)
- **Runtime**: `Python 3`
- **Build Command**: `pip install -r requirements.txt`
- **Start Command**: `python app.py`

### **Étape 4 : Variables d'environnement**

Dans la section **"Environment Variables"**, ajoute :

1. **BALLDONTLIE_API_KEY**
   - Value: `[ta-clé-api-balldontlie]`

2. **FLASK_SECRET_KEY** 
   - Value: `[génère-une-clé-secrète-longue]`

3. **FLASK_ENV**
   - Value: `production`

### **Étape 5 : Déploiement**

1. Clique **"Create Web Service"**
2. Attendre 5-10 minutes le déploiement
3. Ton site sera accessible sur `https://nba-app-[ton-nom].onrender.com`

## 🔧 Si tu as des erreurs

### Erreur de base de données
- Render utilise un système de fichiers temporaire
- La base de données SQLite sera recréée à chaque redémarrage
- C'est normal pour un projet de test !

### Erreur d'API
- Vérifie que ta clé API BallDontLie est correcte
- Assure-toi qu'elle n'a pas expiré

### Erreur de build
- Vérifie que `requirements.txt` est à jour
- Tous les packages doivent être listés

## 🎉 Une fois déployé

Ton site NBA sera accessible 24h/24 sur Internet !

- URL: `https://nba-app-[ton-nom].onrender.com`
- Gratuit jusqu'à 750 heures/mois
- Se réveille automatiquement quand quelqu'un visite
- Peut être lent au premier chargement (normal)

## 🔄 Mettre à jour

Pour mettre à jour ton site :

1. Modifie ton code localement
2. `git add .`
3. `git commit -m "Mise à jour"`
4. `git push`
5. Render redéploiera automatiquement !

---

**🎯 Résumé rapide :**
1. Créer compte Render
2. Connecter GitHub repo
3. Configurer les variables d'environnement
4. Déployer
5. Profiter de ton site en ligne ! 🚀
