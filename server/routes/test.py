import time
from flask_restful import Resource, Api
from flask import Flask, jsonify, request


class TestApi(Resource):
    def get(self):
        return {
            "response": "it works now! (Updated on Nov 29 - 17:16 BRT)"
        }