#get Flask libraries
from flask import Flask
#creating flask instance
app = Flask(__name__)


@app.route('/')
def home ():
#test return browser text
    return "Hello, Concert Program App"
#is file being run and not imported
if __name__ == '__main__':
    app.run(debug=True)