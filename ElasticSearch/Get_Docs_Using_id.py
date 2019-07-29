from datetime import datetime
from elasticsearch import Elasticsearch

es = Elasticsearch([{'host': 'localhost', 'port': '9200'}])

for idnum in range(1,20):
    res = es.get(index="cust-merge", doc_type='cust', id=idnum)
    print(res['_source'])
