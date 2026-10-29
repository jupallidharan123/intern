import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'hostel_management.settings')
django.setup()

from hostels.models import Hostel, Room, Facility

# 1. Add specific College Facilities
college_facilities = [
    ('College Campus Shuttle', 'bi-bus-front', 'Free scheduled shuttle van directly to university campus gates'),
    ('24/7 Silent Study Library', 'bi-journal-bookmark-fill', 'Air-conditioned silent study hall with individual power desks'),
    ('4-Time College Mess Plan', 'bi-egg-fried', 'Nutritious breakfast, lunch, evening snacks/tea, and dinner buffet'),
    ('Biometric Attendance & Curfew', 'bi-fingerprint', 'Automated parent SMS notification on night entry / 9:30 PM curfew'),
    ('Sports Court & Table Tennis', 'bi-trophy', 'Badminton court, table tennis room, and indoor recreation games'),
]

f_objs = {}
for name, icon, desc in college_facilities:
    obj, _ = Facility.objects.get_or_create(name=name, defaults={'icon_class': icon, 'description': desc})
    f_objs[name] = obj

all_facs = {f.name: f for f in Facility.objects.all()}

# 2. Dedicated College Student Hostels
college_hostels = [
    {
        'name': 'Apex University Campus Boys Hostel',
        'hostel_type': 'boys',
        'address': 'Gate No. 3, Near Engineering Block, University Road, Indiranagar',
        'city': 'Bangalore',
        'state': 'Karnataka',
        'pincode': '560038',
        'landmark': 'Adjacent to University Main Library & Tech Park',
        'phone': '+91 80 2345 6789',
        'email': 'apex.college@stayease.com',
        'warden': 'Prof. M. S. Raghavan (Faculty Warden)',
        'description': 'Apex University Campus Boys Hostel is officially recognized student accommodation situated right next to the university gate. Tailored specifically for undergraduate, postgraduate, and engineering students. Features a 24/7 silent study hall, high-speed campus LAN, delicious 4-time mess food, daily laundry service, and strict anti-ragging security.',
        'rules': 'College ID card mandatory at entry. Night curfew at 9:30 PM with biometric punch. Study hours strictly observed from 8:00 PM to 10:00 PM. No loud music during exam weeks.',
        'image': 'https://images.unsplash.com/photo-1541339907198-e08756dedf3f?auto=format&fit=crop&w=1200&q=80',
        'facilities': ['High-Speed WiFi', 'Delicious Meals & Mess', '24/7 Power Backup', 'CCTV & Biometric Security', '24/7 Silent Study Library', '4-Time College Mess Plan', 'College Campus Shuttle'],
        'rooms': [
            {
                'num': 'C-101', 'floor': 1, 'type': 'single', 'cap': 1, 'price': 11000, 'daily': 550, 'ac': True, 'wash': True, 'bal': True,
                'desc': 'Single Private Scholar Room: Dedicated wooden study desk, ergonomic mesh chair, bookshelf, AC, attached private bathroom, and high-speed LAN.',
                'img': 'https://images.unsplash.com/photo-1595526114035-0d45ed16cfbf?auto=format&fit=crop&w=800&q=80'
            },
            {
                'num': 'C-102', 'floor': 1, 'type': 'double', 'cap': 2, 'price': 7500, 'daily': 400, 'ac': True, 'wash': True, 'bal': False,
                'desc': '2-Sharing University Room: Dual separate study desks with reading lamps, twin wardrobes, attached bathroom, and personal lockers.',
                'img': 'https://images.unsplash.com/photo-1560448204-e02f11c3d0e2?auto=format&fit=crop&w=800&q=80'
            },
            {
                'num': 'C-201', 'floor': 2, 'type': 'triple', 'cap': 3, 'price': 5800, 'daily': 320, 'ac': False, 'wash': True, 'bal': True,
                'desc': '3-Sharing Student Room: Spacious ventilated room with 3 individual study stations, high-speed ceiling fans, and balcony.',
                'img': 'https://images.unsplash.com/photo-1582719478250-c89cae4dc85b?auto=format&fit=crop&w=800&q=80'
            },
            {
                'num': 'C-202', 'floor': 2, 'type': 'four', 'cap': 4, 'price': 4500, 'daily': 250, 'ac': False, 'wash': True, 'bal': False,
                'desc': '4-Sharing Budget College Dorm: Budget student accommodation with sturdy wooden bunk beds, individual power sockets, and under-bed secure storage.',
                'img': 'https://images.unsplash.com/photo-1540518614846-7ede433c4ef4?auto=format&fit=crop&w=800&q=80'
            }
        ]
    },
    {
        'name': "St. Xavier's Girls College Residency",
        'hostel_type': 'girls',
        'address': 'Campus Enclave, Near Medical & Arts College, Viman Nagar',
        'city': 'Pune',
        'state': 'Maharashtra',
        'pincode': '411014',
        'landmark': "500m from Xavier Women's College Campus",
        'phone': '+91 20 2789 1234',
        'email': 'stxaviers.girls@stayease.com',
        'warden': 'Dr. Sister Mary Thomas & Mrs. Sunita Rao',
        'description': "St. Xavier's Girls College Residency provides a warm, disciplined, and secure home away from home for college students. Full biometric access, warden support, on-campus doctor on call, hot nutritious home-style meals, laundry facilities, and serene study spaces.",
        'rules': 'College gate timings: 9:00 PM. Parents SMS verification for weekend leave passes. Strictly smoke-free and alcohol-free campus environment.',
        'image': 'https://images.unsplash.com/photo-1523240795612-9a054b0db644?auto=format&fit=crop&w=1200&q=80',
        'facilities': ['High-Speed WiFi', 'Air Conditioning', 'Delicious Meals & Mess', 'CCTV & Biometric Security', 'Biometric Attendance & Curfew', '24/7 Silent Study Library', 'Laundry & Washing Machine'],
        'rooms': [
            {
                'num': 'SX-101', 'floor': 1, 'type': 'single', 'cap': 1, 'price': 12500, 'daily': 650, 'ac': True, 'wash': True, 'bal': True,
                'desc': 'Premium Single Student Room: Quiet study ambiance, book shelves, personal study desk, wardrobe, and attached washroom.',
                'img': 'https://images.unsplash.com/photo-1513694203232-719a280e022f?auto=format&fit=crop&w=800&q=80'
            },
            {
                'num': 'SX-102', 'floor': 1, 'type': 'double', 'cap': 2, 'price': 8500, 'daily': 450, 'ac': True, 'wash': True, 'bal': True,
                'desc': '2-Sharing Deluxe Study Room: Twin beds with orthopedic mattresses, two study tables with pin boards, and attached bath.',
                'img': 'https://images.unsplash.com/photo-1590490360182-c33d57733427?auto=format&fit=crop&w=800&q=80'
            },
            {
                'num': 'SX-201', 'floor': 2, 'type': 'triple', 'cap': 3, 'price': 6200, 'daily': 350, 'ac': False, 'wash': True, 'bal': False,
                'desc': '3-Sharing Standard College Room: 3 student beds, shared study table, individual wardrobes, hot water geyser in bathroom.',
                'img': 'https://images.unsplash.com/photo-1566665797739-1674de7a421a?auto=format&fit=crop&w=800&q=80'
            },
            {
                'num': 'SX-202', 'floor': 2, 'type': 'four', 'cap': 4, 'price': 4800, 'daily': 280, 'ac': False, 'wash': True, 'bal': True,
                'desc': '4-Sharing College Dorm Room: Budget friendly for outstation college students with individual study cubicles and daily housekeeping.',
                'img': 'https://images.unsplash.com/photo-1582719508461-905c673771fd?auto=format&fit=crop&w=800&q=80'
            }
        ]
    },
    {
        'name': 'Scholars Valley Co-Ed University Campus Hostel',
        'hostel_type': 'coliving',
        'address': 'Academic City Phase 1, Gachibowli, Near IIIT & University of Hyderabad',
        'city': 'Hyderabad',
        'state': 'Telangana',
        'pincode': '500032',
        'landmark': 'Opposite University Sports Complex',
        'phone': '+91 40 3344 5566',
        'email': 'scholarsvalley@stayease.com',
        'warden': 'Mr. K. V. Ramanathan',
        'description': 'Modern student hostel community serving university scholars, research scholars, and college students. Includes state-of-the-art study lounges, cafeteria, high-speed WiFi, gym, debate club room, and college shuttle connectivity.',
        'rules': 'College student ID verification required during booking. Maintain silence in study zones. Gate closing time 10:30 PM.',
        'image': 'https://images.unsplash.com/photo-1562774053-701939374585?auto=format&fit=crop&w=1200&q=80',
        'facilities': ['High-Speed WiFi', 'Delicious Meals & Mess', '24/7 Power Backup', 'CCTV & Biometric Security', '24/7 Silent Study Library', 'Sports Court & Table Tennis', 'College Campus Shuttle'],
        'rooms': [
            {
                'num': 'SV-101', 'floor': 1, 'type': 'single', 'cap': 1, 'price': 13000, 'daily': 680, 'ac': True, 'wash': True, 'bal': True,
                'desc': 'Single Scholar Suite: Dedicated high-speed fiber port, study table with bookshelf, air conditioning, and attached washroom.',
                'img': 'https://images.unsplash.com/photo-1616594039964-ae9021a400a0?auto=format&fit=crop&w=800&q=80'
            },
            {
                'num': 'SV-102', 'floor': 1, 'type': 'double', 'cap': 2, 'price': 8900, 'daily': 480, 'ac': True, 'wash': True, 'bal': True,
                'desc': '2-Sharing Student Room: Ergonomic study chairs, dual study stations, wardrobes, attached private washroom.',
                'img': 'https://images.unsplash.com/photo-1505691938895-1758d7feb511?auto=format&fit=crop&w=800&q=80'
            },
            {
                'num': 'SV-201', 'floor': 2, 'type': 'four', 'cap': 4, 'price': 5200, 'daily': 300, 'ac': True, 'wash': True, 'bal': False,
                'desc': '4-Sharing University Dorm: Air-conditioned bunk bed dorm with individual study desks, lockers, and high-speed WiFi.',
                'img': 'https://images.unsplash.com/photo-1540518614846-7ede433c4ef4?auto=format&fit=crop&w=800&q=80'
            }
        ]
    }
]

created_count = 0
for hdata in college_hostels:
    hostel, created = Hostel.objects.get_or_create(
        name=hdata['name'],
        defaults={
            'hostel_type': hdata['hostel_type'],
            'address': hdata['address'],
            'city': hdata['city'],
            'state': hdata['state'],
            'pincode': hdata['pincode'],
            'landmark': hdata['landmark'],
            'contact_phone': hdata['phone'],
            'contact_email': hdata['email'],
            'warden_name': hdata['warden'],
            'description': hdata['description'],
            'rules_and_regulations': hdata['rules'],
            'featured_image': hdata['image'],
            'total_floors': 3,
            'is_active': True,
        }
    )
    for fname in hdata['facilities']:
        if fname in all_facs:
            hostel.facilities.add(all_facs[fname])
        elif fname in f_objs:
            hostel.facilities.add(f_objs[fname])
            
    for r in hdata['rooms']:
        Room.objects.get_or_create(
            hostel=hostel,
            room_number=r['num'],
            defaults={
                'floor': r['floor'],
                'room_type': r['type'],
                'capacity': r['cap'],
                'total_beds': r['cap'],
                'price_per_month': r['price'],
                'price_per_day': r['daily'],
                'is_ac': r['ac'],
                'has_attached_washroom': r['wash'],
                'has_balcony': r['bal'],
                'description': r['desc'],
                'image_url': r['img'],
                'is_available': True,
            }
        )
    created_count += 1
    print(f'Configured College Hostel: {hostel.name} ({hostel.city}) with {len(hdata["rooms"])} rooms.')

print(f'Successfully added {created_count} College Hostels with full room inventories.')

