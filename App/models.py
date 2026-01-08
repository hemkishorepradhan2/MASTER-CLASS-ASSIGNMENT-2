class Customer:
   
    def __init__(self,id,name,email,active):
        self.id=id
        self.name=name
        self.email=email
        self.active=active
    

    def __repr__(self):
        return f"Customer Id : {self.id} Customer Name : {self.name} Customer Email : {self.email}"