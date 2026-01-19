🎫 Ticket Support System API

A backend REST API built using Flask to manage support tickets with authentication, roles, and ticket assignment.

🚀 Features

User Registration & Login

Token-based Authentication

Role System (User / Agent / Admin)

Create, Update, Delete Tickets

Ticket Priority & Category

Assign Tickets to Agents (Admin only)

Database Migrations using Flask-Migrate

Ownership & Access Control

API Testing via Postman

🛠 Tech Stack

Python

Flask

Flask-SQLAlchemy

Flask-Migrate

SQLite

Postman

📌 API Screenshots
🔐 Login

📝 Create Ticket

🔄 Update Ticket

👨‍💼 Assign Ticket (Admin → Agent)

⚙ Setup Instructions
git clone <your-repo-link>
cd ticket_support_system_project
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
pip install -r requirements.txt
flask db upgrade
python run.py

📬 API Endpoints
Method	Endpoint	Description
POST	/auth/register	Register user
POST	/auth/login	Login
POST	/tickets	Create ticket
GET	/tickets	View my tickets
PUT	/tickets/<id>	Update ticket
DELETE	/tickets/<id>	Delete ticket
PUT	/tickets/<id>/assign	Assign ticket (Admin)
🧠 What I Learned

Flask App Factory pattern

Blueprint architecture

Database relationships

Role-based access control

Schema migration workflow

Secure API design

📌 Author

Viral Vaghasiya
Backend Developer (Flask)
