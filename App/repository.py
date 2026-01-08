from models import Customer

customers:list[Customer] = []

customers.append(Customer(id=1, name="Alice", email="alice@example.com", active=True))
customers.append(Customer(id=2, name="Bob", email="bob@example.com", active=False))
customers.append(Customer(id=3, name="Charlie", email="charlie@example.com", active=True))
customers.append(Customer(id=4, name="Diana", email="diana@example.com", active=True))
customers.append(Customer(id=5, name="Ethan", email="ethan@example.com", active=False))

def add_customer(customer:Customer):
    customers.append(customer)
    return customer
def get_all_customers():
    return customers

def get_customer_by_id(customer_id:int):
    for c in customers:
        if c.id==customer_id:
            return c
    return None

def delete_customer(customer_id: int) -> bool:
    """
    Deletes a customer by ID from the customers list.
    Returns True if a customer was deleted, False if not found.
    """
    for i, customer in enumerate(customers):
        if customer.id == customer_id:
            customers.pop(i)
            return True
    return False
