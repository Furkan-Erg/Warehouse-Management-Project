from abc import ABC, abstractmethod

from RawMaterials import RawMaterials


class Products( RawMaterials,ABC):

    def __init__(self, pName, pDateOfProduction, pNameOfCustomer, pStorageExpDate, pStorageCode, pListOfMatCodes,
                 pDescription):

        self.__pName = pName
        self.__pDateOfProduction = pDateOfProduction
        self.__pNameOfCustomer = pNameOfCustomer
        self.__pStorageExpDate = pStorageExpDate
        self.__pStorageCode = pStorageCode
        self.__pListOfMatCodes = pListOfMatCodes
        self.__pDescription = pDescription






    # getters for properties
    @abstractmethod
    def getPName(self):
        return self.pName

    @abstractmethod
    def getPDateOfProduction(self):
        return self.pDateOfProduction

    def getPNameOfCustomer(self):
        return self.pNameOfCustomer

    def getPStorageExpDate(self):
        return self.pStorageExpDate

    def getPStorageCode(self):
        return self.pStorageCode

    def getPListOfMatCodes(self):
        return self.pListOfMatCodes

    def getPDescription(self):
        return self.pDescription

    # getters for properties

    # setters for properties
    def setPName(self, pName):
        self.pName = pName

    def setPDateOfProduction(self, pDateOfProduction):
        self.pDateOfProduction = pDateOfProduction

    def setPNameOfCustomer(self, pNameOfCustomer):
        self.pNameOfCustomer = pNameOfCustomer

    def setPStorageExpDate(self, pStorageExpDate):
        self.pStorageExpDate = pStorageExpDate

    def setPStorageCode(self, pStorageCode):
        self.pStorageCode = pStorageCode

    def setPListOfMatCodes(self, pListOfMatCodes):
        self.pListOfMatCodes = pListOfMatCodes

    def setPDescription(self, pDescription):
        self.pDescription = pDescription
# setters for properties
