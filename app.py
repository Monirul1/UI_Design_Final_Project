from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    name = "Personal Budgeting"
    return render_template("index.html", name=name)


app.run(port=5000)