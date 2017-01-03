import os, subprocess, sqlite3, requests
from flask import Flask, request, session, g, abort, jsonify

app = Flask(__name__)
app.config.from_object(__name__)

app.config.update(dict(
    DATABASE=os.path.join(app.root_path, 'devices.db'),
    SECRET_KEY='q)T5CPEwT369^#qfC8@dr5/H93FlA7',
    USERNAME='serveradmin',
    PASSWORD='repton'
))
app.config.from_envvar('FLASKR_SETTINGS', silent=True)

def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

#connects to database
def connect_db():
    rv = sqlite3.connect(app.config['DATABASE'])
    rv.row_factory = dict_factory
    return rv

#connects to database IF NOT CONNECTED
def get_db():
    if not hasattr(g, 'sqlite_db'):
        g.sqlite_db = connect_db()
    return g.sqlite_db

#Closes database connection
@app.teardown_appcontext
def close_db(error):
    if hasattr(g, 'sqlite_db'):
        g.sqlite_db.close()

#Creates database (or wipes it) on startup
@app.before_first_request
def init_db():
    db = get_db()
    with app.open_resource('schema.sql', mode='r') as f:
        db.cursor().executescript(f.read())
    db.commit()

@app.route('/hub')
def show_devices():
    db = get_db()
    cur = db.execute('select location, inputs, outputs from devices')
    entries = cur.fetchall()
    return jsonify(entries)

@app.route('/addDevice', methods=['POST'])
def add_device():
    try:
	db = get_db()
	db.execute('insert into devices (location, inputs, outputs) values (?, ?, ?)', [request.form['location'], request.form['inputs'], request.form['outputs']])
	db.commit()
	return('Successfully added device.')
    except Exception, e:
	if 'UNIQUE constraint failed' in str(e):
	    db.execute('update devices set inputs=?, outputs=? where location=?', [request.form['inputs'], request.form['outputs'], request.form['location']])
	    db.commit()
	    return('Successfully updated device info')

@app.route('/inputs', methods=['POST'])
def change_input():
    r = requests.post("http://" + request.form['location'] + ":5000/inputs", data={'filename':request.form['filename'], 'input':request.form['input']})
    return('Successfully added data')

@app.route('/outputs', methods=['POST'])
def change_output():
    r = requests.post("http://" + request.form['location'] + ":5000/outputs", data={'filename':request.form['filename']})
    return(r.text)
