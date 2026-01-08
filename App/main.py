from fastapi import FastAPI, HTTPException
from services import create_customer as create_customer_service
from services import list_customers as list_customers_service
from services import remove_customer as remove_customer_service
from services import get_customer_by_id as get_customer_service
from schemas import CustomerCreate
from starlette import status

app = FastAPI()

@app.get("/")
async def home_route():
    return "Welcome!"

@app.post("/create_customer", status_code=status.HTTP_201_CREATED)
async def create_customer(customer: CustomerCreate):
    create_customer_service(
        id=customer.id,
        name=customer.name,
        email=customer.email,
        active=customer.active
    )
    return {"message": "Customer added successfully."}

@app.get("/get_customers", status_code=status.HTTP_200_OK)
async def get_customers():
    return list_customers_service()

@app.get("/customer/{customer_id}",status_code=status.HTTP_200_OK)
async def get_customer_by_id(customer_id: int):
    customer = get_customer_service(customer_id)
    if not customer:
        raise HTTPException(status_code=404, detail="Customer not found")
    return {"customer": customer}

@app.delete("/remove_customer/{customer_id}",status_code=status.HTTP_204_NO_CONTENT)
async def remove_customer(customer_id: int):
    try:
        remove_customer_service(customer_id)
    except Exception:
        raise HTTPException(status_code=404, detail="Customer not found")
    return {"message": "Customer deleted successfully"}
