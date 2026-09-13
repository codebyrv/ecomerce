# 🛒 RvStore – Django E-commerce Website

RvStore is a full-stack **E-commerce web application** built using **Python and Django**.
The project provides essential online shopping features such as user authentication, product browsing, cart management, checkout, and order tracking.

## 🚀 Features

* 👤 User Registration & Login
* 🔐 User Authentication
* 🛍️ Product Listing
* 📂 Product Categories
* 📦 Product Details
* 🛒 Add to Cart
* ➕ Increase Cart Quantity
* ➖ Decrease Cart Quantity
* 💳 Checkout
* 📋 Order Management
* 🚚 Order Tracking
* 📊 Admin Dashboard
* 📦 Stock Management
* 🖼️ Product Image Upload
* 🔒 Login Required for protected pages

## 🛠️ Technologies Used

* **Python**
* **Django**
* **SQLite3**
* **HTML5**
* **CSS3**
* **JavaScript**
* **Django Class-Based Views (CBV)**
* **Django Sessions**

## 📁 Project Structure

```text
RvStore/
│
├── ecomapp/
│   ├── migrations/
│   ├── templates/
│   ├── admin.py
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── context_processors.py
│
├── RvStore/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── media/
│   └── product_images/
│
├── db.sqlite3
├── manage.py
└── requirements.txt
```

## 🛒 Shopping Flow

```text
Register
   ↓
Login
   ↓
Browse Products
   ↓
View Product
   ↓
Add to Cart
   ↓
Manage Cart
   ↓
Proceed to Checkout
   ↓
Place Order
   ↓
Order Tracking
```

## 👨‍💻 Django Concepts Used

This project was developed to practice real-world Django development concepts, including:

* Class-Based Views
* `LoginRequiredMixin`
* Django Authentication
* Django Models & Relationships
* Django ORM
* Sessions
* Context Processors
* CRUD Operations
* Form Handling
* URL Routing
* Template Inheritance
* Static & Media Files
* Admin Customization

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY.git
```

### 2. Navigate to the project

```bash
cd RvStore
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

### 4. Activate the virtual environment

**Windows:**

```bash
venv\Scripts\activate
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

### 6. Run migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 7. Create a superuser

```bash
python manage.py createsuperuser
```

### 8. Run the development server

```bash
python manage.py runserver
```

Open:

```text
http://127.0.0.1:8000/
```

## 🔑 Admin Panel

The Django admin panel can be used to manage:

* Categories
* Products
* Stock
* Orders
* Order Items
* Order Tracking
* Users

Admin URL:

```text
http://127.0.0.1:8000/admin/
```

## 📌 Future Improvements

* Online Payment Gateway
* Product Search
* Product Filtering
* Product Reviews & Ratings
* Wishlist
* Email Order Confirmation
* User Profile
* Responsive Mobile UI
* REST API using Django REST Framework

## 🎯 Purpose

This project was created as a practical Django project to improve backend development skills and understand how an E-commerce application works from authentication to cart, checkout, order management, and tracking.

## 👨‍💻 Developer

**Rijo Varghese**

* Python / Django Developer
* MCA Student
* Interested in Backend & Web Development

---

⭐ If you find this project useful, consider giving it a star!
