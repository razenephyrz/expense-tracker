from pydantic import BaseModel, Field

class Category(BaseModel):
    id : int
    name : str = Field(..., min_length=3)
    type : str = Field(..., min_length=3)
    
    