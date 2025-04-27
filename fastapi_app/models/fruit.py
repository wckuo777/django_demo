from pydantic import BaseModel

class FruitBase(BaseModel):
    name: str
    color: str

class FruitCreate(FruitBase):
    pass

class FruitRead(FruitBase):
    id: int

    class Config:
        orm_mode = True
