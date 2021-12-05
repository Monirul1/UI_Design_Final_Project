import os
import json
from sqlalchemy import *
from sqlalchemy.pool import NullPool
from flask import Flask, request, render_template, g, redirect, Response, url_for, flash
from flask_caching import Cache
import logging
from flask import request

app = Flask(__name__)

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
    return render_template('dashboard.html')

app.run(port=5000, debug=True)
