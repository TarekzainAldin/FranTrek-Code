from flask import Flask

app = Flask(__name__)


@app.route('/')
@app.route('/home')
def home():
    return "welcom in the first page "
@app.route('/about_us')
def about():
    return ("this is the about page ")
if __name__ == '__main__':
    app.run(debug=True)
    