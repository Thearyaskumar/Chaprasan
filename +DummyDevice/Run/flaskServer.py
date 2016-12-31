import os, subprocess
from flask import Flask, request, abort
app = Flask(__name__)

@app.route('/inputs', methods = ["POST"])
def myInputs():
    #Check if the file exists!
    if os.path.isfile("./inputs/" + request.form['filename']):
	return(subprocess.check_output('/usr/bin/python ./inputs/' + request.form['filename'] + ' ' + request.form['input'], shell=True))
    else:
	abort(404)

@app.route('/outputs', methods = ["POST"])
def myOutputs():
    if os.path.isfile("./outputs/" + request.form['filename']):
        return(subprocess.check_output('/usr/bin/python ./outputs/' + request.form['filename'], shell=True))
    else:
        abort(404)
