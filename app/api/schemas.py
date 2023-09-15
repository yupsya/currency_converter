from datetime import datetime
from pydantic import BaseModel


class CurrencySchema(BaseModel):
    from_currency: str
    to_currency: str
    value: float
    converted_value: float
    datetime: datetime
