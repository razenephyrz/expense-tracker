from pydantic import BaseModel
from datetime import datetime
class UserTransaction(BaseModel):
    id: int
    user_id : str
    category_id : int
    amount : float
    type : str
    date : datetime
    desc : str
    