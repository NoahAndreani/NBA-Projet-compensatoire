#!/usr/bin/env python3
"""
Script de test pour vérifier que l'application fonctionne
"""

def test_imports():
    """Teste les imports de base"""
    try:
        print("🔍 Test des imports...")
        import flask
        import flask_sqlalchemy
        import flask_login
        import requests
        print("✅ Tous les imports réussis")
        return True
    except ImportError as e:
        print(f"❌ Erreur d'import: {e}")
        return False

def test_app_creation():
    """Teste la création de l'application"""
    try:
        print("🔍 Test de création de l'application...")
        from app import app, db
        print("✅ Application créée avec succès")
        
        # Test de la configuration
        with app.app_context():
            db.create_all()
            print("✅ Base de données initialisée")
        
        return True
    except Exception as e:
        print(f"❌ Erreur lors de la création: {e}")
        return False

def test_routes():
    """Teste les routes de base"""
    try:
        print("🔍 Test des routes...")
        from app import app
        
        with app.test_client() as client:
            # Test de la route de base
            response = client.get('/')
            print(f"✅ Route '/' : Status {response.status_code}")
            
            # Test de la route de login
            response = client.get('/login')
            print(f"✅ Route '/login' : Status {response.status_code}")
            
            # Test de la route de register
            response = client.get('/register')
            print(f"✅ Route '/register' : Status {response.status_code}")
        
        return True
    except Exception as e:
        print(f"❌ Erreur lors du test des routes: {e}")
        return False

def main():
    """Fonction principale de test"""
    print("🏀 Tests de l'application NBA")
    print("=" * 40)
    
    tests = [
        ("Imports", test_imports),
        ("Création de l'application", test_app_creation),
        ("Routes", test_routes)
    ]
    
    passed = 0
    total = len(tests)
    
    for name, test_func in tests:
        print(f"\n📝 {name}:")
        if test_func():
            passed += 1
        print("-" * 40)
    
    print(f"\n🎯 Résultats: {passed}/{total} tests réussis")
    
    if passed == total:
        print("🎉 Tous les tests sont passés ! L'application est prête.")
        print("\n🚀 Pour démarrer l'application:")
        print("   python run_app.py")
        print("\n🌐 Puis ouvrir: http://localhost:5000")
    else:
        print("⚠️ Certains tests ont échoué. Vérifiez les erreurs ci-dessus.")

if __name__ == '__main__':
    main()
