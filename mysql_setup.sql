-- ==============================================================================
-- StayEase: Hostel Booking and Management System - MySQL Database Setup Script
-- ==============================================================================

-- 1. Create the MySQL Database with UTF-8 character encoding
CREATE DATABASE IF NOT EXISTS `hostel_db`
    CHARACTER SET utf8mb4
    COLLATE utf8mb4_unicode_ci;

USE `hostel_db`;

-- 2. Verify privileges or create dedicated application user (Optional)
-- CREATE USER IF NOT EXISTS 'hostel_user'@'localhost' IDENTIFIED BY 'hostel_pass123';
-- GRANT ALL PRIVILEGES ON `hostel_db`.* TO 'hostel_user'@'localhost';
-- FLUSH PRIVILEGES;

-- ==============================================================================
-- Django Schema Overview:
-- Running 'python manage.py migrate' will automatically create and sync all tables:
--
-- 1. auth_user
--    - id (INT AUTO_INCREMENT PRIMARY KEY)
--    - username, email, password (hashed with PBKDF2/SHA256), first_name, last_name, is_staff
--
-- 2. hostels_userprofile
--    - id (BIGINT AUTO_INCREMENT PRIMARY KEY)
--    - user_id (INT UNIQUE FK -> auth_user.id ON DELETE CASCADE)
--    - phone_number, user_type (student/professional/admin), address, city, emergency_contact, id_proof_type, id_proof_number
--
-- 3. hostels_facility
--    - id (BIGINT AUTO_INCREMENT PRIMARY KEY)
--    - name (VARCHAR UNIQUE), icon_class, description
--
-- 4. hostels_hostel
--    - id (BIGINT AUTO_INCREMENT PRIMARY KEY)
--    - name, slug (VARCHAR UNIQUE), hostel_type (boys/girls/coliving), address, city, state, pincode, landmark, contact_phone, contact_email, warden_name, description, rules_and_regulations, featured_image, is_active, created_at, updated_at
--
-- 5. hostels_hostel_facilities (ManyToMany Relationship)
--    - id (BIGINT AUTO_INCREMENT PRIMARY KEY)
--    - hostel_id (BIGINT FK -> hostels_hostel.id)
--    - facility_id (BIGINT FK -> hostels_facility.id)
--
-- 6. hostels_room
--    - id (BIGINT AUTO_INCREMENT PRIMARY KEY)
--    - hostel_id (BIGINT FK -> hostels_hostel.id ON DELETE CASCADE)
--    - room_number (VARCHAR), floor (INT), room_type (single/double/triple/four), capacity (INT), total_beds (INT), price_per_month (DECIMAL), price_per_day (DECIMAL), is_ac (BOOLEAN), has_attached_washroom (BOOLEAN), has_balcony (BOOLEAN), is_available (BOOLEAN)
--    - UNIQUE KEY (`hostel_id`, `room_number`)
--
-- 7. hostels_booking
--    - id (BIGINT AUTO_INCREMENT PRIMARY KEY)
--    - booking_id (VARCHAR UNIQUE, e.g. 'HST-2026-A1B2C')
--    - user_id (INT FK -> auth_user.id ON DELETE CASCADE)
--    - room_id (BIGINT FK -> hostels_room.id ON DELETE CASCADE)
--    - check_in (DATE), check_out (DATE), duration_days (INT), total_amount (DECIMAL), advance_amount (DECIMAL), remaining_amount (DECIMAL), status (pending/confirmed/cancelled/completed), guest_name, guest_phone, guest_email, emergency_contact, special_requests, created_at, updated_at
--
-- 8. hostels_payment
--    - id (BIGINT AUTO_INCREMENT PRIMARY KEY)
--    - transaction_id (VARCHAR UNIQUE, e.g. 'PAY-123456')
--    - booking_id (BIGINT FK -> hostels_booking.id ON DELETE CASCADE)
--    - payment_method (upi/card/netbanking/cash), payment_type (advance/full/remaining), amount (DECIMAL), status (success/pending/failed), card_last4, upi_id, bank_name, payment_date
--
-- 9. hostels_review
--    - id (BIGINT AUTO_INCREMENT PRIMARY KEY)
--    - hostel_id (BIGINT FK -> hostels_hostel.id ON DELETE CASCADE)
--    - user_id (INT FK -> auth_user.id ON DELETE CASCADE)
--    - rating (INT 1-5), title (VARCHAR), comment (TEXT), is_approved (BOOLEAN), created_at
--    - UNIQUE KEY (`hostel_id`, `user_id`)
-- ==============================================================================

