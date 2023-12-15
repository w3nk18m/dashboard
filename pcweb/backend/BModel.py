from bunnet import Document
from datetime import datetime
from pydantic import Field






class BModel(Document):
    createdt: datetime = Field(default_factory=datetime.now)
    modifieddt: datetime = Field(default_factory=datetime.now)
