# Django with Djongo (MongoDB Integration)

This is a Django application that uses **Djongo** to connect and interact with **MongoDB** as the database backend.

## 🚀 Features
- Django with MongoDB (using Djongo)
- Supports models, queries, and Django ORM-like operations
- Seamless integration with Django Admin (optional)
- Lightweight and easy to configure

## 🛠 Installation & Setup

### 1️⃣ **Clone the Repository**
```bash
git clone https://github.com/gishwinantony/DJONGO.git
cd DJONGO
```

### 2️⃣ **Create a Virtual Environment (Optional but Recommended)**
```bash
python -m venv venv
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate  # On Windows
```

### 3️⃣ **Install Dependencies**
```bash
pip install -r requirements.txt
```
Make sure `requirements.txt` includes:
```
django
djongo
dnspython  # Required for MongoDB connection
```

### 4️⃣ **Configure MongoDB Connection**
Update the `settings.py` file:
```python
DATABASES = {
    'default': {
        'ENGINE': 'djongo',
        'NAME': 'your_database_name',
        'CLIENT': {
            'host': 'mongodb+srv://your_username:your_password@your-cluster.mongodb.net/?retryWrites=true&w=majority',
        }
    }
}
```
> Replace `your_database_name`, `your_username`, and `your_password` accordingly.

### 5️⃣ **Apply Migrations**
```bash
python manage.py makemigrations
python manage.py migrate
```

### 6️⃣ **Run the Development Server**
```bash
python manage.py runserver
```
Access the app at **http://127.0.0.1:8000/**

## 📂 Project Structure
```
/your_project
│── /your_app
│── manage.py
│── requirements.txt
│── README.md
│── settings.py
│── ...
```

## 🛠 Available Commands
- `python manage.py runserver` → Start the Django server  
- `python manage.py makemigrations` → Create migrations  
- `python manage.py migrate` → Apply migrations  

## 📌 Notes
- Ensure MongoDB is **running** or use **MongoDB Atlas** for cloud hosting.
- Djongo **does not support all Django ORM features**, so use MongoDB-native queries when necessary.



