#  MaVieEtudiante

A full-stack student life management dashboard built with **Django** and **Tailwind CSS**.

It helps students organize and track their academic life in one place.

---

##  Live Demo
 https://mavieetudiante-2.onrender.com

---

## Features

-  User authentication (login / register)
-  Dashboard with analytics
  - Average grades calculation
  - Attendance percentage
- Grade management system
-  Revision planner
  - Tasks (Done / Pending / Overdue)
  - Add / Delete / Toggle status
-  Budget tracking (income & expenses UI)
-  Modern responsive UI with Tailwind CSS

---

## Tech Stack

- Django (Python backend)
- SQLite (development) / PostgreSQL (production)
- Tailwind CSS
- HTML templates

---


---

##  Installation (Local Setup)

```bash
git clone https://github.com/aouichaoui-eya/mavieetudiante.git
cd mavieetudiante

python -m venv venv
venv\Scripts\activate   # Windows

pip install -r requirements.txt

python manage.py migrate
python manage.py runserver