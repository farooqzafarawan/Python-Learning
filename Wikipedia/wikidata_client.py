from wikidata.client import Client

client = Client()  # doctest: +SKIP

entity = client.get('Q20145', load=True)

data = entity.data

claims = data['claims']

for clm in claims:
    # print(clm)
    if clm in ('P106', 'P136'):
        qvalue = claims[clm][0]['mainsnak']['datavalue']['value']
        qid_entity = client.get(qvalue['id'], load=True)
        print(qid_entity.description)


# print(entity.description)
