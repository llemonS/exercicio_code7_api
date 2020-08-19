from flask_mongoengine import MongoEngine

db = MongoEngine()

def iniciar_db(app):
    db.init_app(app)