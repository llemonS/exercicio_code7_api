from database import db

class Noticia(db.Document):
    titulo = db.StringField(required=True)
    texto = db.StringField(required=True)
    autor = db.ListField(db.StringField(), required=True)
    