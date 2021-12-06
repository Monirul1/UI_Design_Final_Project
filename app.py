import os
import json
from sqlalchemy import *
from sqlalchemy.pool import NullPool
from flask import Flask, request, render_template, g, redirect, Response, url_for, flash
from flask_caching import Cache
import logging
from flask import request

app = Flask(__name__)

dashboard_data_grocery = {
    'Title':'Grocery',
    'Budget': 250,
    'Remaining': 120
}

dashboard_data_dining = {
    'Title':'Dining',
    'Budget': 400,
    'Remaining': 50
}

dashboard_data_utility = {
    'Title':'Utility',
    'Budget': 200,
    'Remaining': 50
}

ashboard_data_transportation = {
    'Title':'Transportation',
    'Budget': 150,
    'Remaining': 80
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
    return render_template('dashboard.html', dashboard_data_grocery=dashboard_data_grocery, dashboard_data_dining=dashboard_data_dining, dashboard_data_utility=dashboard_data_utility)

@app.route('/manage_budget')
def manage_budget():
    return render_template("manage_budget.html")

@app.route('/transactions')
def transactions():
    return render_template("transactions.html")

@app.route('/account_details')
def account_details():
    return render_template("account_details.html")

@app.route('/manual_expense')
def manual_expense():
    return render_template("manual_expense.html")

    return render_template('dashboard.html')

app.run(port=5000, debug=True)
