from pydantic import BaseModel, Field, HttpUrl
from typing import Optional

class Qr(BaseModel):
    text : str = Field(..., max_length=1000, description="El texto a convertir a qr")
    box_size : int = Field(default=10, le=40)
    fill_color: str = Field(default="black")
    back_color: str = Field(default="white")
    logo_url: Optional[HttpUrl] = None
