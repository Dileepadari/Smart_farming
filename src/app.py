from flask import Flask, request, render_template, redirect, session, url_for, jsonify
import sqlite3
import requests
import json

app = Flask(__name__)
app.secret_key = 'DelhiisDelhi'

@app.route('/', methods=['GET', 'POST'])
@app.route('/home', methods=['GET', 'POST'])
def home():
    headers = {'X-M2M-Origin': 'admin:admin', "Content-Type": "application/json;ty=4"}
    link = "https://api.thingspeak.com/channels/2281910/feeds.json?results=2"
    response = requests.get(link, headers=headers)
    response = json.loads(response.text)
    print(response)
    return render_template('index.html', data = response, file = "home.html", open1="open")

@app.route('/statistics', methods=['GET','POST'])
def statistics():
    return render_template('index.html', file = "statistics.html", open2="open")
    
    
@app.route('/about', methods=['GET','POST'])
def about():
    return render_template('index.html', file = "about.html", open3="open")

# @app.route('/statitics', methods=['GET','POST'])
# def statistics():
#     return render_template('statistics.html')

# @app.route('/statitics', methods=['GET','POST'])
# def statistics():
#     return render_template('statistics.html')

# @app.route('/statitics', methods=['GET','POST'])
# def statistics():
#     return render_template('statistics.html')

# @app.route('/statitics', methods=['GET','POST'])
# def statistics():
#     return render_template('statistics.html')






if __name__ == '__main__':
    app.run(debug=True)
