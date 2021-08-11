from flask import Flask, request, abort, jsonify, render_template, url_for, redirect

import json
import requests

#get other .py files
# from getIP import * #from file getIP.py


app = Flask(__name__, template_folder='templates')

#run other .py files on this coding page
# app.register_blueprint(getIP) #ให้ file getIP.py เชื่อมกับไฟล์นี้ ในตอนที่ runserver ได้



@app.route('/')
def hello():
    return "Hello Flask-Heroku Github Python"
            
#@app.route('/')
#def main():
 #   return render_template('index.html')

@app.route("/about")
def about():
    return render_template('about.html')

@app.route('/api', methods=['GET'])
def get_api():
    return jsonify(data)


if __name__ == "__main__":
    app.run(debug = True)
