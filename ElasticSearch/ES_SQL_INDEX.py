from elasticsearch import Elasticsearch
import pyodbc
import datetime

cnxn = pyodbc.connect("Driver={SQL Server Native Client 11.0};
                       Server=localhost;
                       UID=python;PWD=python;
                       Database=AdventureWorks;")

cursor = cnxn.cursor()
cursor.execute('SELECT top(100) from Person.Person')

es = Elasticsearch([{'host': 'localhost', 'port': '9200'}])
startTime = datetime.datetime.now()

print(f"Loading started: {startTime}")
idnum=1
for custrec in cursor:
         doc = {
            'BusinessEntityID':custrec[0],
            'PersonType': custrec[1],
            'FirstName':custrec[2],
            'LastName': custrec[3],
            'Suffix': custrec[4],
            'EmailPromotion': custrec[5],
            'ModifiedDate': custrec[6]
         }
         
         #print(doc)

         res = es.index(index="person-data", id=idnum, body=doc)
         #print(res['result'],idnum)
         print(f'Created :{idnum}')
         idnum = idnum + 1

endTime     = datetime.datetime.now()
elapsedTime = endTime - startTime

print(f"Loading started: {endTime}")
print(elapsedTime)
