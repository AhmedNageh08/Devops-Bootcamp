from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_geek():
    return '<h1>Final Project For Devops Bootcamp</h2>'


if __name__ == "__main__":
    app.run(debug=True)