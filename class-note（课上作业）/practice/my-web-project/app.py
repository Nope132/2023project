#!/usr/bin/python
# coding: utf-8
from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("insert.html")

@app.route("/insert", methods=["POST"])
def insert():
    # extract data from request
    name = request.form['name']
    age = int(request.form['age'])
    # connect to a.db
    con = sqlite3.connect("a.db")
    # insert into students ...
    con.execute("insert into students values (?, ?)", (name, age))
    con.execute("commit")
    # redirect to display.html
    return redirect("/display")

@app.route("/display")
def display():
    # read from db
    con = sqlite3.connect("a.db")
    results = list(con.execute("select * from students"))
    # call render_template
    return render_template("display.html", results=results)