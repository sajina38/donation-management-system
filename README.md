# Donation Management System

A Django-based web application to manage donors, donations, expenses, and reports for organizations, charities, or NGOs.


## ✨ Features

- **Donor Management**
  - Register new donors with name, email, and contact.
  - View and manage donor list.

- **Donations**
  - Record donations (Cash, Bank, or Online).
  - Associate donations with events.
  - Track donation status (Pending / Confirmed).
  - Store and access donation receipts.
  - View list of all donations.

- **Expenses**
  - Record expenses with categories (Program, Admin, Other).
  - View and manage expense list.

- **Events**
  - Add and manage fundraising events.
  - Link donations to specific events.

- **Reports**
  - Total donations received.
  - Total expenses recorded.
  - Remaining funds available.

---


## 🛠️ Setup

## 1️⃣ Clone the repository
git clone https://github.com/your-username/donation-management-system
cd donation-management-system

## 2️⃣ Create virtual environment
python -m venv venv

## 3️⃣ Activate virtual environment
## On Windows:
.\venv\Scripts\activate
## On Linux/Mac:
source venv/bin/activate

## 4️⃣ Install dependencies
pip install -r requirements.txt

## 5️⃣ Setup database
python manage.py makemigrations
python manage.py migrate

## 6️⃣ Create superuser (for admin access)
python manage.py createsuperuser

## 7️⃣ Run development server
python manage.py runserver

## 8️⃣ Open in browser
## 👉 http://127.0.0.1:8000/

## 📂 Apps Structure:
## donors → manage donors
## donations → manage donations + reports
## expenses → manage expenses

# 📊 Sample Data Used in the Project

## Donors

Sajina Gurung | sajinagrg0@gmail.com
 | 9999328371

Jharana Gurung | jhagrg7@gmail.com
 | 9255328371

Sunita Poudel | sunitapdl6@gmail.com
 | 9123456797

## Donations

Aug. 13, 2025 → Sajina Gurung donated 10,000 via Bank (Status: Confirmed, Event: School Fund 2025)

Aug. 2, 2025 → Jharana Gurung donated 5,000 via Cash (Status: Pending, Event: Arts Festival Fund)

Aug. 29, 2025 → Sunita Poudel donated 50,000 via Online (Status: Confirmed, Event: School Fund 2025)

## Expenses

Aug. 29, 2025 → Program expense: Fund raise for school (50,000)

Aug. 29, 2025 → Admin expense: Supplies for fund management (6,000)