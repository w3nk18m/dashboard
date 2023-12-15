from .BModel import BModel
from pydantic import Field, BaseModel
from bunnet import Link, BackLink

class Subject(BModel):
    label: str = Field(alias='교과')
    year: str = Field(alias='학년도', default='2023년')
    semester: str = Field(alias='학기', default='1학기')
    grade: str = Field(alias='학년', default='1학년')
    units: list[Link["Unit"]] = Field(alias='단원')

class Unit(BModel):
    label: str = Field(alias='단원명')
    achievementstds: list[Link["AchievementSTDS"]] = Field(alias='성취기준')
    subject: BackLink[Subject] = Field(original_field="units")

class AchievementSTDS(BModel):
    label: str = Field(alias='성취기준')
    unit: BackLink[Unit] = Field(original_field="achievementstds")