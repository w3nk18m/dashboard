from pymongo import MongoClient
from bunnet import init_bunnet, Document

from .SubjectModel import Subject,AchievementSTDS, Unit
from .BModel import BModel


def init():
    models = BModel.__subclasses__()
    client = MongoClient("mongodb://localhost:27017")
    init_bunnet(database=client['data1'], document_models=models)
