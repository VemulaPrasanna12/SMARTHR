# SMARTHR – Human Resource Management System

## Project Overview

SMARTHR is a Django-based Human Resource Management System developed using Python, Django, HTML, CSS, and SQLite.

This project helps manage employee information and provides a platform for viewing company news, holiday calendars, and job openings.

The application allows users to add, view, update, and delete employee records. It stores employee details such as employee ID, name, designation, department, joining date, annual CTC, and experience.

It also provides separate employee and HR manager pages, a CSV export feature for employee records, and a Django admin panel for managing application data.

The main objective of this project is to understand how an HR management system works and gain practical experience in Django web development, database management, and CRUD operations.

## Features

- Add new employee records
- View employee information
- Update and delete employee details
- Store employee ID, name, designation, and department
- Maintain joining date, annual CTC, and experience
- View company news and updates
- Add and view holiday calendar entries
- Browse available job openings
- Employee and HR manager pages
- Export employee information as a CSV file
- Django admin panel for data management

## Technologies Used

- **Frontend:** HTML, CSS
- **Backend:** Python, Django
- **Database:** SQLite
- **Templates:** Django Templates
- **Data Export:** Python CSV Module
- **Tools:** VS Code, Git, GitHub

## Project Structure

- `app1/` – Django application containing models, views, forms, and admin configuration
- `project/` – Main Django project settings and URL configuration
- `templates/` – HTML templates for website pages
- `static/` – CSS files and images
- `db.sqlite3` – SQLite database
- `manage.py` – Django management file

## Installation

Clone the repository:

```bash
git clone https://github.com/VemulaPrasanna12/SMARTHR.git
cd SMARTHR
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate the virtual environment:

**Windows PowerShell:**
```powershell
.\venv\Scripts\Activate.ps1
```

**macOS/Linux:**
```bash
source venv/bin/activate
```

Install Django:

```bash
pip install django
```

## Database Setup

Apply database migrations:

```bash
python manage.py migrate
```

Create an administrator account:

```bash
python manage.py createsuperuser
```

## How to Run the Project

Start the Django development server:

```bash
python manage.py runserver
```

Open the following URLs in your browser:

- **Home Page:** http://127.0.0.1:8000/home/
- **Employee Page:** http://127.0.0.1:8000/emp/
- **HR Manager Page:** http://127.0.0.1:8000/hrmanager/
- **Django Admin:** http://127.0.0.1:8000/admin/

Press `Ctrl + C` in the terminal to stop the server.

## Application Routes

| URL | Description |
|---|---|
| `/home/` | Home page |
| `/emp/` | Employee page |
| `/emp2/` | Additional employee page |
| `/employee/` | Employee information page |
| `/hrmanager/` | HR manager page |
| `/login/` | Login page |
| `/addemployee/` | Add employee details |
| `/viewemployee/` | View employee records |
| `/update/<id>` | Update employee details |
| `/delete/<id>` | Delete employee records |
| `/download/` | Export employee data as CSV |
| `/holidaycalendar/` | View holiday calendar |
| `/calender/` | Add calendar entries |
| `/holidaycalendar/news/` | View company news |
| `/employee/latestnews/` | View latest news |
| `/hrmanager/jobopenings/` | View job openings |
| `/adddetails/` | Add company news or details |
| `/details/<id>/` | View details |
| `/admin/` | Django admin panel |

## Future Improvements

- Implement complete employee and HR manager login functionality
- Add role-based access permissions
- Improve employee data validation
- Add job opening creation and management
- Improve CSV export functionality
- Add automated testing
- Add a `requirements.txt` file
- Improve the website design and responsiveness
- Deploy the application online

## Learning Outcomes

Through this project, I learned how to:

- Develop a web application using Python and Django
- Create and manage database models using SQLite
- Perform CRUD operations
- Build dynamic web pages using Django templates
- Work with forms, views, and URL routing
- Export database records into CSV files
- Understand basic employee management workflows
- Use Git and GitHub for version control
