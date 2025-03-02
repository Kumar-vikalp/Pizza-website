# Pizza Website

A Django-based web application for managing and displaying information about various pizzas. This project includes features such as user registration, login, pizza listing, and more. It is designed for learning and demonstration purposes.

---
## Deployed on KOyeb 
Live = https://eligible-ciel-punvers-43ec5b24.koyeb.app/home/

## Features

### User Features:
- **Home Page:** Welcome users and display general information about the website.
- **About Page:** Learn more about the purpose of the website.
- **User Registration:** Allow new users to sign up with their name, email, and password.
- **User Login:** Provide existing users access to their account.

### Pizza Management:
- **Pizza List:** View available pizzas, including name, description, type, and price.
- **Edit Pizza Details:** Modify pizza information such as name, type, or price.
- **Delete Pizza:** Remove pizzas from the database.

### Menu and Booking:
- **Menu Page:** Browse all available menu items, including pizzas, fries, pasta, and burgers.
- **Booking Page:** Reserve or book items from the menu.

---

## Tech Stack
- **Backend Framework:** Django (4.2.16)
- **Frontend:** HTML, CSS (managed via templates)
- **Database:** SQLite3
- **Media Handling:** Support for uploading and displaying pizza images.

---

## Installation

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/Kumar-vikalp/Pizza-website.git
   cd Pizza-website
2. **Set Up Virtual Environment:**
   ```bash
   python -m venv pizza_env
   source pizza_env/bin/activate
3. **Install Dependencies:
   ````bash
   pip install -r requirements.txt
4. **Apply Migrations:**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
5. **Run Development Server:**
   ```bash
   python manage.py runserver

Visit http://127.0.0.1:8000/home/ in your web browser to access the website.

## Pizza-website/
   ```bash
   |
   |-- Pizza_app/               # Core application for pizza-related features
   |-- templates/               # HTML templates
   |-- static/                  # Static files (CSS, JS, Images)
   |-- media/                   # Uploaded media files
   |-- db.sqlite3               # Database file
   |-- manage.py                # Django's command-line utility
   |-- pizza/                   # Project configuration
   |-- pizza_env/               # Virtual environment (excluded in .gitignore)
   |-- requirements.txt         # Dependencies for the project
   ```
## Models
   ```bash
   Pizza
   Stores pizza-related details:
   name: Name of the pizza.
   description: Description of the pizza.
   type: Type of item (e.g., pizza, fries, burger, pasta).
   rate: Price of the item.
   pizza_picture: Image of the pizza.
   ```
## URLs
   ```bash

    Path	     Description
    /home/ 	     Home page
    /about/	     About page
    /register/	 User registration
    /login/	     User login
    /pizza/	     List of all pizzas
    /menu/	     View menu items
    /book/	     Book menu items
    ```

## Future Enhancements

        Add authentication using Django's User model.
        Improve UI using modern frameworks like Bootstrap.
        Add a cart and order management system.
        Integrate payment gateways.

