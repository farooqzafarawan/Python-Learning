import feedparser
from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)
RSS_FEEDS = {'yahoo': 'https://www.yahoo.com/news/rss/world',
             'oreilly': 'http://feeds.feedburner.com/oreilly/radar/atom',
             'google': 'https://news.google.com/rss',
             'fox': 'http://feeds.foxnews.com/foxnews/latest'
            }


@app.route("/")
def get_news():
  query = request.args.get("publication")
  if not query or query.lower() not in RSS_FEEDS:
          publication = "fox"
  else:
          publication = query.lower()

  feed = feedparser.parse(RSS_FEEDS[publication])

  return render_template("home.html", articles=feed['entries'])

# if __name__ == "__main__":
#   app.run(port=5002, debug=True)
