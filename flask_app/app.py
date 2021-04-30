def run_request():
    index = int(request.json['index'])
    list = ['red', 'green', 'blue', 'yellow', 'black']
    return list[index]

def run_faas_request():
    function = request.json['function']
    # ref xspdf.com/resolution/50942456.html
    # cmd = "/bin/sh -c export OPENFAAS_URL=https://faasd.cthulu.tk && echo | faas-cli invoke catapi"
    cmd2 = "export OPENFAAS_URL=https://faasd.cthulu.tk && echo | faas-cli invoke catapi"
    args = shlex.split(cmd2)
    #proc = Popen(args, stdout=PIPE, stderr=PIPE)
    proc = Popen(args, shell=True, stdout=PIPE, stderr=PIPE)
    out, err = proc.communicate()
    exitcode = proc.returncode
    return out

def run_faas_request2():
    cmd = "export OPENFAAS_URL=https://faasd.cthulu.tk && echo | faas-cli invoke catapi"
    args = shlex.split(cmd)
    success = False
    while success = False:
        try:
            output = subprocess.check_output(args, stderr=subprocess.STDOUT).decode()
            success = True
        except subprocess.CalledProcessError as e:
            output = e.output.decode()
            success = False
    return out.decode()

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

@server.route('/faas2', methods=['GET', 'POST'])
def make_faas_request2():
    if request.method == 'GET':
        return 'This is the faas route.  Send a POST request with json payload of the form { function: catapi }.'
    if request.method == 'POST':
        return run_faas_request2()
"flask_app/app.py" 58L, 2069C                                                                       54,22         Bot

def run_request():
    index = int(request.json['index'])
    list = ['red', 'green', 'blue', 'yellow', 'black']
    return list[index]

def run_faas_request():
    function = request.json['function']
    # ref xspdf.com/resolution/50942456.html
    # cmd = "/bin/sh -c export OPENFAAS_URL=https://faasd.cthulu.tk && echo | faas-cli invoke catapi"
    cmd2 = "export OPENFAAS_URL=https://faasd.cthulu.tk && echo | faas-cli invoke catapi"
    args = shlex.split(cmd2)
    #proc = Popen(args, stdout=PIPE, stderr=PIPE)
    proc = Popen(args, shell=True, stdout=PIPE, stderr=PIPE)
    out, err = proc.communicate()
    exitcode = proc.returncode
    return out

def run_faas_request2():
    cmd = "export OPENFAAS_URL=https://faasd.cthulu.tk && echo | faas-cli invoke catapi"
    args = shlex.split(cmd)
    success = False
    while success = False:
        try:
            output = subprocess.check_output(args, stderr=subprocess.STDOUT).decode()
            success = True
        except subprocess.CalledProcessError as e:
            output = e.output.decode()
            success = False
    return out.decode()

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

@server.route('/faas2', methods=['GET', 'POST'])
def make_faas_request2():
    if request.method == 'GET':
        return 'This is the faas route.  Send a POST request with json payload of the form { function: catapi }.'
    if request.method == 'POST':
        return run_faas_request2()
