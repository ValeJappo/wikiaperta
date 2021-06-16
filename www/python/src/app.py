import json
from github_webhook import Webhook
import os
from flask import Flask
from flask import render_template
from flask_mwoauth import MWOAuth
from configparser import ConfigParser
import toolforge
from tinydb import TinyDB, Query
from flask import Markup

app = Flask(__name__)
webhook = Webhook(app)

# Get keys
config_object = ConfigParser()
config_object.read("keys.conf")
keys = config_object["KEYS"]

# Secret application key
app.secret_key = keys["app_secret"]

# OAuth
mwoauth = MWOAuth(base_url='https://it.wikipedia.org/w',clean_url='https://it.wikipedia.org/wiki',consumer_key=keys["consumer_key"],consumer_secret=keys["consumer_secret"])   
app.register_blueprint(mwoauth.bp)

# Get OAuth user
def getUser():
    if repr(mwoauth.get_current_user(True))!="None":
        return repr(mwoauth.get_current_user(True)).replace("'", "")
    else:
        return None


# Push github changes
@webhook.hook()
def on_push(data):
    os.system("cd $HOME && git pull origin main")

# Main
@app.route("/")
def index():
    return render_template('home.html', user=getUser())

# Test
@app.route("/test")
def test():
    return render_template('home.html', user="Testing-User")

# Debug
if __name__ == "__main__":
    app.run(debug=True, threaded=True)