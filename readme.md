# Django REST API for E-commerce Application
    A comprehensive and user-friendly API for an online store built with Django REST Framework. This project allows users to view products, add them to their shopping cart, and place orders. Administrators can manage products, categories, orders, and users through the admin panel.


## Prerequisites

Before you begin, ensure that you have the following installed:

- Python 3.11
- Django 5.1 or higher
- Django REST Framework
- Virtualenv (optional but recommended)

## Installation

To set up the project on your local machine, follow these steps:

1. **Clone the repository:**
   ```bash
   git clone https://github.com/mohammd-1819/ecommerce_api.git


2. **Create and activate a virtual environment:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate


3. **Install the required dependencies:**
   ```bash
    pip install -r requirements.txt


4. **Apply the migrations:**
   ```bash
    python manage.py migrate


5. **Create a superuser for the admin panel (optional but recommended):**
   ```bash
    python manage.py createsuperuser
    default is: admin@gmail.com
    password : admin

6. **Run the development server:**
    ```bash
    python manage.py runserver


7. **Access the application:**
    Open your browser and go to http://127.0.0.1:8000/ for the main page


## Features
    User registration and login
    Add products to the shopping cart and manage the cart
    Admin panel to manage products, orders, users,...
    Product pagination
    Comment system for each product (authenticated users only)
    Review system for all products


## Usage
    Once the server is running, users can browse through products add items to their cart, and proceed to checkout. Administrators can add, edit, and delete products, as well as manage orders from the admin panel.


## Managing Products
    Only admin users can create new products. Products can be categorized and have attributes like price, description, and stock status.


## Technologies Used
    Backend: Django restframework
    Database: PostgreSQL
    Authentication: Customized Django built-in authentication system
    

## Author
    https://github.com/mohammd-1819