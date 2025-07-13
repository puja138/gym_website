# 🏋️‍♀️ Gym Website

Welcome to the Gym Website!  
This is a Django-based web application for managing gym memberships, plans, bookings, and more.

---

## 📌 **Project Features**

- 🏠 Modern Home Page with hero section
- 📋 Membership Plans with dynamic details
- 🗓️ Join Now form with Razorpay Payment Integration
- 📊 Admin  (Jazzmin theme)
- 🔍 Search & Filter for plans/orders
- 📦 Order Management with MySQL Database
- 📸 CKEditor support for rich text editing
- 📂 Static & Media file handling

---

## 🖥️ **Local Development Setup**

Follow these steps to run the project on your local machine:

### ✅ 1️⃣ Clone the Repository
```bash
git clone https://github.com/puja138/gym_website.git
cd gym_website

✅ 2️⃣ Create Virtual Environment
bash
Copy
Edit
python -m venv venv
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate

✅ 3️⃣ Install Requirements
bash
Copy
Edit
pip install -r requirements.txt
✅ 4️⃣ Create .env file
Add these lines in .env:
ini
Copy
Edit
SECRET_KEY=your_secret_key_here
DEBUG=True

✅ 5️⃣ Apply Migrations
bash
Copy
Edit
python manage.py migrate

✅ 6️⃣ Create Superuser
bash
Copy
Edit
python manage.py createsuperuser

✅ 7️⃣ Run the Development Server
bash
Copy
Edit
python manage.py runserver
🔗 Open http://127.0.0.1:8000/ in your browser.
🔗 Admin Panel: http://127.0.0.1:8000/admin/

🚀 Optional: Deployment Guide
🌍 If you want to deploy on Render:
Create a new Web Service on Render.

Connect your GitHub repository.

Build Command:

bash
Copy
Edit
pip install -r requirements.txt && python manage.py collectstatic --noinput && python manage.py migrate
Start Command:

bash
Copy
Edit
gunicorn gym_website.wsgi:application
Add Environment Variables:

SECRET_KEY

DEBUG=False

ALLOWED_HOSTS → Use your Render domain

DATABASE_URL → Use Render's Postgres DB URL

RAZORPAY_KEY_ID & RAZORPAY_KEY_SECRET if payments are enabled

✅ Done! Your site will auto-deploy after each commit.

📌 Tech Stack
Python 3.10+

Django 5.2

MySQL / PostgreSQL (for production)

Razorpay API (for payment integration)

Jazzmin (for styled admin)

Gunicorn, Whitenoise (for production)

📬 Contact
If you have any questions or need help:
📧 Email: 
💼 Fiverr:

Happy Lifting! 💪
Built with ❤️ by Puja

yaml
Copy
Edit

---
