- [Creating Headline Project](#Creating-Headlines-Project)
  * [Create Flask Application](#Creating-Flask-Application)
     + [Flask Installation](#Flask-Installation)
     + [Create HeadLines Flask Application](#Create-HeadLines-App)
  * [Using RSS from Python](#Using-RSS-From-Python)    
     + [Feedparser Installation](#Feedparser-Installation)
     + [Parsing First Article in HTML](#Parsing-First-Article-in-HTML)
  * [URL routing in Flask](#URL-Routing-in-Flask)
     + [RSS FEED URL](#RSS-FEED-URLS)
     + [Static Routing Implementation](#Static-Routing-Implementation)
    
# Creating Headlines Project
## Creating Flask Application
### Flask Installation
on command prompt, use following command to install flask

```python
pip install flask
```

### Create HeadLines App
To begin with, we'll create the skeleton of our new Flask application, which is pretty much the same as our Hello World application. Open `headlines.py` in your editor and write the following code:
```python
from flask import Flask
app = Flask(__name__)

@app.route("/")
def get_news():
  return "no news is good news"

if __name__ == '__main__':
  app.run(port=5000, debug=True)
```


## Using RSS from Python
### Feedparser Installation
install feedparser using following command
```python
pip install feedparser
```

### Parsing First Article in HTML
In our headlines.py file, we'll make modifications to import the feedparser library, parse the feed, and grab the first article. We'll build up HTML formatting around the first article and show this in our application.
Our new code adds the import for the new library, defines a new global variable for the RSS feed URL, and further adds a few lines of logic to parse the feed, grab the data we're interested in, and insert this into some very basic HTML.

```python
import feedparser
from flask import Flask
app = Flask(__name__)
BBC_FEED = "http://feeds.bbci.co.uk/news/rss.xml"
@app.route("/")
def get_news():
  feed = feedparser.parse(BBC_FEED)
  first_article = feed['entries'][0]
  return """<html>
    <body>
        <h1> BBC Headlines </h1>
        <b>{0}</b> <br/>
        <i>{1}</i> <br/>
        <p>{2}</p> <br/>
    </body>
</html>""".format(first_article.get("title"), first_article.get("published"), first_article.get("summary"))

if __name__ == "__main__":
  app.run(port=5000, debug=True)

```

## URL Routing in Flask
Python decorators are represented by `@app.route("/")` line we had above our main function, and they indicate to Flask which parts of our application should be triggered by which URLs. Our base URL, which is usually something similar to site.com but in our case is the IP address of our VPS, is omitted, and we will specify the rest of the URL (that is, the path) in the decorator. Earlier, we used a single slash, indicating that the function should be triggered whenever our base URL was visited with no path specified. Now, we will set up our application so that users can visit URLs such as site.com/bbc or site.com/cnn to choose which publication they want to see an article from.

### RSS FEED URLS
The first thing we need to do is collect a few RSS URLs. At the time of writing, all of the following are valid:
- yahoo: 'https://www.yahoo.com/news/rss/world',
- oreilly: 'http://feeds.feedburner.com/oreilly/radar/atom',
- google: 'https://news.google.com/rss',
- fox: 'http://feeds.foxnews.com/foxnews/latest'

### Static Routing Implementation
First, we will consider how we might achieve our goals using static routing. It's by no means the best solution, so we'll implement static routing for only two of our publications. Once we get this working, we'll consider how to use dynamic routing instead, which is a simpler and more generic solution to many problems.
Instead of declaring a global variable for each of our RSS feeds, we'll build a Python dictionary that encapsulates them all. We'll make our get_news() method generic and have our decorated methods call this with the relevant publication. Our modified code looks as follows:

```python
import feedparser
from flask import Flask
app = Flask(__name__)
RSS_FEEDS = {'bbc': 'http://feeds.bbci.co.uk/news/rss.xml',
             'cnn': 'http://rss.cnn.com/rss/edition.rss',
             'fox': 'http://feeds.foxnews.com/foxnews/latest',
             'iol': 'http://www.iol.co.za/cmlink/1.640'}

@app.route("/")
@app.route("/fox")
def fox():
    return get_news('fox')

@app.route("/cnn")
def cnn():
    return get_news('cnn')

def get_news(publication):
  feed = feedparser.parse(RSS_FEEDS[publication])
  first_article = feed['entries'][0]
  return """<html>
    <body>
        <h1>Headlines </h1>
        <b>{0}</b> </ br>
        <i>{1}</i> </ br>
        <p>{2}</p> </ br>
    </body>
</html>""".format(first_article.get("title"), first_article.get("published"), first_article.get("summary"))

if __name__ == "__main__":
  app.run(port=5000, debug=False)

```
