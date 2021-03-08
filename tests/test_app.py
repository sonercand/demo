import pytest
import flask
from flask import request, jsonify
from flask import Flask, Response as BaseResponse, json
from flask.testing import FlaskClient
from .. import app
print(app)
# flask app routes
def test_home():
    with app.test_request_context('/') :
        assert(flask.request.path == '/')
        assert(flask.request.status_code==200)
   
