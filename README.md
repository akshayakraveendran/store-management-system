# Store Management System

Demo for a store management system and  purchase system

## Analysis

### Functional Requirements
- Backend - Python/Django
- RDBMS - SQLServer
- CRUD for Items
- CRUD for Inventory
- CRUD for Purchase
- Track shipping
- Everything should be stored in DB. DB is our single
  source of truth.
- Frontend: User friendly CRUD Frontend
- Frontend: Use CSS to make better user experience
- Rest API needed
- Validation and Error handling
  - HTTP Status 200 for CRUD Success with message
  - HTTP Status 400 for CRUD related user errors
  - HTTP Status 500 for internal errors

### Non Functional Requirements
- API security
- API latency
- UX (User Experience)
- Toast system for form submission and validation notifications


## Design/Mockups

### Initial design mockup for reference
![store-management-mockup](/library/store-management-mockup.jpg)

## Database Design
![DB Diagram](/library/store-management-db.jpg)

## Start Backend Server
```bash
python manage.py runserver
```