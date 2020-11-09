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
2. Duplicate settings.py so that there is local_settings.py and prod_settings.py
  -- for development and production environments respectively
3. Create 02_env.config
4. Add SECRET_KEY and DEBUG to the file
5. ALLOWED_HOSTS can be hard-coded into settings file
5. Make sure that local_settings.py are in .ebignore

### GitHub:
1. Create GitHub repository with README.md (this) and .gitignore (template for django found online) files
2. Rename webdevsite dir - call it webdevsite-template
3. Clone repository (git clone <URL> .) to the webdevsite empty dir
4. Add branch (git remote add origin <URL>)
5. Copy all (including hidden files!) stuff from webdevsite-temp to webdevsite and remove webdevsite-temp
6. Make sure that prod_settings.py is in .gitignore
7. Make sure git stuff is in .ebignore
6. Set default environment for EB (eb use webdevsite-env)
7. Test it (eb deploy && eb status)
8. 
