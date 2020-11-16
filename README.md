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
1. Duplicate settings.py so that there is local_settings.py and prod_settings.py
  -- for development and production environments respectively
2. Create 02_env.config
3. Add SECRET_KEY and DEBUG to the file
4. ALLOWED_HOSTS can be hard-coded into settings file
5. Make sure that local_settings.py are in .ebignore

### GitHub:
1. Create GitHub repository with README.md (this) and .gitignore (template for django found online) files
2. Rename webdevsite dir - call it webdevsite-template
3. Clone repository (git clone <URL> .) to the webdevsite empty dir
4. Add branch (git remote add origin <URL>)
5. Copy all (including hidden files!) stuff from webdevsite-temp to webdevsite and remove webdevsite-temp
6. Make sure that prod_settings.py is in .gitignore
7. Make sure git stuff is in .ebignore
8. Set the default environment for EB (eb use webdevsite-env)
9. Test it (eb deploy && eb status; source eb-virt/bin/activate && python manage.py runserver)

### Backend (part 1):
1. Create projects and website apps
2. Add them to settings files
3. Create urls.py in website directories
4. Migrate if you haven't already (python manage.py migrate)
5. Create templates folder inside of website app
6. Add index.html and hire_me.html there
7. In webdevsite/urls.py add mapping to the website/urls.py using path and include
8. In website/urls.py add paths to view.index and view.hire_me using path
9. Add index() and hire_me() functions in website/views.py redirecting to (rendering) the index.html and hire_me.html templates
10. Write "index" in index.html and "hire me" in hire_me.html
10. Run server and test both templates
11. Do the same process for the other app (webdevsite/urls.py, website/urls.py, website/views.py, website/template/project.html)
12. Test it

### Configure Database:
1. Install pg_config ($ pg_config --version, then if it returns an error, type in 'y' to install it)
2. Check in pg_config's (PostgreSQL) version is 12.4
3. Install python-dev (sudo dnf install python3-devel)
4. Run pip freeze > requirements.txt to update requirements file
  -- more info on https://www.psycopg.org/docs/install.html#prerequisites
5. Install postgresql-server (dnf)
6. Run postgresql-setup initdb and systemctl start postgresql to initialise and start PG cluster
  -- type in service postgresql status to check if it's working
7. Log in using sudo -u postgres psql
8. Create project database: CREATE DATABASE webdevsite;
9. Create project user: CREATE USER webdev WITH PASSWORD '...';
10. Set encoding (the same as django): ALTER ROLE webdev SET client_encoding TO 'utf8';
11. Block reading from uncommitted transactions: ALTER ROLE webdev SET default_transaction_isolation TO 'read committed';
12. Set time zone (the same as django): ALTER ROLE webdev SET timezone TO 'UTC';
13. Give access to database: GRANT ALL PRIVILEGES ON DATABASE webdevsite TO webdev;
14. Remove db.sqlite3 file
15. Modify local_settings.py accordingly
16. Go to /var/lib/pgsql/data (or any other directory in which pgsql is stored) and modify pg_hba.config
  -- swap ident with md5
17. Run service postgresql restart and service postgresql status to check if it works
16. Makemigrations and migrate

### Backend (part 2):
1. Add STATIC_ROOT in local_settings.py
2. Add MEDIA_URL and MEDIA_ROOT in local_settings.py
3. Install Pillow 8.0.1 and update requirements.txt
4. Create projects model
  -- Copied from the Portfolio project
5. Makemigrations and migrate
6. Check if the table was created
  -- connect to the psql console (sudo -u postgres psql)
  -- connect to the database (\\c webdevsite)
  -- list tables (\\dt)
  -- last two rows should display projects_link and projects_project
7. Run python manage.py createsuperuser
  -- patryk; jesionka.patryk13@gmail.com; 1234
8. Register models in projects/admin.py via admin.site.register(<ModelName>)
9. Run python manage.py collectstatic
10. Check if it works going to localhost:8000/admin
11. Create a test project(s) and link(s)
12. Add static dir to .gitignore
13. Add static and media dirs and migrations to .ebignore

### Configure database and static/media files (on the server):
1. Run eb deploy
  -- encounter errors
2. Add 00_packages.config
3. Crash the whole environment by redoing eb deploy
4. Remove 00_packages.config
5. In requirements.txt rename psycopg2 to psycopg2-binary
6. Run eb create
7. Run eb status to get the CNAME
8. Run eb deploy and eb logs to find IP that return error 404 - add it to prod_settings as well
9. Crash the environment trying to add packages: yum: postgresql12-devel: []
10. Clean up and start the environment again
11. Change psycopg2 to psycopg2-binary and deploy
12. Add 02_packages.config file with postgresql12-devel so that env.config has # 3
13. Deploy and test
14. Following AWS documentation set up RDS database instance
  -- https://us-east-2.console.aws.amazon.com/elasticbeanstalk/home?region=us-east-2#/environment/dashboard?applicationName=webdevsite&environmentId=e-xxd6iswwqa
15. Update prod_settings.py
16. Restart app servers in the EB Console
17. Run eb deploy
18. Add container_commands: 00_makemigrations and 01_migrate: to the 01_python.config
19. Run eb Deploy
20. Add option_settings for static files and container_commands: 02_collectstatic:
21. Update prod_settings.py for static files
22. Run eb deploy
23. Create a custom command that creates a super user with given details
  -- https://docs.djangoproject.com/en/3.1/howto/custom-management-commands/
  -- run python manage.py startapp s_user
24. Create a dir structure inside of the app: management/commands/createsu.py
25. Write a class to handle creating super user via User.objects.create_superuser()
  -- user details given as environmental variables
26. Add s_user app to prod_settings.py
27. Write SU_NAME, SU_EMAIL, SU_PASSWORD variables into environment via eb console
28. Write 03_createsuperuser into 01_python.config
29. Run eb deploy and go to <url>/admin to log in
30. Had a problem with reading static files. The formatting of config was off; that's the correct one:
  -- aws:elasticbeanstalk:environment:proxy:staticfiles: /static: static
31. Go to the AWS S3 bucket (which is already created) and create a files/media directory structure
32. Go to /.aws/credentials (or any other place with your aws credentials) and copy access key and key id to environment variables
33. Install boto3 and django-storages
34. Edit prod_settings.py
  -- https://coderbook.com/@marcus/how-to-store-django-static-and-media-files-on-s3-in-production/

Configure media files
Create new secret key
Transfer env variables to .config file
