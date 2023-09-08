
class Publication:

    def __init__(self, publication):
        self._id = (publication['_id'])
        self.titre = publication['title']
        self.type = publication['type']
        self.auteur = publication['authors']

    def to_json(self):
        return {"_id" : self._id, "titre" : self.titre, "auteur" : self.auteur, "type" : self.type}