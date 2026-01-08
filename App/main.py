from fastapi import FastAPI
from repository import add_customer, delete_customer,get_all_customers
from repository import get_customer_by_id as gci
from schemas import CustomerCreate,CustomerResponse
app=FastAPI()





@app.get("/")
async def home_route():
    return f"Welcome!"

@app.post("/create_customer")
async def create_customer(customer:CustomerCreate):
    add_customer(customer)
    return {"message":"Customer added successfully."}

@app.get("/get_customers")
async def get_customers():
    customers=get_all_customers()
    return customers

@app.get("/customer/{customer_id}")
async def get_customer_by_id(customer_id: int):
    customer = gci(customer_id)
    return {"customer": customer}

@app.delete("/remove_customer/{customer_id}")
async def remove_customer(customer_id:int):
    delete_customer(customer_id)
    return {"message":"Deleted Successfully"}


