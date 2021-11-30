from flask import Flask, jsonify, request
from flask_restful import Resource, Api
from server.routes.test import MainApi

app = Flask(__name__)
api = Api(app)

api.add_resource(MainApi, '/')

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=7000, debug=False)