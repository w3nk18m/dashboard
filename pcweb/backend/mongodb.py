from pymongo import MongoClient
from bunnet import init_bunnet, Document

from .SubjectModel import SubjectModel


def init():
    client = MongoClient("mongodb://localhost:27017")
    init_bunnet(database=client['data1'], document_models=[SubjectModel])
