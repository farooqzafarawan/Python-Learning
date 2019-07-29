#from datetime import datetime
from elasticsearch import Elasticsearch
import csv

es = Elasticsearch([{'host': 'localhost', 'port': '9200'}])

csvfile = r'C:\ElasticSearch\data.csv'

with open(csvfile) as csvf:  
    idnum = 1

    csv_reader = csv.DictReader(csvf, delimiter=',')
    line_count = 0
    for custrec in csv_reader:
        doc = {
            'CustomerKey': custrec['ID'],
            'DWCustomerNo':      custrec['custNo'],
            'CustomerFirstName': custrec['FName'],
            'CustomerLastName': custrec['LName'],
            'CustomerEmail':custrec['Email']
        }

        res = es.index(index="cust-all-1", id=idnum, body=doc)
        print(res['result'])
        idnum += 1

print('Finishing inserted documents in Index')
