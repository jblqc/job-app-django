

# SimpleStock Portfolio API

A Django REST Framework project for managing stocks, orders, and calculating total portfolio value. Supports CRUD operations, pagination, and Swagger API documentation.

---

## Features

* Add, update, and delete Stocks
* Place Orders to buy stocks
* Retrieve Order history
* View Portfolio Summary with total value
* Custom pagination (items per page, current page)
* API documentation using Swagger (drf\_yasg)

---

## Tech Stack

* Python 3.10+
* Django 4.x
* Django REST Framework
* drf\_yasg (Swagger)
* SQLite (default)

---

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/jblqc/job-app-django.git
   cd job-app-django
   ```

2. (Optional but recommended) Create and activate a virtual environment:

   ```bash
   python -m venv venv
   source venv/bin/activate    # Linux/macOS
   .\venv\Scripts\activate     # Windows
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Run migrations:

   ```bash
   python manage.py migrate
   ```

5. Run the development server:

   ```bash
   python manage.py runserver
   ```

6. Open your browser and go to:

   ```
   http://127.0.0.1:8000/swagger/
   ```

   to view the API documentation.

---

## Additional Info

* The **answer to the technical exam Part 1** (with sample usage and explanations) is provided in the file:

  ```
  technical_exam_part1_solution.py
  ```

* Feel free to clone the project from my GitHub repo:

  ```
  https://github.com/jblqc/job-app-django.git
  ```

---
