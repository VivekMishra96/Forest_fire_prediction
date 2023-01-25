import pymongo
from loggerMain import FirePredictLogger

class MongoDbUtils:
    def __init__(self):
        """
        Constructor initializes monogdb url link
        """
        try:
            self.url = "mongodb+srv://mongodb:mongodb@cluster0.oxgpt.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
            self.client = pymongo.MongoClient(self.url)
            self.logger = FirePredictLogger.ineuron_scrap_logger()

        except Exception as e:
            self.logger.info(" Something went wrong on initiation process")

    def isDatabasePresent(self, db_name):
        '''Methods checks if Database already present or not'''
        try:
            print(self.client.list_database_names())
            if db_name in self.client.list_database_names():
                self.database = self.client[(db_name)]
                return True
            else:
                return False
        except Exception as e:
            self.logger.info("{db_name} already exists! Please chose different one" )


    def createDatabase(self, db_name):
        """
        This function checks whether the database is present or not.
        :param db_name:
        :return:
        """
        try:
            self.database = self.client[str(db_name)]
        except Exception as e:
            self.logger.error("[createDatabase]:Database Creation issue" + str(e))
        else:
            self.logger.info('Connection Established!' + str(self.client))

    def isCollectionPresent(self, collection_name):
        """
        This checks if collection is present or not.
        :param collection_name:
        :return:
        """
        try:
            database_status = self.database.name in self.client.list_database_names()
            self.logger.info(f"Database {self.database.name} present")
            if database_status:
                if collection_name in self.database.list_collection_names():
                    self.logger.info(f"Collection {collection_name} present")
                    return True
                else:
                    return False
            else:
                return False
        except Exception as e:
            self.logger.info(f"[isCollectionPresent]: Failed to check collection\n" + str(e))

    def getRecords(self, collection_name):
        """
        This fetches collection data from database.
        :param collection_name:
        :return:
        """
        try:
            collection = self.database[collection_name]
            data = collection.find()
            self.logger.info(f"Fetching records from collection")
            return data
        except Exception as e:
            self.logger.info("[getRecords]:Problem occured while fetching data" + str(e))
            print("[getRecords]:Problem occured while fetching data")