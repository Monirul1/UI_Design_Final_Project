from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)

# @app.route('/')
# def home():
#     name = "Personal Budgeting"
#     return render_template("index.html", name=name)

@app.route('/')
def home():
    name = "Personal Budgeting"
    return render_template("home.html", name=name)

@app.route('/login', methods=['POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'test' or request.form['password'] != 'test':
            error = 'Invalid Credentials. Please try again.'
        else:
            return redirect(url_for('home'))
    return render_template('login.html', error=error)

app.run(port=5000, debug=True)
