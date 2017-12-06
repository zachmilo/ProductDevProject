
from flask import Flask, jsonify
from model import constructor as query

app = Flask(__name__)

print(query.getOneRisk())

@app.route("/")
def initPage():
    ## this will return the generic risk
    return "Hello World!"

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