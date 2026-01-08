from models import Customer
from repository import add_customer, get_customer_by_id
from repository import get_all_customers
from repository import delete_customers
from errors import CustomerNotFoundError
def create_customer(id:int , name:str , email:str , active:bool):
    customer=Customer(id,name=name,email=email ,active=active)
    return add_customer(customer)
def list_customer():
    return get_all_customers()
 
def remove_customers(customer_id:int):
    customer=get_customer_by_id(customer_id)
    if not customer:
        raise CustomerNotFoundError("Customer is not found.")
    delete_customers(customer_id=customer_id)
    


