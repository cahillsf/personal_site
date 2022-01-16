from flask import Flask, jsonify, request, Response, make_response
from flask_cors import CORS
import logging
import pymongo
from pprint import pprint
import sys
import datetime
import os
import ddtrace.profiling.auto
from ddtrace.profiling.profiler import Profiler
from ddtrace import config, patch_all, Pin, patch
config.env = "dev"      # the environment the application is in
config.service = "flask-server"  # name of your application
config.version = "0.0.1"  # version of your application
patch_all()

# configuration

# DEBUG = True
# prof = Profiler(
#     env="dev",  # if not specified, falls back to environment variable DD_ENV
#     service="flask-server",  # if not specified, falls back to environment variable DD_SERVICE
#     version="0.0.1",   # if not specified, falls back to environment variable DD_VERSION
# )
# prof.start()

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)
# enable CORS
# CORS(app, resources={r'/*': {'origins': '*'}})
CORS(app, origins=["http://localhost:8080"], headers=['Content-Type'], expose_headers=['Access-Control-Allow-Origin'], supports_credentials=True)

# this is the client connection in the k8s env
# connecting to ps-mongo-service (k8s-config/services/ps-mongo)
client = pymongo.MongoClient('mongodb://flask-role:toor@ps-mongo-service:27017/sitecontent?authSource=sitecontent')

# this is the client connection in the docker env
# connecting to mongodb (container name in docker compose)
# client = pymongo.MongoClient('mongodb://flask-role:toor@mongodb:27017/sitecontent?authSource=sitecontent')

def create_user_obj(input):
    clean_obj = {'email': str(input['email']), 'name': str(input['submitterName']), 'message':str(input['message'])}
    print(clean_obj, file=sys.stderr)
    app.logger.info(clean_obj)
    return clean_obj


@app.route('/api/cards', methods=['GET'])
def all_cards():
    db = client['sitecontent']
    cards = db.cards
    cards_cursor = cards.find({})
    print(cards_cursor, file=sys.stderr)
    cards_dict = {}
    for index, document in enumerate(cards_cursor):
        print(document, file=sys.stderr)
        cards_dict[index] = document
    # print(type(cards_dict), file=sys.stderr)
    return (cards_dict)

@app.route('/createMessage', methods=['POST'])
def createMessage():
    print(request.json, file=sys.stderr)
    db = client['sitecontent']
    clean_user_obj = create_user_obj(request.json)
    x = db.messages.insert_one(clean_user_obj)
    print(x, file=sys.stderr)
    return "OKAY", 200

@app.route('/testRoute', methods=['GET'])
def testRoute():
    print(os.environ.get('DD_AGENT_HOST'), file=sys.stderr)
    app.logger.info(os.environ.get('DD_AGENT_HOST'))
    print("test route", file=sys.stderr)
    app.logger.info("test route")
    return "OKAY", 200

if __name__ == '__main__':
    app.run(host="localhost", port=8000, debug=True)

if __name__ != '__main__':
    gunicorn_logger = logging.getLogger('gunicorn.error')
    app.logger.handlers = gunicorn_logger.handlers
    app.logger.setLevel(gunicorn_logger.level)