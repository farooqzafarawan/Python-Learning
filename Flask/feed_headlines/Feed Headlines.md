# Creating a new Flask application
To begin with, we'll create the skeleton of our new Flask application, which is pretty much the same as our Hello World application. Open headlines.py in your editor and write the following code:
```python
from flask import Flask
app = Flask(__name__)

@app.route("/")
def get_news():
  return "no news is good news"

if __name__ == '__main__':
  app.run(port=5000, debug=True)
```
