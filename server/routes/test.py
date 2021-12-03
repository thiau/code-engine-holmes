import time
from flask_restful import Resource, Api
from flask import Flask, jsonify, request


class MainApi(Resource):
    def get(self):
        return {
            "response": "It works! (Updated on Dec 03 - 17:40 BRT)"
        }