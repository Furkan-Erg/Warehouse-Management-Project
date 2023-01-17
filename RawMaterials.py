from abc import ABC


class RawMaterials(ABC):
    def __init__(self, name, dateOfPurchase, nameOfSupplier, storageExpDate, storageCode, description):
        self.name = name
        self.dateOfPurchase = dateOfPurchase
        self.nameOfSupplier = nameOfSupplier
        self.storageExpDate = storageExpDate
        self.storageCode = storageCode
        self.description = description


    # getters for properties
    def getName(self):
        return self.name

    def getDateOfPurchase(self):
        return self.dateOfPurchase

    def getNameOfSupplier(self):
        return self.nameOfSupplier

    def getStorageExpDate(self):
        return self.storageExpDate

    def getStorageCode(self):
        return self.storageCode

    def getDescription(self):
        return self.description

    # getters for properties

    # setters for properties
    def setName(self, name):
        self.name = name

    def setDateOfPurchase(self, dateOfPurchase):
        self.dateOfPurchase = dateOfPurchase

    def setNameOfSupplier(self, nameOfSupplier):
        self.nameOfSupplier = nameOfSupplier

    def setStorageExpDate(self, storageExpDate):
        self.storageExpDate = storageExpDate

    def setStorageCode(self, storageCode):
        self.storageCode = storageCode

    def setDescription(self, description):
        self.description = description

    # setters for properties
