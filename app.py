from data import Data
from flask import Flask, render_template, request, url_for, redirect
from pymongo import MongoClient
from bson.objectid import ObjectId
import pprint

app = Flask(__name__)

@app.route('/')
def main_page() :
    return render_template("main_page.html",)

@app.route('/publications')
def liste_publis() :
    data = Data()
    publications = data.get_publications()
    publication_count = data.count_publications()
    authors = data.auteur_unique()
    
    titre = [publication.titre for publication in publications]

    return render_template ("list_publis.html",publications = publications, count = publication_count, authors = authors, titre = titre)

@app.route("/search")
def search_by_author():
    author = request.args.get('author')
    data = Data()
    publications = data.publications_auteur(author)

    return render_template("list_publis.html", publications=publications, count=len(publications), authors=data.auteur_unique())

@app.route('/date', methods=['GET'])
def date():
    date = request.args.get('date')
    data = Data()
    publications = data.get_publications_by_date(date)

    return render_template("list_publis.html", publications=publications, count=len(publications), search_date=date)

@app.route('/details')
def publication_details(publication_id) :
    data = Data()
    publication = data.get_publication_by_id(publication_id)

    return render_template("publication_details.html", publication=publication)


if __name__ == '__main__':
   app.run(host='0.0.0.0', port=5000)
#app.run(debug=True)

