from pydantic import BaseModel, Field
from schemas.transaction import TransactionType
from enum import Enum

class CategoryType(str, Enum):
    shopping = "shopping"
    investing = "investing"
    food = "food"
    phone = "phone"
    entertainment = "entertainment"
    education = "education"
    beauty = "beauty"
    sports = "sports"
    social = "social"
    transportation = "transportation"
    fashion = "fashion"
    car = "car"
    alcohol = "alcohol"
    electronics = "electronics"
    travel = "travel"
    health = "health"
    pets = "pets"
    repairs = "repairs"
    housing = "housing"
    home = "home"
    gifts = "gifts"
    donation = "donation"
    lottery = "lottery"
    snacks = "snacks"
    kids = "kids"
    shady = "shady"
    add = "add"
    
    
    