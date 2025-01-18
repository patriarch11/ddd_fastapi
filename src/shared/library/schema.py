from datetime import datetime

from pydantic import BaseModel


class AbstractEntitySchema(BaseModel):
    id: int
    created_at: datetime
    updated_at: datetime | None
