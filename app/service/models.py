from pydantic import BaseModel
from typing import Optional

class User(BaseModel):
    first_name: str
    last_name: str
    address: Optional[str] = None
    country: Optional[str] = None
    age: Optional[int] = None

class UserResponse(User):
    id: int