from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/weather')
def weather():
    return render_template("main.html")

if __name__ == '__main__':
    app.run(debug=True)
