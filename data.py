from connection import Connection
from publis import Publication
from bson.objectid import ObjectId

class Data :

    def get_publications(self):
        client = Connection.connexion()
        publications = client.publis.find()
        publications = [Publication(publication) for publication in publications]
        Connection.deconnexion()
        return publications
    
    def count_publications(self):
        client = Connection.connexion()
        count = client.publis.count_documents({})
        Connection.deconnexion()
        return count

    def auteur_unique(self):
        client = Connection.connexion()
        auteur = client.publis.distinct("authors")
        Connection.deconnexion()
        return auteur
    
    def publications_auteur(self,author) :
        client = Connection.connexion()
        tous  = client.publis.find({"authors":author})
        publications = []

        for publication in tous :
            publications.append(Publication(publication))
        
        Connection.deconnexion()
        return publications
    
    def get_publications_by_date(self,date) :
        client = Connection.connexion()
        publications = client.publis.find({'year': {'$gte': int(date)}}).sort([('year'),('title')])
        publis = [Publication(pub) for pub in publications]
        Connection.deconnexion()
        return publis
    
    def get_publication_by_id(self, publication_id):
        client = Connection.connexion()
        publication = client.publis.find_one({'_id': ObjectId(publication_id)})
        return Publication(publication)