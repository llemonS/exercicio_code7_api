from flask import Flask, request, Response, jsonify
from database import iniciar_db
from models import Noticia

app = Flask(__name__)

app.config['MONGODB_SETTINGS'] = { "host": "mongodb://127.0.0.1:27017/"}

iniciar_db(app)

@app.route('/noticias', methods=["GET","POST"])
def ver_adicionar():

    if request.method == "GET":
        #listar noticias existentes
        noticias = Noticia.objects().to_json()
        return Response(noticias, mimetype="application/json", status=200)

    elif request.method == "POST":
        #adicionar noticia
        body = request.get_json()
        noticia = Noticia(**body).save()
        sucesso = "Noticia adicionada com sucesso."
        return Response(sucesso, mimetype="application/json", status=200)

    else:
        return Response('Metodo Incorreto', mimetype="application/json", status=200)

@app.route('/noticia/<id_>', methods = ["GET","PUT","DELETE"])
def editar_apagar(id_):
    
    if request.method == "GET":
        noticia = Noticia.objects.get(id=id_).to_json()
        return Response(noticia, mimetype="application/json", status=200)

    elif request.method == "PUT":
        body = request.get_json()
        Noticia.objects.get(id=id_).update(**body)
        return Response('Editada', mimetype="application/json", status=200)

    elif request.method== "DELETE":
        Noticia.objects.get(id=id_).delete()
        return Response('Apagada', mimetype="application/json", status=200)

    else:
        return Response('Metodo Incorreto', mimetype="application/json", status=200)

app.run()
