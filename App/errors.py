class CustomerNotFoundError(Exception):
    def __init__(self, customer_id:int):
        self.customer_id=customer_id
        super().__init__(f"Customer with id {customer_id} not found.")
        
