# SMARTHR

SMARTHR is a Django-based human resources portal for managing employee information and sharing workplace updates, holiday dates, and job opening details.

## Features

- Add, view, update, and delete employee records
- Store employee details such as ID, designation, department, joining date, annual CTC, and experience
- Display company news and updates
- Add and view holiday calendar entries
- Browse job opening information
- Provide employee and HR manager pages
- Export employee data as a CSV file
- Use Django’s built-in admin site

## Technologies

- Python
- Django
- SQLite
- HTML and CSS
- Django Templates
- Python CSV module

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/VemulaPrasanna12/SMARTHR.git
   cd SMARTHR
   ```

2. Create and activate a virtual environment:

   ```bash
   python -m venv venv
   ```

   **Windows PowerShell**

   ```powershell
   .\venv\Scripts\Activate.ps1
   ```

   **macOS/Linux**

   ```bash
   source venv/bin/activate
   ```

3. Install Django:

   ```bash
   pip install django
   ```

4. Apply database migrations:

   ```bash
   python manage.py migrate
   ```

5. Create an administrator account:

   ```bash
   python manage.py createsuperuser
   ```

6. Start the development server:

   ```bash
   python manage.py runserver
   ```

7. Open `http://127.0.0.1:8000/` in your browser. The project’s routes include `/home/`, `/emp/`, and `/hrmanager/`.

## Database Setup

The project uses SQLite. Django stores the database in `db.sqlite3` at the project root.

To create migrations after changing a model and apply them:

```bash
python manage.py makemigrations
python manage.py migrate
```

## Application Routes

This project currently uses Django-rendered web pages and does not expose a REST API.

| Endpoint | Description |
|---|---|
| `/admin/` | Django administration |
| `/home/` | Home page |
| `/emp/` | Employee page; requires an authenticated user |
| `/emp2/` | Additional employee page |
| `/employee/` | Employee page |
| `/hrmanager/` | HR manager page |
| `/login/` | Login page |
| `/addemployee/` | Add an employee |
| `/viewemployee/` | View employee records |
| `/update/<id>` | Update an employee record |
| `/delete/<id>` | Delete an employee record |
| `/download/` | Download employee data as CSV |
| `/holidaycalendar/` | View holiday calendar |
| `/calender/` | Add a calendar entry |
| `/holidaycalendar/news/` | View company news |
| `/employee/latestnews/` | View latest news |
| `/hrmanager/jobopenings/` | View job openings |
| `/adddetails/` | Add a news or details entry |
| `/details/<id>/` | View a details entry |

## Future Improvements

- Add working login and role-based access for employees and HR managers
- Protect employee management actions so only authorized users can make changes
- Complete job opening management, including adding and editing roles
- Fix and verify CSV export formatting
- Add form validation and clearer error messages
- Add automated tests
- Add a `requirements.txt` file for reproducible installation
- Prepare production settings, including secure secret management and debug settings

    
10:58 PM







mote informatio for this project 







10:59 PM






Here’s a more detailed, copy-ready README for SMARTHR:
# SMARTHR

SMARTHR is a Django-based human resources portal for handling employee records and viewing company updates, holiday dates, and job opening information. It uses SQLite and Django templates to provide a web interface for employee and HR-related pages.

## Features

- Add and view employee records
- Update and delete employee information
- Store employee ID, designation, department, joining date, annual CTC, and experience
- Export employee data as a CSV file
- Add and view holiday calendar entries
- Display company news and details
- View job opening information
- Provide employee and HR manager pages
- Include Django’s built-in administration site

## Technologies

- **Backend:** Python, Django
- **Database:** SQLite
- **Frontend:** HTML, CSS, Django Templates
- **Data export:** Python CSV module

## Project Structure

```text
SMARTHR/
├── app1/                  # Models, forms, views, admin, and migrations
├── project/               # Django settings and URL configuration
├── static/                # CSS and image files
├── templates/             # HTML templates
├── db.sqlite3             # SQLite database
└── manage.py              # Django management commands
```

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/VemulaPrasanna12/SMARTHR.git
   cd SMARTHR
   ```

2. Create and activate a virtual environment:

   ```bash
   python -m venv venv
   ```

   **Windows PowerShell**

   ```powershell
   .\venv\Scripts\Activate.ps1
   ```

   **macOS/Linux**

   ```bash
   source venv/bin/activate
   ```

3. Install Django:

   ```bash
   pip install django
   ```

4. Apply the existing database migrations:

   ```bash
   python manage.py migrate
   ```

5. Create an administrator account for Django Admin:

   ```bash
   python manage.py createsuperuser
   ```

6. Start the development server:

   ```bash
   python manage.py runserver
   ```

7. Open `http://127.0.0.1:8000/home/` in your browser. The project does not define a homepage at `/`.

## Database Setup

SMARTHR uses SQLite. Django stores the database in `db.sqlite3` in the project root.

The application defines these database models:

- **Employee:** name, employee ID, designation, joining date, department, annual CTC, and experience
- **Details:** text content used for company news or updates
- **Calendar:** date and occasion
- **JobOpening:** role, experience, skills, CTC, and notice period

To create and apply migrations after changing a model:

```bash
python manage.py makemigrations
python manage.py migrate
```

## Application Routes

These are Django web routes, not REST API endpoints.

| Method | Endpoint | Description |
|---|---|---|
| GET | `/home/` | Home page |
| GET | `/emp/` | Employee page; requires an authenticated user |
| GET | `/emp2/` | Additional employee page |
| GET | `/employee/` | Employee page |
| GET | `/hrmanager/` | HR manager page |
| GET | `/login/` | Displays the login page |
| GET, POST | `/addemployee/` | Add an employee |
| GET | `/viewemployee/` | List employee records |
| GET, POST | `/update/<id>` | Display or update an employee record |
| `/delete/<id>` | Delete an employee record |
| GET | `/download/` | Download employee data as CSV |
| GET, POST | `/calender/` | Display the calendar form or add a calendar entry |
| GET | `/holidaycalendar/` | View holiday entries |
| GET | `/holidaycalendar/news/` | View company news |
| GET | `/employee/latestnews/` | View news and details entries |
| GET | `/hrmanager/jobopenings/` | View job opening information |
| GET, POST | `/adddetails/` | Display the details form or add an entry |
| GET | `/details/<id>/` | View a details entry |
| GET | `/admin/` | Django administration |

## Authentication Note

The project includes Django’s authentication middleware, and the `/emp/` page requires an authenticated user. The `/login/` route currently displays a template; it does not itself process a login. Review and complete authentication and access controls before deploying the application.

## Future Improvements

- Implement working login and logout flows
- Add role-based permissions for employees and HR managers
- Protect employee create, update, and delete actions
- Add full job opening management
- Verify and improve CSV export formatting
- Add input validation and clearer error handling
- Add automated tests
- Add a `requirements.txt` file for repeatable setup
- Configure secure production settings and deployment instructions

    
10:59 PM



















Work locallyLocal
