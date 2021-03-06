from Interfaces.ISuperVisor import ISuperVisor
from Database.DataBaseConnection import CreateConnection
from bson.objectid import ObjectId


class SuperVisor(ISuperVisor):

    def __init__(self, username=None):
        super(SuperVisor).__init__()
        if username is not None:
            self.username = username
            self.getSupervisor()

    def save(self):
        collection = CreateConnection()["users"]
        self.user_role = "supervisor"
        print(self.user_role)
        response = collection.insert_one({
            "full_name": self.full_name,
            "username": self.username,
            "password": self.password,
            "email": self.email,
            "user_role": self.user_role,
            "imagePath": self.imagePath+'/'
        })
        if response is not None:
            return True
        else:
            return False

    def getSupervisor(self):
        print(self.username)
        user = CreateConnection()["users"].find_one({
            "username": {"$eq": self.username}
        })
        print(user)
        print(user.get('user_role'))
        self.id = user.get('_id')
        self.full_name = user.get('full_name')
        self.user_role = user.get('user_role')
        self.phone = user.get('phone')
        self.email = user.get('email')
        self.vardiya = user.get('vardiya')

    @staticmethod
    def getAllSuperVisor():
        users = CreateConnection()["users"].find({
            "user_role": {"$eq": "supervisor"}
        })
        if users is not None:
            return list(users)
        else:
            return False

    @staticmethod
    def getSupervisor2(_id):
        user = CreateConnection()["users"].find_one({
            "_id": {"$eq": ObjectId(_id)}
        })
        return user

    def checkUsername(self):
        if self.username is not None:
            db = CreateConnection()["users"]
            res = db.find_one({
                "username": {"$eq": self.username}
            })
            if res is not None:
                return True
            else:
                return False

    def checkEmail(self):
        if self.email is not None:
            db = CreateConnection()["users"]
            res = db.find_one({
                "email": {"$eq": self.email}
            })
            if res is not None:
                return True
            else:
                return False

    def createWorker(self, data):
        # TODO : İşçi oluşturma işlemi Worker Classında yapılmaktadır.
        pass

    def createFolderForWorker(self, tcno):
        import os
        from pathlib import Path
        home = str(Path.home())
        folderPath = os.path.isfile(home + '/.faceAnalytics/program/supervisor/')
        if os.path.isfile(home + '/.faceAnalytics/program/supervisor'):
            workerPath = folderPath + tcno
            os.mkdir(workerPath)
            return workerPath
        else:
            print("Oluşmadı")
            return False

    @staticmethod
    def editSupervisorShift(id, vardiya):
        user = CreateConnection()["users"].find_one_and_update({
            "_id": {"$eq": id}
        },
            {
                "$set": {'vardiya': vardiya}
            })

        if user is not None:
            return True
        else:
            return False

    def editWorker(self, data):
        pass

    def deleteWorker(self, data):
        pass

    def addWorkerToShift(self, data):
        pass

    def removeWorkerFromShift(self):
        pass

    def viewReport(self):
        pass
