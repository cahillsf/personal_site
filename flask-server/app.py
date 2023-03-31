from flask import Flask, jsonify, request, Response, make_response
from flask_cors import CORS
import logging
import pymongo
from pprint import pprint
import sys
import datetime
import os
import requests
import json
import werkzeug
## THIS IS THE TRACING BLOCK IN USE IN IMAGE FOR K8S#####
# import ddtrace.profiling.auto
from ddtrace import config, patch_all, Pin, patch, tracer
config.env = "dev"      # the environment the application is in
config.service = "flask-server"  # name of your application
config.version = "0.0.1"  # version of your application
patch(logging=True)
patch_all()
#################

# configuration

# DEBUG = True
# prof = Profiler(
#     env="dev",  # if not specified, falls back to environment variable DD_ENV
#     service="flask-server",  # if not specified, falls back to environment variable DD_SERVICE
#     version="0.0.1",   # if not specified, falls back to environment variable DD_VERSION
# )
# prof.start()

FORMAT = ('%(asctime)s %(levelname)s [%(name)s] [%(filename)s:%(lineno)d] '
          '[dd.service=%(dd.service)s dd.env=%(dd.env)s dd.version=%(dd.version)s dd.trace_id=%(dd.trace_id)s dd.span_id=%(dd.span_id)s] '
          '- %(message)s')
logging.basicConfig(format=FORMAT)

# instantiate the app
app = Flask(__name__)
deployment = os.environ.get('DEPLOYMENT')
config_string = 'config.' + deployment + 'Config'
my_obj_instance = werkzeug.utils.import_string(config_string)()
app.config.from_object(my_obj_instance)

db_uri = str(app.config['DATABASE_URI'])
print(app.config['DATABASE_URI'], file=sys.stderr)
client = pymongo.MongoClient(db_uri)

# enable CORS
# CORS(app, resources={r'/*': {'origins': '*'}})
CORS(app, origins=["http://localhost:8080"], headers=['Content-Type'], expose_headers=['Access-Control-Allow-Origin'], supports_credentials=True)


def deploy_to_mongo_host(argument):
    switcher = {
        "local": "localhost",
        "docker": "mongodb",
        "kubernetes": "ps-mongo-service",
    }
    return switcher.get(argument, "nothing")

def create_user_obj(input):
    clean_obj = {'email': str(input['email']), 'name': str(input['submitterName']), 'message':str(input['message'])}
    print(clean_obj, file=sys.stderr)
    app.logger.info(clean_obj)
    return clean_obj

def validate_response(resp): 
    app.logger.info("validating response" + str(resp))
    print(resp['success'], file=sys.stderr)
    success = True if resp['success'] == True else False
    print(success, file=sys.stderr)
    human = True if resp['score'] > 0.3 else False
    correct_action = True if resp['action'] == 'formSubmit' else False
    if (human and correct_action and resp['success']):
        return "valid"
    return "invalid"


@app.route('/api/cards', methods=['GET'])
# @app.route(base_url + '/cards', methods=['GET'])
def all_cards():
    app.logger.info("getting cards")
    db = client['sitecontent']
    cards = db.cards
    cards_cursor = cards.find({})
    print(cards_cursor, file=sys.stderr)
    cards_dict = {}
    for index, document in enumerate(cards_cursor):
        print(document, file=sys.stderr)
        cards_dict[index] = document
    return (cards_dict)

@app.route('/api/createMessage', methods=['POST'])
def createMessage():
    print(request.json, file=sys.stderr)
    db = client['sitecontent']
    clean_user_obj = create_user_obj(request.json)
    x = db.messages.insert_one(clean_user_obj)  
    print(x, file=sys.stderr)
    return "OKAY", 200

@app.route('/api/testRoute', methods=['GET'])
def testRoute():
    print(os.environ.get('DD_AGENT_HOST'), file=sys.stderr)
    app.logger.info(os.environ.get('DD_AGENT_HOST'))
    print("test route", file=sys.stderr)
    app.logger.info("test route")
    return "OKAY", 200

@app.route('/api/recaptcha', methods=['POST'])
def recaptcha():
    print(request.json, file=sys.stderr)
    recaptcha_secret= str(os.environ.get('RECAPTCHA_SECRET'))
    token = request.json['token']
    app.logger.info("validating with recaptcha")
    url = 'https://www.google.com/recaptcha/api/siteverify?secret='+ recaptcha_secret + '&response=' + token
    response = requests.post(url)
    response_dict = json.loads(response.text)
    response_assement = validate_response(response_dict)
    return response_assement, 200

#local deployment
if __name__ == '__main__':
    app.run(host="localhost", port=8000, debug=True)
    log = logging.getLogger(__name__)
    log.level = logging.DEBUG

#k8s deployment using gunicorn
if __name__ != '__main__':
    gunicorn_logger = logging.getLogger('gunicorn.error')
    app.logger.handlers = gunicorn_logger.handlers
    app.logger.setLevel(gunicorn_logger.level)
    base_url = "/api"
    mongo_client = "ps-mongo-service"