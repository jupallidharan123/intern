# StayEase - Hostel Booking and Management System

A full-stack, responsive, and secure web application designed for students, working professionals, and hostel administrators. StayEase allows residents to search for hostels, verify amenities and room types, check live bed availability, make reservations with simulated payments, and track their bookings. It also provides administrators with a dedicated dashboard to manage properties, rooms, approvals, and revenue analytics.

---

## 1. Technology Stack

- **Frontend:** HTML5, CSS3, JavaScript (ES6+), Bootstrap 5, Bootstrap Icons.
- **Backend:** Python 3.12+, Django (Model-View-Template Architecture).
- **Database:** MySQL (configured with PyMySQL connector; auto-fallback to SQLite for zero-config local testing).
- **Authentication:** Django Authentication with PBKDF2/SHA256 password hashing, session-based auth, and role-based permissions (`student`, `professional`, `admin`).
- **Payment:** Simulated payment gateway supporting UPI / QR Code, Credit/Debit Cards, Net Banking, and Cash at Desk.

---

## 2. Key Modules & Features

### 👤 User Module
- **Registration & Authentication:** Sign up with name, email, phone, role (Student / Working Professional), and password. Login supporting either username or email.
- **Profile Management:** View and edit personal details, phone, emergency contact, permanent address, and government ID proof.
- **Forgot Password Simulator:** Interactive demo simulation with token generation and password reset.

### 🔍 Hostel Search & Discovery
- **Multi-Parameter Search:** Search by city, location / landmark, hostel type, and keyword.
- **Filters:** Boys' Hostel, Girls' Hostel, Co-living spaces, room sharing type (Single, Double, Triple, Quad), budget min/max, and amenities.
- **Rich Hostel Details:** Image gallery, detailed description, house rules, gate timings, warden contact details, and list of amenities with icons.

### 🛏️ Room Booking & Double-Booking Prevention
- **Real-Time Availability Engine:** Calculates active overlapping bookings for chosen dates (`check_in` < `existing.check_out` AND `check_out` > `existing.check_in`).
- **Live Pricing Calculation:** Live AJAX calculation of monthly/daily rent, duration in days and months, 25% advance deposit, and balance due.
- **Instant Booking Confirmation:** Generates a unique, verifiable Booking ID (e.g., `HST-2026-9A4B12`).
- **Printable Booking Receipt:** Formatted printable and downloadable voucher with payment breakdown, guest info, and hostel check-in instructions.
- **Cancellation Management:** Residents can cancel reservations with cancellation reason recording and immediate bed release.

### 💳 Simulated Payment Gateway
- **Realistic Payment Options:**
  - UPI / QR Code scanning & VPA entry (`user@upi`).
  - Credit / Debit Card (Card number, Expiry, CVV).
  - Net Banking with major Indian banks.
  - Cash at Reception Desk (Pay on Arrival).
- **Test Mode Toggle:** Simulate both **Approved (Success)** and **Declined (Failure)** transactions to test validation.
- **Receipt Generation:** Automatically creates transaction logs with unique IDs (`PAY-XXXXX`).

### 📊 Resident Dashboard
- Summary statistics: Total reservations, Active stays, Completed stays, Total spent.
- Active stay highlight card with 1-click receipt access.
- Filterable booking history (Confirmed, Pending, Cancelled, Completed).
- Post verified reviews and ratings (1 to 5 stars) after a stay.

### 🛠️ Admin Management Module (`/admin-dashboard/`)
- **Executive Analytics:** Total hostels, total rooms, total bed capacity, available beds, pending booking requests, total revenue collected, and total registered users.
- **Hostel CRUD:** Add new hostels, edit details, upload photo URLs, configure facilities, and toggle active status.
- **Room & Bed Inventory:** Add/edit rooms, floor numbers, room types, bed capacities, monthly/daily prices, AC/Non-AC, and attached bathrooms.
- **Booking Approvals:** View all bookings, approve pending requests with 1 click, reject or mark completed.
- **Payment Logs:** Complete audit trail of all online and desk transactions.
- **Occupancy Reports:** Visual progress bars displaying bed utilization rates and revenue generated per property.

---

## 3. Project Directory Structure

```text
intern proje/
├── hostel_management/            # Django Project Settings & Root URLs
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py              # MySQL & SQLite hybrid configuration
│   ├── urls.py                  # Project-level routing
│   └── wsgi.py
├── hostels/                      # Main Application
│   ├── management/
│   │   └── commands/
│   │       └── seed_data.py     # Database seeder with realistic test data
│   ├── migrations/              # Database migration files
│   ├── admin.py                 # Django standard admin registrations
│   ├── apps.py
│   ├── context_processors.py    # Global cities and branding context
│   ├── forms.py                 # Forms with validation
│   ├── models.py                # Database models (Hostel, Room, Booking, etc.)
│   ├── tests.py                 # Automated unit and integration test suite
│   ├── urls.py                  # App URL endpoints
│   └── views.py                 # Core business logic and controllers
├── static/                       # Static Assets
│   ├── css/
│   │   └── style.css            # Custom responsive CSS with CSS variables
│   └── js/
│       └── main.js              # Availability calculator, gallery, alerts
├── templates/                    # HTML Templates (Bootstrap 5)
│   ├── base.html                # Global layout with navbar & footer
│   └── hostels/
│       ├── home.html            # Modern landing page with hero search
│       ├── hostel_list.html     # Search & filter listings page
│       ├── hostel_detail.html   # Property details, rooms, gallery, reviews
│       ├── about.html           # About StayEase
│       ├── contact.html         # Inquiry and support contact
│       ├── auth/
│       │   ├── login.html       # Login with 1-click test credentials
│       │   ├── register.html    # Registration with password hashing
│       │   ├── forgot_password.html
│       │   └── reset_password.html
│       ├── booking/
│       │   ├── book_room.html   # Date selection & guest details
│       │   ├── payment_gateway.html # Simulated demo payment gateway
│       │   ├── booking_receipt.html # Printable booking confirmation
│       │   └── cancel_booking.html
│       ├── user/
│       │   ├── dashboard.html   # Resident dashboard with metrics
│       │   ├── my_bookings.html # Booking history and receipts
│       │   └── profile.html     # User profile update
│       └── admin/
│           ├── dashboard.html   # Admin KPI dashboard & quick actions
│           ├── hostel_list.html # Manage hostels
│           ├── hostel_form.html # Add / Edit hostel
│           ├── room_list.html   # Manage rooms and bed inventory
│           ├── room_form.html   # Add / Edit room
│           ├── booking_list.html# Approve/reject bookings
│           ├── payment_list.html# Transaction logs
│           ├── user_list.html   # Customer list
│           ├── reports.html     # Occupancy analytics
│           └── confirm_delete.html
├── manage.py
├── mysql_setup.sql              # MySQL schema & database creation script
├── requirements.txt             # Python dependencies
└── README.md                    # Project documentation
```

---

## 4. Setup & Running in VS Code

### Step 1: Open the Project in VS Code
1. Open VS Code.
2. Go to **File -> Open Folder...** and select this directory (`intern proje`).
3. Open the integrated terminal (`Ctrl + ~` or **Terminal -> New Terminal**).

### Step 2: Install Dependencies
Ensure Python 3.10+ is installed, then run:
```bash
pip install -r requirements.txt
```

### Step 3: Database Setup

#### Option A: Run with SQLite (Zero-Config / Out of the Box)
The application has built-in auto-detection: if MySQL is not running locally, it seamlessly and gracefully runs on SQLite without crashing.
```bash
python manage.py migrate
python manage.py seed_data
```

#### Option B: Run with MySQL
1. Make sure your MySQL Server (e.g., XAMPP, WampServer, or MySQL Server) is running on port `3306`.
2. Open MySQL CLI or phpMyAdmin and execute:
   ```sql
   CREATE DATABASE IF NOT EXISTS `hostel_db` CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
   ```
   *(Or run the provided `mysql_setup.sql` script).*
3. If your MySQL credentials differ from the defaults (`root` / no password), set environment variables:
   ```powershell
   $env:DB_USER="root"
   $env:DB_PASSWORD="your_password"
   $env:DB_NAME="hostel_db"
   $env:DB_HOST="127.0.0.1"
   $env:DB_PORT="3306"
   ```
4. Run migrations and seed data:
   ```bash
   python manage.py migrate
   python manage.py seed_data
   ```

### Step 4: Run the Development Server
```bash
python manage.py runserver
```
Open your browser and navigate to:
👉 **`http://127.0.0.1:8000/`**

---

## 5. Sample User Login Details

The database seeder automatically creates the following accounts:

| Role | Username | Password | Email | Purpose |
|---|---|---|---|---|
| **Super Administrator** | `admin` | `admin123` | `admin@stayease.com` | Full access to Admin Dashboard (`/admin-dashboard/`) and Django Admin (`/admin/`) |
| **Student Resident** | `rahul` | `user123` | `rahul.sharma@example.com` | Test student bookings, receipt viewing, reviews |
| **Working Professional** | `priya` | `user123` | `priya.patel@example.com` | Test professional bookings in Pune PG |
| **Resident Resident** | `ananya` | `user123` | `ananya.v@example.com` | Test co-living bookings in Hyderabad |

*(Tip: On the Login page `/login/`, you can click the quick demo buttons to auto-fill these credentials instantly!)*

---

## 6. Running Automated Tests

To run the comprehensive test suite (covers homepage, search filtering, double-booking prevention, payment flow, and admin access restrictions):
```bash
python manage.py test
```
All tests should pass with `OK`.

---

## 7. Security Features Implemented

1. **Password Hashing:** Passwords are never stored in plain text; Django's PBKDF2 algorithm with SHA256 hashing is enforced.
2. **CSRF Protection:** All POST forms include `{% csrf_token %}` to prevent Cross-Site Request Forgery.
3. **Role-Based Access Control:** Admin views are protected with `@login_required` and `@user_passes_test(is_admin_or_staff)`. Regular users cannot view admin pages.
4. **Double-Booking Validation:** Bed availability is recalculated against date intervals before any booking is created or confirmed.
5. **Clean Session Management:** Secure login and logout with proper session cleanup.

