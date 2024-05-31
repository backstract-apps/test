from pydantic import BaseModel

class CreatePersonsSchema(BaseModel):
    id: int
    name: str


class ReadPersonsSchema(BaseModel):
    id: int
    name: str
    class Config:
        from_attributes = True


