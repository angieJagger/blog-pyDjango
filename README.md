# Django Blog Project

This is a Django-based blog application built with a clean and scalable project structure.  
The project is designed with security, configurability, and future extensibility in mind.

---

## 🚀 Tech Stack

- **Python**
- **Django**
- **PostgreSQL**
- **HTML / CSS** (styling planned)
- **Git & GitHub**

---

## 📁 Project Structure

The project uses a modular Django settings configuration:
```
mysite/
├── mysite/
│ ├── settings/
│ │ ├── base.py
│ │ ├── local.py
│ │ └── production.py
│ ├── urls.py
│ ├── asgi.py
│ └── wsgi.py
├── blog/
├── manage.py
└── .gitignore
```

This structure allows easy separation of:
- common settings (`base.py`)
- local development configuration (`local.py`)
- production configuration (`production.py`)

Sensitive data (such as secret keys and database credentials) is **not included in the repository**.

---

## ⚙️ Environment Configuration

The project uses environment-based configuration.

You should create your own `.env` file or environment variables for:
- `SECRET_KEY`
- database credentials
- email configuration (if enabled)

Example (not included in repo):

SECRET_KEY=your-secret-key
DB_NAME=your_db_name
DB_USER=your_db_user
DB_PASSWORD=your_db_password
DB_HOST=localhost
DB_PORT=5432

---

## 🗄️ Database

The application is configured to work with **PostgreSQL**.

Make sure PostgreSQL is installed and running before starting the project.

---

## ▶️ Running the Project Locally

1. Clone the repository:
   ```bash
   git clone https://github.com/angieJagger/blog-pyDjango.git
   cd blog-pyDjango

2. Create and activate a virtual environment:

python -m venv my_env
source my_env/bin/activate  # Linux/macOS
my_env\Scripts\activate     # Windows


3. Install dependencies:

pip install -r requirements.txt


4. Apply migrations:

python manage.py migrate


5. Run the development server:

python manage.py runserver



🌍 Planned Features

Frontend styling (CSS / templates)

Multi-language support (i18n)

Externalized content configuration (JSON-based, no hardcoded HTML)

Further blog features and improvements


🔐 Security Notes

No secret keys or credentials are stored in the repository

.gitignore is configured to prevent sensitive files from being committed

Settings are split according to Django best practices

📌 Status

The core application logic is implemented.
The project is under active development and will be expanded further.

👤 Author

Created by Angelika Pawluk
