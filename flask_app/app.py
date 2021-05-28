from flask import Flask
from flask import request, jsonify
from random import sample
from subprocess import Popen, PIPE, check_output
import shlex
import collections
import threading
import time
import subprocess

server = Flask(__name__)

def run_publish_request():
    functionName = request.json['function'] # eg catapi
    appId = request.json['app_id'] # eg 123
    resolvedFunctionName = appId + functionName # eg 123catapi
    stdout = subprocess.check_output(["./publish.sh", resolvedFunctionName])
    return stdout.decode('UTF-8').rstrip().replace("'", "\"")

def run_invoke_request():
    functionName = request.json['function'] # eg catapi
    stdout = subprocess.check_output(["./invoke.sh", functionName])
    return stdout.decode('UTF-8').rstrip().replace("'", "\"")

@server.route('/publish', methods=['GET', 'POST'])
def make_faas_publish_request():
    if request.method == 'GET':
        return 'This is the faas publish route. Send a POST request with json payload of the form { app_id: 123, function: catapi } in order to have your function published as 123catapi.'
    else:
        return run_publish_request()

@server.route('/invoke', methods=['GET', 'POST'])
def make_faas_invoke_request():
    if request.method == 'GET':
        return 'This is the faas invoke route. Send a POST request with json payload of the form { function: catapi }.'
    if request.method == 'POST':
        return run_invoke_request()
