from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, EqualTo
import requests
import os
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('FLASK_SECRET_KEY', 'your-secret-key-here')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///nba_app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'
login_manager.login_message = 'Vous devez vous connecter pour accéder à cette page.'

# API Configuration
API_BASE_URL = 'https://api.balldontlie.io/v1'
API_KEY = os.getenv('BALLDONTLIE_API_KEY', 'your-api-key-here')

# Debug: afficher la clé API (seulement les premiers caractères pour la sécurité)
print(f"🔑 Clé API chargée: {API_KEY[:10]}..." if len(API_KEY) > 10 else f"🔑 Clé API: {API_KEY}")

# Models
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(120), nullable=False)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Forms
class LoginForm(FlaskForm):
    username = StringField('Nom d\'utilisateur', validators=[DataRequired()])
    password = PasswordField('Mot de passe', validators=[DataRequired()])
    submit = SubmitField('Se connecter')

class RegisterForm(FlaskForm):
    username = StringField('Nom d\'utilisateur', validators=[DataRequired(), Length(min=4, max=20)])
    password = PasswordField('Mot de passe', validators=[DataRequired(), Length(min=6)])
    password2 = PasswordField('Confirmer le mot de passe', 
                             validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Créer le compte')

# API Helper Functions
def make_api_request(endpoint, params=None):
    """Effectue une requête à l'API BallDontLie"""
    headers = {}
    if API_KEY != 'your-api-key-here':
        # Nouveau format d'autorisation pour BallDontLie API
        headers['Authorization'] = f'Bearer {API_KEY}'
    
    try:
        response = requests.get(f"{API_BASE_URL}/{endpoint}", headers=headers, params=params)
        print(f"🌐 Requête API: {endpoint} - Status: {response.status_code}")
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"❌ Erreur API: {e}")
        print(f"🔍 Headers utilisés: {headers}")
        return None

def get_all_players(cursor=None):
    """Récupère tous les joueurs avec le système de curseur"""
    params = {'per_page': 25}  # Réduire pour de meilleures performances
    if cursor:
        params['cursor'] = cursor
    
    data = make_api_request('players', params)
    
    if data and data.get('data'):
        print(f"✅ {len(data['data'])} joueurs récupérés (curseur: {cursor or 'début'})")
    else:
        print(f"⚠️ Aucun joueur récupéré (curseur: {cursor or 'début'})")
    
    return data

def get_player_by_id(player_id):
    """Récupère un joueur par son ID"""
    return make_api_request(f'players/{player_id}')

def get_all_teams():
    """Récupère toutes les équipes"""
    return make_api_request('teams')

def get_team_by_id(team_id):
    """Récupère une équipe par son ID"""
    return make_api_request(f'teams/{team_id}')

def get_all_games(cursor=None):
    """Récupère tous les matchs avec le système de curseur"""
    params = {'per_page': 25}  # Réduire pour de meilleures performances
    if cursor:
        params['cursor'] = cursor
    
    data = make_api_request('games', params)
    
    if data and data.get('data'):
        print(f"✅ {len(data['data'])} matchs récupérés (curseur: {cursor or 'début'})")
    else:
        print(f"⚠️ Aucun match récupéré (curseur: {cursor or 'début'})")
    
    return data

def get_game_by_id(game_id):
    """Récupère un match par son ID"""
    return make_api_request(f'games/{game_id}')

def get_team_players(team_id):
    """Récupère tous les joueurs d'une équipe"""
    # Nouvelle approche : utiliser l'endpoint spécifique pour les joueurs d'une équipe
    params = {'team_ids[]': team_id, 'per_page': 100}
    data = make_api_request('players', params)
    
    if data and data.get('data'):
        print(f"✅ Trouvé {len(data['data'])} joueurs pour l'équipe {team_id}")
        return data['data']
    
    print(f"⚠️ Aucun joueur trouvé pour l'équipe {team_id}")
    return []

def search_players(query, cursor=None):
    """Recherche des joueurs par nom"""
    params = {'per_page': 25, 'search': query}
    if cursor:
        params['cursor'] = cursor
    
    data = make_api_request('players', params)
    
    if data and data.get('data'):
        print(f"✅ Recherche '{query}': {len(data['data'])} joueurs trouvés")
    else:
        print(f"⚠️ Recherche '{query}': Aucun joueur trouvé")
    
    return data

def search_teams(query):
    """Recherche des équipes par nom"""
    data = get_all_teams()
    if not data or not data.get('data'):
        return {'data': []}
    
    # Filtrer les équipes localement car l'API n'a pas de recherche
    teams = data['data']
    filtered_teams = []
    query_lower = query.lower()
    
    for team in teams:
        if (query_lower in team.get('full_name', '').lower() or 
            query_lower in team.get('name', '').lower() or 
            query_lower in team.get('city', '').lower() or 
            query_lower in team.get('abbreviation', '').lower()):
            filtered_teams.append(team)
    
    print(f"✅ Recherche équipes '{query}': {len(filtered_teams)} équipes trouvées")
    return {'data': filtered_teams}

def search_games_by_date(date_query, cursor=None):
    """Recherche des matchs par date"""
    params = {'per_page': 25}
    if cursor:
        params['cursor'] = cursor
    
    # Essayer de parser la date
    try:
        # Formats acceptés: YYYY-MM-DD, DD/MM/YYYY, DD-MM-YYYY
        if '/' in date_query:
            parts = date_query.split('/')
            if len(parts) == 3:
                if len(parts[2]) == 4:  # DD/MM/YYYY
                    date_query = f"{parts[2]}-{parts[1].zfill(2)}-{parts[0].zfill(2)}"
        elif '-' in date_query and len(date_query.split('-')[0]) == 2:  # DD-MM-YYYY
            parts = date_query.split('-')
            if len(parts) == 3:
                date_query = f"{parts[2]}-{parts[1].zfill(2)}-{parts[0].zfill(2)}"
        
        params['dates[]'] = date_query
    except:
        pass
    
    data = make_api_request('games', params)
    
    if data and data.get('data'):
        print(f"✅ Recherche matchs '{date_query}': {len(data['data'])} matchs trouvés")
    else:
        print(f"⚠️ Recherche matchs '{date_query}': Aucun match trouvé")
    
    return data

# Routes
@app.route('/')
def index():
    if current_user.is_authenticated:
        return redirect(url_for('players'))
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('players'))
    
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and user.check_password(form.password.data):
            login_user(user)
            return redirect(url_for('players'))
        flash('Nom d\'utilisateur ou mot de passe incorrect')
    
    return render_template('login.html', form=form)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('players'))
    
    form = RegisterForm()
    if form.validate_on_submit():
        if User.query.filter_by(username=form.username.data).first():
            flash('Ce nom d\'utilisateur existe déjà')
            return render_template('register.html', form=form)
        
        user = User(username=form.username.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Compte créé avec succès!')
        return redirect(url_for('login'))
    
    return render_template('register.html', form=form)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route('/players')
@login_required
def players():
    cursor = request.args.get('cursor', None)
    search_query = request.args.get('search', '').strip()
    
    if search_query:
        data = search_players(search_query, cursor)
        search_active = True
    else:
        data = get_all_players(cursor)
        search_active = False
    
    if not data:
        flash('Erreur lors du chargement des joueurs')
        return render_template('players.html', players=[], meta={'has_next': False, 'has_prev': False}, 
                             search_query=search_query, search_active=search_active)
    
    # Adapter la structure meta pour le système de curseur
    meta = {
        'has_next': bool(data.get('meta', {}).get('next_cursor')),
        'has_prev': bool(cursor),
        'next_cursor': data.get('meta', {}).get('next_cursor'),
        'current_cursor': cursor
    }
    
    return render_template('players.html', players=data.get('data', []), meta=meta, 
                         search_query=search_query, search_active=search_active)

@app.route('/player/<int:player_id>')
@login_required
def player_detail(player_id):
    data = get_player_by_id(player_id)
    if not data:
        flash('Joueur non trouvé')
        return redirect(url_for('players'))
    
    return render_template('player_detail.html', player=data.get('data'))

@app.route('/teams')
@login_required
def teams():
    search_query = request.args.get('search', '').strip()
    
    if search_query:
        data = search_teams(search_query)
        search_active = True
    else:
        data = get_all_teams()
        search_active = False
    
    if not data:
        flash('Erreur lors du chargement des équipes')
        return render_template('teams.html', teams=[], search_query=search_query, search_active=search_active)
    
    return render_template('teams.html', teams=data.get('data', []), 
                         search_query=search_query, search_active=search_active)

@app.route('/team/<int:team_id>')
@login_required
def team_detail(team_id):
    team_data = get_team_by_id(team_id)
    if not team_data:
        flash('Équipe non trouvée')
        return redirect(url_for('teams'))
    
    players = get_team_players(team_id)
    return render_template('team_detail.html', team=team_data.get('data'), players=players)

@app.route('/games')
@login_required
def games():
    cursor = request.args.get('cursor', None)
    search_query = request.args.get('search', '').strip()
    
    if search_query:
        data = search_games_by_date(search_query, cursor)
        search_active = True
    else:
        data = get_all_games(cursor)
        search_active = False
    
    if not data:
        flash('Erreur lors du chargement des matchs')
        return render_template('games.html', games=[], meta={'has_next': False, 'has_prev': False},
                             search_query=search_query, search_active=search_active)
    
    # Adapter la structure meta pour le système de curseur
    meta = {
        'has_next': bool(data.get('meta', {}).get('next_cursor')),
        'has_prev': bool(cursor),
        'next_cursor': data.get('meta', {}).get('next_cursor'),
        'current_cursor': cursor
    }
    
    return render_template('games.html', games=data.get('data', []), meta=meta,
                         search_query=search_query, search_active=search_active)

@app.route('/game/<int:game_id>')
@login_required
def game_detail(game_id):
    data = get_game_by_id(game_id)
    if not data:
        flash('Match non trouvé')
        return redirect(url_for('games'))
    
    return render_template('game_detail.html', game=data.get('data'))

# Template Filters
@app.template_filter('format_date')
def format_date(date_string):
    """Formate une date pour l'affichage"""
    if not date_string:
        return "Date inconnue"
    try:
        date = datetime.fromisoformat(date_string.replace('Z', '+00:00'))
        return date.strftime('%d/%m/%Y')
    except:
        return date_string

@app.template_filter('format_position')
def format_position(position):
    """Formate une position avec son nom complet"""
    if not position:
        return ""
    
    position_names = {
        'G': 'Guard (Meneur)',
        'PG': 'Point Guard (Meneur)',
        'SG': 'Shooting Guard (Arrière)',
        'F': 'Forward (Ailier)',
        'SF': 'Small Forward (Ailier fort)',
        'PF': 'Power Forward (Ailier fort)',
        'C': 'Center (Pivot)',
        'G-F': 'Guard-Forward (Meneur-Ailier)',
        'F-G': 'Forward-Guard (Ailier-Meneur)',
        'F-C': 'Forward-Center (Ailier-Pivot)',
        'C-F': 'Center-Forward (Pivot-Ailier)'
    }
    
    return position_names.get(position, position)

if __name__ == '__main__':
    print("🏀 Démarrage de l'application NBA...")
    print("📍 Pour arrêter l'application, utilisez Ctrl+C")
    print("🌐 L'application sera accessible sur: http://localhost:5000")
    print("=" * 50)
    
    with app.app_context():
        db.create_all()
    
    # Configuration adaptative : local vs production
    if os.environ.get('RENDER'):
        # Configuration pour Render (production)
        port = int(os.environ.get('PORT', 10000))
        app.run(host='0.0.0.0', port=port, debug=False)
    else:
        # Configuration locale (développement)
        app.run(debug=True)
