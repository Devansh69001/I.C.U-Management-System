# COMPLETE DJANGO PROJECT SETUP GUIDE

## Step-by-Step Installation and Setup Instructions

### Prerequisites
- Python 3.8 or higher
- MySQL Server installed and running
- Git (optional)

### Step 1: Create Project Directory and Virtual Environment

```bash
# Create project directory
mkdir hospital_icu_management
cd hospital_icu_management

# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

### Step 2: Create Django Project and Apps

```bash
# Install Django
pip install django

# Create Django project
django-admin startproject hospital_icu_management 

# Create individual apps
python manage.py startapp staff
python manage.py startapp patients
python manage.py startapp doctor
python manage.py startapp nurse
python manage.py startapp equipment
python manage.py startapp reports
```

### Step 3: Create requirements.txt

Copy all dependencies from the requirements.txt file provided, then install:

```bash
pip install -r requirements.txt
```

### Step 4: Create MySQL Database

```bash
# Connect to MySQL
mysql -u root -p

# In MySQL prompt:
CREATE DATABASE hospital_icu_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
SHOW DATABASES;
EXIT;
```

### Step 5: Configure .env File

Create a `.env` file in your project root with:

```
DEBUG=True
SECRET_KEY=your-very-secret-key-change-this-in-production
DATABASE_NAME=hospital_icu_db
DATABASE_USER=root
DATABASE_PASSWORD=your_mysql_password
DATABASE_HOST=localhost
DATABASE_PORT=3306
ALLOWED_HOSTS=localhost,127.0.0.1
```

### Step 6: Copy All Code Files

For each app (staff, patients, doctor, nurse, equipment, reports):

1. Replace `models.py` with code from `all_models.md`
2. Replace `serializers.py` with code from `serializers_views.md`
3. Replace `views.py` with code from `serializers_views.md`
4. Replace `urls.py` with code from `serializers_views.md`
5. Replace `admin.py` with code from `admin_apps.md`
6. Replace `apps.py` with code from `admin_apps.md`

Update `hospital_icu_management/settings.py` with code from `django_project_setup.md`
Update `hospital_icu_management/urls.py` with code from `django_project_setup.md`

### Step 7: Create Templates and Static Files

Create the following directories:
```bash
mkdir -p templates/staff
mkdir -p templates/patients
mkdir -p templates/doctor
mkdir -p templates/nurse
mkdir -p templates/equipment
mkdir -p templates/reports
mkdir -p static/css
mkdir -p static/js
mkdir -p static/images
```

Create files:
- `templates/base.html` - from `templates_frontend.md`
- `templates/patients/patient_list.html` - from `templates_frontend.md`
- `static/css/style.css` - from `templates_frontend.md`
- `static/js/dashboard.js` - from `templates_frontend.md`

### Step 8: Run Migrations

```bash
# Create migration files
python manage.py makemigrations

# Show migration details (optional)
python manage.py showmigrations

# Apply migrations
python manage.py migrate
```

### Step 9: Create Superuser

```bash
python manage.py createsuperuser
# Follow prompts to enter username, email, and password
```

### Step 10: Collect Static Files

```bash
python manage.py collectstatic --noinput
```

### Step 11: Run Development Server

```bash
python manage.py runserver
```

The application will be available at: `http://127.0.0.1:8000`
Admin panel: `http://127.0.0.1:8000/admin`
API Docs: `http://127.0.0.1:8000/api/docs/`

---

## Project File Structure Summary

```
hospital_icu_management/
├── manage.py
├── requirements.txt
├── .env
├── db.sqlite3 (or MySQL database)
├── hospital_icu_management/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
├── doctor/
│   ├── migrations/
│   ├── templates/doctor/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── serializers.py
│   ├── urls.py
│   ├── views.py
│   └── tests.py
├── nurse/
│   ├── migrations/
│   ├── templates/nurse/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── serializers.py
│   ├── urls.py
│   ├── views.py
│   └── tests.py
├── patients/
│   ├── migrations/
│   ├── templates/patients/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── serializers.py
│   ├── urls.py
│   ├── views.py
│   └── tests.py
├── staff/
│   ├── migrations/
│   ├── templates/staff/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── serializers.py
│   ├── urls.py
│   ├── views.py
│   └── tests.py
├── equipment/
│   ├── migrations/
│   ├── templates/equipment/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── serializers.py
│   ├── urls.py
│   ├── views.py
│   └── tests.py
├── reports/
│   ├── migrations/
│   ├── templates/reports/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── serializers.py
│   ├── urls.py
│   ├── views.py
│   └── tests.py
├── templates/
│   └── base.html
│   └── patients/patient_list.html
└── static/
    ├── css/style.css
    └── js/dashboard.js
```

---

## Common Commands

### Development Commands

```bash
# Start development server
python manage.py runserver

# Create new migrations
python manage.py makemigrations

# Apply migrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser

# Access Django shell
python manage.py shell

# Collect static files
python manage.py collectstatic

# Run tests
python manage.py test

# Create app
python manage.py startapp app_name
```

### Database Commands

```bash
# Show migration status
python manage.py showmigrations

# Show SQL for specific migration
python manage.py sqlmigrate app_name migration_name

# Check for issues
python manage.py check
```

---

## API Endpoints Overview

### Staff Management
- `GET/POST /api/staff/` - List/Create staff
- `GET/PUT/DELETE /api/staff/<id>/` - Retrieve/Update/Delete staff
- `GET /api/staff/doctors/` - List all doctors
- `GET /api/staff/nurses/` - List all nurses

### Patient Management
- `GET/POST /api/patients/` - List/Create patients
- `GET/PUT/DELETE /api/patients/<id>/` - Retrieve/Update/Delete patient

### Doctor Services
- `GET/POST /api/doctor/prescriptions/` - List/Create prescriptions
- `GET/POST /api/doctor/treatment-plans/` - List/Create treatment plans

### Nurse Services
- `GET/POST /api/nurse/admissions/` - List/Create admissions
- `GET/POST /api/nurse/observations/` - List/Create observations

### Equipment
- `GET/POST /api/equipment/equipment/` - List/Create equipment
- `GET/POST /api/equipment/maintenance-logs/` - List/Create maintenance logs

### Reports
- `GET/POST /api/reports/` - List/Create reports

### Documentation
- `GET /api/docs/` - Swagger/OpenAPI documentation

---

## Troubleshooting

### MySQL Connection Issues
```
Error: "Can't connect to MySQL server"
Solution:
1. Ensure MySQL is running: `mysql -u root -p`
2. Check .env DATABASE settings
3. Verify database exists: `SHOW DATABASES;`
```

### Migration Issues
```
Solution:
1. Delete migration files in app migrations/ folder (except __init__.py)
2. Run: python manage.py makemigrations
3. Run: python manage.py migrate --fake
```

### Static Files Not Loading
```
Solution:
1. Run: python manage.py collectstatic --noinput
2. Check STATIC_ROOT in settings.py
3. In production, use WhiteNoise middleware
```

### CORS Issues with Frontend
```
Solution:
Update CORS_ALLOWED_ORIGINS in settings.py:
CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",
    "http://127.0.0.1:8000",
]
```

---

## Production Deployment Checklist

- [ ] Set DEBUG=False in .env
- [ ] Generate new SECRET_KEY
- [ ] Configure ALLOWED_HOSTS
- [ ] Set up database backups
- [ ] Configure email settings
- [ ] Set up static file serving (WhiteNoise or CDN)
- [ ] Configure Gunicorn/WSGI
- [ ] Set up SSL/HTTPS
- [ ] Configure logging
- [ ] Set up monitoring and alerts
- [ ] Run security checks: `python manage.py check --deploy`

---

## Additional Resources

- Django Documentation: https://docs.djangoproject.com/
- Django REST Framework: https://www.django-rest-framework.org/
- Bootstrap 5: https://getbootstrap.com/
- MySQL Documentation: https://dev.mysql.com/doc/

