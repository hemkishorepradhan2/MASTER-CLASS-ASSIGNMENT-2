from pydantic import BaseModel,EmailStr,Field

class CustomerCreate(BaseModel):
    id:int=Field(gt=0)
    name:str=Field(min_length=3,max_length=100)
    email:EmailStr
    active:bool=True

class CustomerResponse(BaseModel):
    id:int
    name:str
    email:EmailStr
    active:bool
    
