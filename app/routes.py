import os
from app import app
from flask import render_template, request, redirect
import csv
import json
import pandas as pd
import sys, getopt, pprint
csvfile = open('/Users/2020jkapasi/Desktop/CompSci_IA/Book1.csv', "r")
reader = csv.DictReader(csvfile)

header = ["Category","Author","Title/Subtitle","Barcode","Circ Type","Description 1","Description 2","Description 3","ISBN","Subject"]

books = {"horror":"Goosebumps", "juvenile fiction":"Caillou", "love stories":"The Notebook", "prejudice":"things fall apart",
"domestic fiction":"Spongebob", "mystery":"Kung Fu Panda 3", "magic":"perry the platapus", "detective":"inspector gadget", "survival":"minecraft"




}




events = [
        {"event":"First Day of Classes", "date":"2019-08-21"},
        {"event":"Winter Break", "date":"2019-12-20"},
        {"event":"Finals Begin", "date":"2019-12-01"}]
from flask_pymongo import PyMongo

# name of database
app.config['MONGO_DBNAME'] = 'test'

# URI of database
app.config['MONGO_URI'] = 'mongodb+srv://admin:tsul0w85xQtsdZJa@cluster0-3rv5u.mongodb.net/test?retryWrites=true&w=majority'

mongo = PyMongo(app)


@app.route('/input')
def input():
    return render_template('input.html')



# INDEX

@app.route('/')
@app.route('/index')

def index():
    #connects the events to the mongo database
    collection = mongo.db.events
    #finding all of the events (stored as events)
    events = list(collection.find({}))
    print(events)
    return render_template('index.html', events = events)



# CONNECT TO DB, ADD DATA

@app.route('/add')
def add():
    #connect to database
    collection = mongo.db.book
    #iterating through each row of the CSV file
    for each in reader:
        #make new row
        row={}
        for field in header:
            print("the current field is " , field)
            row[field]=each[field]
        print(row)
        collection.insert(row) #inserting data to database
    return("added data to database")


@app.route('/results', methods = ["Get", "Post"]) #initiating the route
def results(): #defining the results page
    userdata = dict(request.form) #the user data is a dictionary of the form we created (inputs)
    print(userdata) # test to see in terminal
    # author_name = userdata['author_name']
    # print(author_name) #test to see in terminal
    # bar_code = userdata['bar_code']
    # print(bar_code) #test to see in terminal
    # title_ofbook_ofbook = userdata['title_ofbook']
    radiobutton = userdata["genre"]

    # for x in books:
    #     if x == radiobutton:
    #          print(books[radiobutton])
    #          return books[radiobutton]
    #1.) WEEKEND GOAL, QUERY DATABASE AND MAKE IT SO THAT IT GOES {"SUBJECT":RADIOBUTTON}
    #2.) RETURN THE LIST O FBOOKS FROM QUERY


    collection = mongo.db.events #connecting to the Mongo database (the events collection within the databse)

    #find the events in the collection, store them as a list of dictionaries, and assign to X.
    x = list(collection.find({})) #
    print(x)
    # collection.insert({"name": author_name, "date": bar_code, "time": title_ofbook})
    return redirect("/")

@app.route('/deleteall')
def deleteall():
    #connect to mongo
    collections = mongo.db.events
    collections.delete_many({})
    return "I deleted your database mwahahahahah"
