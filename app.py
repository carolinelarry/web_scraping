from flask import Flask, render_template, redirect, jsonify
from flask_pymongo import PyMongo 
import scrape_mars

#Create an instance of Flask
app = Flask(__name__)

#Use PyMongo to establish mongo connection
mongo = PyMongo(app, uri="mongodb://localhost:27017/mars_app")

@app.route("/")
def home():
    mars_collection = mongo.db.mars_collection.find_one()
    return render_template("index.html", mars_collection=mars_collection)


@app.route("/scrape")
def scraper():
    mars_collection = mongo.db.mars_collection
    mars_data = scrape_mars.scrape_info()
    mars_collection.update({}, mars_data, upsert=True)
    return redirect("/", code=302)

if __name__ == "__main__":
  app.run(debug=True)
