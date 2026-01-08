# 🚀 FastAPI Customer Management API

A simple FastAPI application to manage customers with basic CRUD operations.
This project demonstrates how to create, list, retrieve, and delete customers using RESTful APIs.

---

## 📌 Features

- Create a new customer  
- List all customers  
- Get customer by ID  
- Remove customer by ID  
- Interactive API docs using Swagger UI  

---

## 🛠 Tech Stack

- Python 3.9+  
- FastAPI  
- Starlette  
- Pydantic  

---

## 📂 Project Structure

    project-root/
    │── main.py
    │── services/
    │   ├── create_customer.py
    │   ├── list_customers.py
    │   ├── get_customer_by_id.py
    │   └── remove_customer.py
    │── schemas.py
    │── README.md
    │── images/
    │   ├── home.png
    │   ├── swagger_ui.png
    │   ├── create_customer.png
    │   ├── get_customers.png
    │   └── delete_customer.png

---

## ▶️ How to Run the Application

1. Create virtual environment

    python -m venv venv  
    source venv/bin/activate   (Linux / Mac)  
    venv\Scripts\activate      (Windows)  

2. Install dependencies

    pip install fastapi uvicorn  

3. Start the server

    uvicorn main:app --reload  

4. Open browser

- API Home: http://127.0.0.1:8000/  
- Swagger Docs: http://127.0.0.1:8000/docs  
- ReDoc: http://127.0.0.1:8000/redoc  

---

## 🔗 API Endpoints

### 🏠 Home

GET /

Response  
    "Welcome!"

---

### ➕ Create Customer

POST /create_customer

Request Body  
    {
      "id": 1,
      "name": "John Doe",
      "email": "john@example.com",
      "active": true
    }

Response  
    {
      "message": "Customer added successfully."
    }

---

### 📋 Get All Customers

GET /get_customers

Response  
    [
      {
        "id": 1,
        "name": "John Doe",
        "email": "john@example.com",
        "active": true
      }
    ]

---

### 🔍 Get Customer by ID

GET /customer/{customer_id}

Response  
    {
      "customer": {
        "id": 1,
        "name": "John Doe",
        "email": "john@example.com",
        "active": true
      }
    }

Error  
    {
      "detail": "Customer not found"
    }

---

### ❌ Remove Customer

DELETE /remove_customer/{customer_id}

Response  
    {
      "message": "Customer deleted successfully"
    }

---

## 📸 Screenshots

### Home Route
![Home](images/home.png)

### Swagger UI
![Swagger UI](outputs/Image1.png)

### Create Customer
![Create Customer](out/create_customer.png)

### Get Customers
![Get Customers](images/get_customers.png)

### Delete Customer
![Delete Customer](images/delete_customer.png)

---

## ✅ Status Codes Used

- 201 Created  
- 200 OK  
- 204 No Content  
- 404 Not Found  

---

## ✨ Author

Your Name  
FastAPI Developer 🚀

---

## 📄 License

This project is licensed under the MIT License.
