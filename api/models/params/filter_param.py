from typing import Literal 
from pydantic import BaseModel, Field
from datetime import datetime, timedelta

class FilterParams(BaseModel):
    toTms: int = Field(int(datetime.now().timestamp()), gt=0)
    fromTms: int = Field(gt=int((datetime.now()- timedelta(days=365)).timestamp()))
    range: Literal["20", "50", "200"]