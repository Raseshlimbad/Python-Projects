from pydantic import BaseModel

class Note(BaseModel):
    id: int
    title: str
    content: str

    class Config:
        from_attributes = True