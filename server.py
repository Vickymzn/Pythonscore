from flask import Flask, jsonify, request
import requests
import json
import sys
from bs4 import BeautifulSoup
from cricbuzz import Cricbuzz
from flask import Response
from json2html import *
app = Flask(__name__)

@app.route('/getMatches')
def getMatches():
    c = Cricbuzz()
    list =  c.matches()
    return json2html.convert(json=list)

@app.route('/livescore')
def getMatchInfo():
    matchId = request.args.get('matchId')
    c = Cricbuzz()
    list =  c.livescore(matchId)
    return json2html.convert(json=list)

@app.route('/scorecard')
def scorecard():
    matchId = request.args.get('matchId')
    c = Cricbuzz()
    list = c.scorecard(matchId)
    return json2html.convert(json=list)

@app.route('/commentary')
def commentary():
    matchId = request.args.get('matchId')
    c = Cricbuzz()
    list = c.commentary(matchId)
    return json2html.convert(json=list)

if __name__ == '__main__':
    app.run(
        host="0.0.0.0",
        port=int("1234")
    )


