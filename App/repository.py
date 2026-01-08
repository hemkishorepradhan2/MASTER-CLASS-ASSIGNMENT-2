from models import Customer

customers:list[Customer] = []

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

def delete_customers(customer_id:int):
    global customers
    customers=[c for c in customers if c.id!=customer_id]