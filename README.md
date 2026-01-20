🎫 Ticket Support System API

A backend REST API built using Flask to manage customer support tickets with authentication, roles, priority handling, and ticket assignment.

🚀 Project Overview

This project simulates a real company support system where:

Users can create support tickets

Admin can assign tickets to agents

Agents can work on assigned tickets

Tickets have priority, category & status

All APIs are secured using token-based authentication

🛠 Tech Stack

Python

Flask

Flask SQLAlchemy (ORM)

Flask Migrate

SQLite

Postman (API Testing)

✨ Features

User Registration & Login

Token based authentication

Role system (User, Admin, Agent)

Ticket CRUD operations

Ticket Priority & Category

Ticket Assignment (Admin → Agent)

Created & Updated timestamps

Database migrations

📌 API Endpoints
Method	Endpoint	Description
POST	/auth/register	Register user
POST	/auth/login	Login
POST	/tickets	Create ticket
GET	/tickets	Get my tickets
PUT	/tickets/<id>	Update ticket
DELETE	/tickets/<id>	Delete ticket
PUT	/tickets/<id>/assign	Assign ticket (Admin only)
📸 API Screenshots
🔐 Login API
POST /auth/login


📝 Create Ticket API
POST /tickets


✏ Update Ticket API
PUT /tickets/<ticket_id>


👨‍💼 Assign Ticket API
PUT /tickets/<ticket_id>/assign


⚙ Setup Instructions
1️⃣ Clone Repository
git clone <your-repo-link>
cd ticket_support_system_project

2️⃣ Create Virtual Environment
python -m venv venv
venv\Scripts\activate

3️⃣ Install Dependencies
pip install -r requirements.txt

4️⃣ Run Migrations
flask db upgrade

5️⃣ Run Server
flask run


Server will start on
👉 http://127.0.0.1:5000

🧪 Testing

Use Postman to test all APIs.

📚 What I Learned

Flask project structure

Blueprints

SQLAlchemy ORM

Database migrations

Authentication & roles

API security

Real-world backend logic

👤 Author

Viral Vaghasiya
Backend Developer (Flask)
