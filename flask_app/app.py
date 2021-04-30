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

def run_request():
    index = int(request.json['index'])
    list = ['red', 'green', 'blue', 'yellow', 'black']
    return list[index]

def read_output(process, append):
    for line in iter(process.stdout.readline, ""):
        append(line)

def run_faas_request():
    functionName = request.json['function'] # eg catapi
    stdout = subprocess.check_output(["./test.sh", functionName])
    return stdout.decode('UTF-8').rstrip().replace("'", "\"")

@server.route('/', methods=['GET', 'POST'])
def hello_world():
    if request.method == 'GET':
        return 'The model is up and running. Send a POST request'
    else:
        return run_request()

@server.route('/faas', methods=['GET', 'POST'])
def make_faas_request():
    if request.method == 'GET':
        return 'This is the faas route.  Send a POST request with json payload of the form { function: catapi }.'
    if request.method == 'POST':
        return run_faas_request()
