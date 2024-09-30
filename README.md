# HRMS (Human Resource Management System)

This project is a simple HRMS (Human Resource Management System) application built using Django. It includes functionalities such as employee management, attendance tracking, and basic reporting.

### Features
- Employee Management: Add, retrieve, and display a list of employees.
- Attendance Tracking: Mark and retrieve attendance for specific employees.
- Basic Reporting: Display a simple report of the number of employees in each department.

### Project Structure
```
hrms_project/
│
├── hrms_project/              # Django project settings and configuration
│   ├── settings.py            # Main project settings
│   ├── urls.py                # Project-level URL routing
│   └── ...
│
├── employee_management/       # Main application for employee management and attendance tracking
│   ├── migrations/            # Database migrations
│   ├── templates/             # HTML templates for rendering views
│   │   ├── home.html          # Home page template
│   │   └── report.html        # Report page template
│   ├── static/                # Static files (CSS, JS)
│   ├── admin.py               # Django admin configuration
│   ├── apps.py                # App configuration
│   ├── models.py              # Database models (Employee, Attendance)
│   ├── views.py               # Views for handling requests
│   ├── serializers.py         # Serializers for API endpoints
│   └── urls.py                # App-level URL routing
│
├── manage.py                  # Django management script
└── README.md                  # Project documentation
```

## How to Run the App Locally
Follow the steps below to set up and run the application on your local machine.

### Prerequisites
- Python 3.x
- Django 4.x
- Django REST Framework

### Installation
1. Clone the repository to your local machine:
   ```
   git clone https://github.com/yourusername/hrms_project.git
   cd hrms_project
   ```
2. Create a virtual environment and activate it:
   ```
   python -m venv venv
   source venv/bin/activate  # For Windows: venv\Scripts\activate
   ```
3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```
4. Run the database migrations:
   ```
   python manage.py makemigrations
   python manage.py migrate
   ```
5. Create a superuser for Django's admin panel:
   ```
   python manage.py createsuperuser
   ```
6. Start the Django development server:
   ```
   python manage.py runserver
   ```

## Accessing the App
- **Home Page**: Open your browser and navigate to [http://localhost:8000/](http://localhost:8000/) to view the home page.
- **API Endpoints**:
  - Add an employee: `POST /add_employee/`
  - List employees: `GET /employees/`
  - Mark attendance: `POST /mark_attendance/`
  - Get attendance: `GET /attendance/<employee_id>/`
- **Admin Panel**: Go to [http://localhost:8000/admin](http://localhost:8000/admin) to manage the app using Django's admin interface.


## Additional Information
- Employee Management: Employees have fields such as name, designation, department, and date of joining. You can add employees via the API or the admin panel.
- Attendance Tracking: Attendance can be marked for specific employees, and the attendance status can be viewed by fetching the data for that employee.
- Basic Reporting: A simple report is available that shows the number of employees per department. This is presented in a table format on the report page.

## Database Design 
The project uses Django's built-in ORM for database management. The main models are:
- Employee: Stores employee details like name, designation, department, and date of joining.
- Attendance: Tracks the attendance of employees with fields like employee reference, date, and status.

## Coding Practices
- All functions and classes are documented with clear docstrings.
- The project adheres to Python's PEP 8 coding style.
