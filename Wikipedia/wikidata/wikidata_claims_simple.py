import pywikibot

site = pywikibot.Site("wikidata", "wikidata")
repo = site.data_repository()
# Q1751870 = Game of Thrones
item = pywikibot.ItemPage(repo, "Q1751870")

item_dict = item.get()
clm_dict = item_dict["claims"]
#clm_list = clm_dict["P2069"]

print(item_dict['descriptions']['en'])

for clmdictItem in clm_dict:
    print(clmdictItem)
    clm_list = clm_dict[clmdictItem]
    for clm in clm_list:
        
        if clm.id == 'P50':
            print('Author of Book')
        elif clm.id == 'P123':
            print('Publisher ')
        elif clm.id == 'P136':
            print('Genre ')
        elif clm.id == 'P166':
            print('Award Received ')
        elif clm.id == 'P179':
            print('Part of series ')
        elif clm.id == 'P407':
            print('Language of Work ')
        elif clm.id == 'P495':
            print('Country of Origin ')
        elif clm.id == 'P577':
            print('Publication Date ')
        elif clm.id == 'P856':
            print('Official Website ')
        elif clm.id == 'P1922':
            print('First Line ')

        clm_trgt = clm.getTarget()
        print(clm_trgt)
