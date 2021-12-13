from flask import Flask, request, render_template, redirect, url_for
from flask import request

app = Flask(__name__)

user_data = [
{
    "title":"SJHBFHSJBFJHSFS",
    "budget": 250,
    "remaining": 120
},
{
     "title":'Dining',
    "budget": 400,
    "remaining": 50
},
{
     "title":'Utility',
    "budget": 200,
    "remaining": 50
},
{
     "title":'Transportation',
    "budget": 150,
    'remaining': 80
}

]

dashboard_data_grocery = {
    'title':'Grocery',
    'budget': 300,
    'remaining': 120
}

dashboard_data_dining = {
    'title':'Dining',
    'budget': 400,
    'remaining': 50
}

dashboard_data_utility = {
    'title':'Utility',
    'budget': 200,
    'remaining': 50
}

dashboard_data_transportation = {
    'title':'Transportation',
    'budget': 150,
    'remaining': 80
}


@app.route('/')
def home():
    name = "Personal Budgeting"
    return render_template("home.html", name=name)

@app.route('/login', methods=['POST', 'GET'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'test' or request.form['password'] != 'test':
            error = 'Invalid Credentials. Please try again.'
        else:
            return redirect(url_for('home'))
    return render_template('login.html', error=error)

@app.route('/display_dashboard', methods=['GET'])
def display_dashboard():
    return render_template('dashboard.html', user_data=user_data, dashboard_data_grocery=dashboard_data_grocery, dashboard_data_dining=dashboard_data_dining, dashboard_data_utility=dashboard_data_utility)

@app.route('/manage_budget')
def manage_budget():
    return render_template("manage_budget.html")

@app.route('/transactions')
def transactions():
    return render_template("transactions.html")

@app.route('/account_details')
def account_details():
    return render_template("account_details.html")

@app.route('/account_insights')
def account_insights():
    return render_template("account_insights.html")

@app.route('/manual_expense')
def manual_expense():
    return render_template("manual_expense.html")

@app.route('/signup')
def signup():
    return render_template("signup.html")

if __name__ == '__main__':
    app.run(port=5000, debug=True)
