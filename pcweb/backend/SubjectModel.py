from .BModel import BModel
from pydantic import Field, BaseModel

class UnitModel(BaseModel):
    label: str = Field(alias='단원명')
    achievementstds: list[str] = Field(alias='성취기준')

class SubjectModel(BModel):
    label: str = Field(alias='교과')
    unit: list[UnitModel] = Field(alias='단원')
