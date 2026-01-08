from pydantic import BaseModel

class CustomerCreate(BaseModel):
    id:int
    name:str
    email:str
    active:bool

class CustomerResponse(BaseModel):
    id:int
    name:str
    email:str
    active:bool
    
