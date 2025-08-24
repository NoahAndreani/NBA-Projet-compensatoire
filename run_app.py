#!/usr/bin/env python3
"""
Script de démarrage pour l'application NBA
"""

import os
import sys

def main():
    """Démarre l'application NBA"""
    print("🏀 Démarrage de l'application NBA...")
    print("📍 Pour arrêter l'application, utilisez Ctrl+C")
    print("🌐 L'application sera accessible sur: http://localhost:5000")
    print("=" * 50)
    
    # Définir les variables d'environnement par défaut
    os.environ.setdefault('FLASK_SECRET_KEY', 'dev-secret-key-change-in-production')
    os.environ.setdefault('FLASK_DEBUG', 'True')
    
    try:
        # Importer et lancer l'application
        from app import app, db
        
        # Créer les tables de base de données
        with app.app_context():
            db.create_all()
            print("✅ Base de données initialisée")
        
        # Démarrer l'application
        print("🚀 Démarrage du serveur...")
        app.run(debug=True, host='127.0.0.1', port=5000)
        
    except KeyboardInterrupt:
        print("\n👋 Arrêt de l'application...")
        sys.exit(0)
    except Exception as e:
        print(f"❌ Erreur lors du démarrage: {e}")
        print("\n💡 Assurez-vous que:")
        print("   - Toutes les dépendances sont installées (pip install -r requirements.txt)")
        print("   - Le port 5000 n'est pas utilisé par une autre application")
        sys.exit(1)

if __name__ == '__main__':
    main()
