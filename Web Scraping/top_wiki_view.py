import requests
from bs4 import BeautifulSoup



TOP_WIKI = "https://top.hatnote.com/ur/wikipedia/"
YEAR = "2020"
MON = "7"
DAY = "17"
DATE = YEAR + "/" + MON + "/" + DAY
EXT = ".html"
URL_WIKI = TOP_WIKI + DATE + EXT

page = requests.get(URL_WIKI)
soup = BeautifulSoup(page.content, 'html.parser')

colLabelDivs = soup.find_all("div", class_="column label")

title= [div.select(".title")[0].get_text().strip() for div in colLabelDivs]
views = [div.select(".views")[0].contents[0] for div in colLabelDivs]

titleViewTuple = dict(zip(title, views))


def format_row(title, views, row_template):

    table_row = {'title': title.replace("_", " "),
                 'views': views,
                 }

    row = row_template.format(**table_row)
    #     print(row)
    return(row)


RT_ROW = """|-
    |[[{title}|{title}]]
    |{views}
"""

# report_rows
report_rows = [format_row(x, y, RT_ROW)
               for x, y in zip(title, views,)
            ]

print(report_rows)

# for tup in titleViewTuple:
#     print(tup[1])

# for div in colLabelDivs:
#     # print(div)
#     title_class = div.find(class_="title")
#     #print(title_class)
#     title = div.select(".title")[0]

#     summary = div.select(".views")[0]
#     views = summary.contents[0]
#     #print(summary.get_text())
#     print(f"{title.get_text():<10} |  {views:>10} ")
