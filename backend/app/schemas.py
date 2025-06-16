from pydantic import BaseModel

class DocumentCreate(BaseModel):
    content: str
    metadata: dict = None