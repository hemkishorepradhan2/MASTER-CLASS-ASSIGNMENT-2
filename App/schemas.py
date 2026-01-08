from pydantic import BaseModel,EmailStr

class CustomerCreate(BaseModel):
    id:int
    name:str
    email:EmailStr
    active:bool

class CustomerResponse(BaseModel):
    id:int
    name:str
    email:EmailStr
    active:bool
    
