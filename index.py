from flask import Flask
from flask import render_template
from projectinspire import jsonVotes

app = Flask(__name__)

app.jinja_env.globals.update(jsonVotes=jsonVotes)
jsonList = jsonVotes()
@app.route('/')
def hello():
    return render_template('index.html', jsonList=jsonList)

if __name__ == '__main__':
    app.run(debug=True)
