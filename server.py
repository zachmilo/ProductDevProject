
from flask import Flask, jsonify
from flask_cors import CORS
from model.model import db
from model import constructor as query

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:!Apple45@localhost/test"
CORS(app)
db.init_app(app)

@app.route("/singlerisk")
def singleRiskType():
    res = query.getOneRisk()
    return jsonify(res.serialize())
    
@app.route("/allrisks")
def allRiskType():
    res = serializeResult(query.getAllRisks())
    return jsonify(res)

def serializeResult(query):
    return [i.serialize() for i in query]