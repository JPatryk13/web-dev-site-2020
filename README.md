# webdevsite
Web development services entrepreneurship website.

## Some guides:
### Prerequisites:
1. AWS Account
2. EB CLI
3. GitHub Account
4. Git CLI
5. Python 3.7
6. Pip
7. Virtualenv
### Setup:

1. Create venv (virtualenv)
2. Start django project (django-admin)
3. Run the app locally (python manage.py)
4. Create .ebextensions/01_python.config (/w Gunicorn WSGI and project settings file)
5. Initialise Elastic Beanstalk environment (eb init)
6. Create EB Application (eb create)
7. Add CNAME in ALLOWED_HOSTS in settings.py
8. Deploy the app (eb deploy) and see if works

### Configuration:
1. Install python-dotenv
2. Duplicate settings.py so that there is local_settings.py and prod_settings.py
  -- for development and production environments respectively
3. Create .env alongside with settings files
4. Make sure that prod_settings.py and .env are in .gitignore
5. Make sure that local_settings.py are in .ebignore
