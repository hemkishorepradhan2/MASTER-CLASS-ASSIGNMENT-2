from models import Customer
from repository import add_customer, get_customer_by_id, get_all_customers, delete_customer
from errors import CustomerNotFoundError

def create_customer(id: int, name: str, email: str, active: bool) -> Customer:
    customer = Customer(id=id, name=name, email=email, active=active)
    return add_customer(customer)

def list_customers() -> list[Customer]:
    return get_all_customers()

def remove_customer(customer_id: int) -> bool:
    customer = get_customer_by_id(customer_id)
    if not customer:
        raise CustomerNotFoundError(f"Customer with ID {customer_id} not found.")
    delete_customer(customer_id)
    return True
