from pydantic import BaseModel
from bson import ObjectId

class DocumentModel(BaseModel):
    id: str
    content: str
    metadata: dict

    class Config:
        orm_mode = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
