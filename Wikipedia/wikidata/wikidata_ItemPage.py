import pywikibot as pwb

site = pwb.Site("en", "wikipedia")
page = pwb.Page(site, "A_Game_of_Thrones")
FullItem = pwb.ItemPage.fromPage(page)
QID = pwb.ItemPage.getID(page)

item_dict = FullItem.get()
print(item_dict)
