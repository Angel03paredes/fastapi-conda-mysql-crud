from datetime import date, datetime
from pydantic import BaseModel
from typing import Optional

class post (BaseModel):
    id: Optional[str]
    user:str
    post:str
    created_at:Optional[datetime]
