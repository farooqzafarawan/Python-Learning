import feedparser
from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)
RSS_FEED = 'http://feeds.foxnews.com/foxnews/latest'

@app.route("/")
def get_news():
  feed = feedparser.parse(RSS_FEED)
  first_article = feed['entries'][2]

#   return """<html>
#     <body>
#         <h1> Headlines </h1>
#         <b>{0}</b> <br/>
#         <i>{1}</i> <br/>
#         <p>{2}</p> <br/>
#     </body>
# </html>""".format(first_article.get("title"), first_article.get("published"), first_article.get("summary"))

  return render_template("home_simple.html",title=first_article.get("title")
                                   ,published=first_article.get("published"),    summary=first_article.get("summary"))

if __name__ == "__main__":
  app.run(port=5000, debug=False)

