# 🌟 Portfolio — Mariam Abakar Adoum

Portfolio personnel développé avec **Python / Django 4.2**, design éditorial élégant fond nuit et doré.

---

## ✨ Fonctionnalités

| Page | Description |
|------|-------------|
| **Accueil** | Hero animé, section À propos, CV complet avec barres de progression |
| **Contact** | Formulaire Django (sauvegarde en base de données) |
| **Connexion** | Authentification Django sécurisée |
| **Dashboard** | Voir et gérer les messages reçus |
| **Admin Django** | Interface `/admin/` pour tout gérer |

---

## 🛠️ Technologies

- **Backend** : Python 3.10+ · Django 4.2 · SQLite / PostgreSQL
- **Frontend** : HTML5 · CSS3 · JavaScript ES6+
- **Déploiement** : Gunicorn · WhiteNoise · Render / Railway
- **Polices** : Cormorant Garamond + DM Sans

---

## 🚀 Installation locale

```bash
# 1. Cloner le projet
git clone https://github.com/votre-username/mariam-portfolio.git
cd mariam-portfolio

# 2. Créer l'environnement virtuel
python -m venv venv
source venv/bin/activate        # Windows : venv\Scripts\activate

# 3. Installer les dépendances
pip install -r requirements.txt

# 4. Configurer les variables d'environnement
cp .env.example .env
# Éditez .env et mettez votre SECRET_KEY

# 5. Appliquer les migrations
python manage.py migrate

# 6. Charger les données initiales
python manage.py loaddata portfolio/fixtures/initial_data.json

# 7. Créer un superutilisateur
python manage.py createsuperuser
# → choisissez le nom d'utilisateur "mariam" et un mot de passe

# 8. Lancer le serveur
python manage.py runserver
```

Accédez à **http://127.0.0.1:8000**

---

## 🔐 Accès

| URL | Description |
|-----|-------------|
| `http://127.0.0.1:8000/` | Site public |
| `http://127.0.0.1:8000/connexion/` | Connexion |
| `http://127.0.0.1:8000/dashboard/` | Tableau de bord |
| `http://127.0.0.1:8000/admin/` | Administration Django |

---

## 🖼️ Ajouter votre photo de profil

Placez votre photo ici :
```
portfolio/static/images/profile.jpg
```
Puis exécutez :
```bash
python manage.py collectstatic
```

---

## 📁 Structure du projet

```
mariam-portfolio/
├── manage.py
├── requirements.txt
├── Procfile                         # Déploiement
├── .env.example
├── mariam_site/
│   ├── settings.py                  # Configuration Django
│   ├── urls.py                      # URLs principales
│   └── wsgi.py
└── portfolio/                       # Application principale
    ├── models.py                    # Message, Compétence, Formation, Langue
    ├── views.py                     # Vues (index, contact, login, dashboard)
    ├── forms.py                     # Formulaire de contact
    ├── urls.py                      # URLs de l'app
    ├── admin.py                     # Interface admin
    ├── fixtures/
    │   └── initial_data.json        # Données de départ
    ├── templates/portfolio/
    │   ├── base.html
    │   ├── index.html
    │   ├── contact.html
    │   ├── login.html
    │   └── dashboard.html
    └── static/
        ├── css/style.css
        ├── js/script.js
        └── images/                  # Mettez profile.jpg ici
```

---

## 🌍 Déploiement sur Render (gratuit)

1. Poussez le projet sur **GitHub**
2. Créez un compte sur [render.com](https://render.com)
3. **New Web Service** → connectez votre dépôt
4. Paramètres :
   - **Build Command** : `pip install -r requirements.txt && python manage.py collectstatic --noinput`
   - **Start Command** : `gunicorn mariam_site.wsgi --log-file -`
5. Variables d'environnement à ajouter :
   ```
   SECRET_KEY   = une-cle-aleatoire-longue
   DEBUG        = False
   ALLOWED_HOSTS = votre-app.onrender.com
   ```

---

## 🎨 Personnalisation

Pour modifier vos informations (compétences, langues, formations) :
- Via **l'interface admin** Django : `/admin/`
- Ou en modifiant directement `portfolio/fixtures/initial_data.json` puis en rechargeant

---

*Développé avec ❤️ par Mariam Abakar Adoum*  
*Étudiante en Génie Logiciel — Institut National de Science et Technique d'Abéché*
