🏋️‍♀️ Gym Website
Welcome to the Gym Website!
A Django-based web application designed to manage gym memberships, plans, bookings, and more.

📌 Project Features
🏠 Modern Home Page with a hero section for attention-grabbing content

📋 Membership Plans with dynamic pricing and details

🗓️ Join Now Form with Razorpay payment integration for easy sign-ups

📊 Admin Dashboard (with the Jazzmin theme) for smooth management

🔍 Search & Filter capabilities for efficient plan/order lookup

📦 Order Management backed by MySQL database for scalability

📸 CKEditor Support for rich text editing in the admin panel

📂 Static & Media File Handling for images, documents, and other assets

🖥️ Local Development Setup
Follow these steps to run the project on your local machine:

✅ 1️⃣ Clone the Repository
bash
Copy
Edit
git clone https://github.com/puja138/gym_website.git
cd gym_website
✅ 2️⃣ Create a Virtual Environment
For Windows:

bash
Copy
Edit
python -m venv venv
venv\Scripts\activate
For macOS/Linux:

bash
Copy
Edit
python -m venv venv
source venv/bin/activate
✅ 3️⃣ Install Required Packages
bash
Copy
Edit
pip install -r requirements.txt
✅ 4️⃣ Create a .env File
Add the following lines to your .env file:

ini
Copy
Edit
SECRET_KEY=your_secret_key_here
DEBUG=True
✅ 5️⃣ Apply Database Migrations
bash
Copy
Edit
python manage.py migrate
✅ 6️⃣ Create a Superuser
bash
Copy
Edit
python manage.py createsuperuser
✅ 7️⃣ Run the Development Server
bash
Copy
Edit
python manage.py runserver
Open your browser and go to http://127.0.0.1:8000/ to view the site.

Admin Panel: http://127.0.0.1:8000/admin/

🚀 Optional: Deployment Guide
🌍 Deploying on Render:
Create a New Web Service on Render and link your GitHub repository.

Set Build Command:

bash
Copy
Edit
pip install -r requirements.txt && python manage.py collectstatic --noinput && python manage.py migrate
Set Start Command:

bash
Copy
Edit
gunicorn gym_website.wsgi:application
Add Environment Variables on Render:
SECRET_KEY

DEBUG=False

ALLOWED_HOSTS → Set this to your Render domain

DATABASE_URL → Use Render's Postgres DB URL

RAZORPAY_KEY_ID & RAZORPAY_KEY_SECRET (if payments are enabled)

✅ Done! Your site will auto-deploy after each commit.

📌 Tech Stack
Python 3.10+

Django 5.2

MySQL / PostgreSQL (for production)

Razorpay API (for payment integration)

Jazzmin (for styled admin panel)

Gunicorn (for production server)

Whitenoise (for serving static files in production)

📬 Contact
If you have any questions or need help:

📧 Email: pbarman80637@example.com

💼 Fiverr: your-fiverr-profile

Happy Lifting! 💪
Built with ❤️ by Puja

