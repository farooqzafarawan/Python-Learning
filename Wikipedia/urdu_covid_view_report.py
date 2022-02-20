from datetime import datetime, timedelta
import requests
import json
import pandas as pd
import pywikibot
import mwapi
from mwapi.errors import APIError

rt_header = """==   کورونا وائرس 2019 مضامین پیشرفت {year}-{month}-{day} ==
   تاریخ تجدید: ~~~~~
    {{| class="wikitable sortable"
    !شمار
    !مضمون
    !مشاہدات
"""

footer = """|}
    <!--IMPORTANT add all categories to the top section of the page, not here. Otherwise, they will get removed when the bot runs tomorrow! -->
"""

rt_row = """|-
    |{view rank}
    |[[{title}|{title}]]
    |{views}
    """


def get_template_mems(template):
    # If passed a `continuation` parameter, returns an iterable over a continued query.
    # On each iteration, a new request is made for the next portion of the results.
    continued = session.get(
        formatversion=2,
        action='query',
        generator='transcludedin',
        gtinamespace="0",
        gtiprop="title",
        gtishow="!redirect",
        titles=template,
        gtilimit=500,  # 100 results per request
        continuation=True)

    pages = []
    try:
        for portion in continued:
            if 'query' in portion:
                for page in portion['query']['pages']:
                    pages.append(page['title'])
            else:
                print("MediaWiki returned empty result batch.")
    except APIError as error:
        raise ValueError(
            "MediaWiki returned an error:", str(error)
        )

    return pages


def api_call(endpoint, parameters):  # I don't need this
    try:
        call = requests.get(endpoint, params=parameters)
        response = call.json()
    except:
        response = None
    return response


def get_yesterdates():
    """
    Returns month, day year for yesterday; month and day for day before
    """
    date_parts = {'year': datetime.strftime(datetime.now() - timedelta(1), '%Y'),
                  'month': datetime.strftime(datetime.now() - timedelta(1), '%m'),
                  'day': datetime.strftime(datetime.now() - timedelta(2), '%d'),
                  'month2': datetime.strftime(datetime.now() - timedelta(1), '%m'),
                  'day2': datetime.strftime(datetime.now() - timedelta(2), '%d'),
                  }

    return date_parts


def format_row(rank, title, views, row_template):

    table_row = {'view rank': rank,
                 'title': title.replace("_", " "),
                 'views': views,
                 }

    row = row_template.format(**table_row)
    #     print(row)
    return(row)


def get_latest_rev(page_title):
    # https://en.wikipedia.org/w/api.php?action=parse&prop=sections&format=json&formatversion=2&page=Whidbey_Island
    ENDPOINT = 'https://ur.wikipedia.org/w/api.php'

    params = {'action': 'query',
              'prop': 'revisions',
              'titles': page_title,
              'format': 'json',
              'formatversion': 2,
              }

    page_data = api_call(ENDPOINT, params)
    #     pprint(page_data)

    try:
        latest_rev = page_data['query']['pages'][0]['revisions'][0]['revid']
    except:
        print("unable to retrieve latest revision for " + page_title)
        latest_rev = None

    return latest_rev


def get_pageviews(article_params):
    from json.decoder import JSONDecodeError
    # sample https://wikimedia.org/api/rest_v1/metrics/pageviews/per-article/en.wikipedia.org/all-access/user/Zeng_Guang/daily/20200314/20200314
    q_template = "https://wikimedia.org/api/rest_v1/metrics/pageviews/per-article/ur.wikipedia.org/all-access/user/{title}/daily/{startdate}/{enddate}"
    q_string = q_template.format(**article_params)
    #print(q_string)
    try:
        response = requests.get(q_string)
        res_json = response.json()
        views = response['items'][0]['views']
    except JSONDecodeError as e:
        print(e)
        views = None
    except TypeError as e:
        print(f'Type Error: {e}')

    return views


session = mwapi.Session('https://ur.wikipedia.org/', user_agent="fztechno@gmail.com")  # add ua to config

# get yesterday's date info for queries and reporting
date_parts = get_yesterdates()

# get all corona articles using template
cat = 'سانچہ: کورونا وائرس کی وبا، 2019ء - 2020ء'
mems = get_template_mems(cat)
# print(mems)

# put these in a dataframe
df_pandemic = pd.DataFrame(mems)

# should do this when we create the df
df_pandemic.rename(columns={0: 'page title'}, inplace=True)

latest_revs = []
scores = []

# get recent pageviews
views = []

q_params = {'startdate': date_parts['year'] + date_parts['month'] + date_parts['day'],
            'enddate': date_parts['year'] + date_parts['month'] + date_parts['day'],
            'title': '',
            }  # do this outside the loop?

# page views list
for row in df_pandemic['page title']:
    latest = get_latest_rev(row)
    latest_revs.append(latest)
    # scores.append(get_quality_score(latest))

    # update the params with the current article title
    q_params['title'] = row
    v = get_pageviews(q_params)
    views.append(v)
    print(row, v)

# Add the scores and revs into the dataframe
lrs = pd.Series(latest_revs)
#ss = pd.Series(scores)

df_pandemic.insert(loc=1, column='latest revision', value=lrs)
#df_pandemic.insert(loc=2, column='quality prediction', value=ss)

# create views pandas series
vs = pd.Series(views)

# insert column views
df_pandemic.insert(loc=2, column='views', value=vs)

# sort views values in DF
df_pandemic.sort_values('views', ascending=False, inplace=True)

rank = range(1, len(df_pandemic) + 1)

df_pandemic['rank'] = list(rank)

print(df_pandemic['views'])

df_pandemic['views'].fillna(0, inplace=True)

# After fillna on views column
print(df_pandemic['views'])

# report_rows
report_rows = [format_row(x, y, z, rt_row)
               for x, y, z in zip(df_pandemic['rank'],
                                  df_pandemic['page title'],
                                  df_pandemic['views'],
                                  )]

rows_wiki = ''.join(report_rows)

header = rt_header.format(**date_parts)

output = header + rows_wiki + footer


def publish_report(output):
    """
    Accepts page text,  edit summary and Publishes the formatted page text to the specified wiki page
    """

    title_page = 'ویکیپیڈیا:ویکی منصوبہ برائے کووڈ-19/مضامین کی شماریات'

    site = pywikibot.Site('ur', 'wikipedia')
    urpage = pywikibot.Page(site, title_page)

    urtext = urpage.text

    urpage.text = output + '\n' + urtext

    # save the page
    urpage.save(summary='خودکار: کورونا وائرس صفحات شماریات', minor=False)


publish_report(output)
