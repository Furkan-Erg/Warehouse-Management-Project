# # library importation for sql db usage
import sqlite3
from sqlite3 import Cursor

import Products
from RawMaterials import RawMaterials

# # library importation for sql db usage

# sql connection function

db = sqlite3.connect('DataBase.db')

# sql connection function

# instance creation for usage of executer

dbCursor = db.cursor()


# instance creation for usage of executer

# sql query to create table

commend = 'CREATE TABLE deneme(id,name,dateOfPurchase ,nameOfSupplier ,storageExpDate ,storageCode,description)'
# commend = 'CREATE TABLE products(id,pName,pDateOfProduction ,pNameOfCustomer ,pStorageExpDate ,pStorageCode,pListOfMatCodes,pDescription)'

# sql query to create table

# query executer function

dbCursor.execute(commend)

# query executer function

def fetchMaterials():
    command = """SELECT * FROM raw_materials"""
    materialResponse: [RawMaterials] = dbCursor.execute(command)
    materialList = []
    for material in materialResponse:
        materialList.append(material)
    return materialList


def postProduct(product):
    dbCursor.execute("insert into products values (null,?,?,?,?,?,?,?)", (product))
    db.commit()


def getProducts():
    command = """SELECT * FROM products"""
    productResponse: [Products] = dbCursor.execute(command)
    productList = []
    for product in productResponse:
        productList.append(product)
    return productList


def getMaterials():
    command = """SELECT * FROM raw_materials"""
    materialResponse: [RawMaterials] = dbCursor.execute(command)
    materialList = []
    for material in materialResponse:
        materialList.append(material)
    return materialList


def getProductById(id):
    command = """SELECT * FROM products WHERE id =?"""
    productResponse = dbCursor.execute(command, (id,))
    return productResponse

def getMaterialById(id):
    command = """SELECT * FROM raw_materials WHERE id =?"""
    materialResponse = dbCursor.execute(command, (id,))
    return materialResponse
