from pymongo import MongoClient

class Connection : 
    __USER = "root"
    __PW = "example"
    __DB_NAME = "dblp"


    @classmethod
    def connexion(cls) :
        cls.client = MongoClient(f"mongodb://{cls.__USER}:{cls.__PW}@mongo-db")

        cls.db = cls.client[cls.__DB_NAME]

        return cls.db

    @classmethod
    def deconnexion(cls) :
        cls.client.close()