from pydantic import BaseModel

class EmployeeCreate(BaseModel):
    name: str
    email: str
    department: str
    designation: str
    experience: float
    skills: list[str]
    
class EmployeeResponse(BaseModel):
    id: int
    name: str
    email: str
    department: str
    designation: str
    experience: float
    skills: list[str]
    
    class Config:
        orm_mode = True

class UserCreate(BaseModel):
    username: str
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str
