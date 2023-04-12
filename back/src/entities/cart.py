from pydantic import BaseModel
from typing import List


class Report(BaseModel):
    count: int
    price: float
    product_id: int


class Cart(BaseModel):
    reports: List[Report]
