from flask import Flask, request, render_template, redirect, session, url_for, jsonify
from datetime import datetime
import sqlite3
import requests
import json

app = Flask(__name__)
app.secret_key = 'DelhiisDelhi'
connection = sqlite3.connect("Database.db")
curser = connection.cursor()
connection.close()

def get_notifs():
    connection = sqlite3.connect("Database.db")
    curser = connection.cursor()
    query = "SELECT * FROM notifications WHERE status=0 LIMIT 4"
    results = curser.execute(query)
    all_notifs = results.fetchall()
    date_format = "%d-%m-%Y %H:%M"
    time_data = []
    for i in all_notifs:
        date_time = datetime.strptime(i[4], date_format)
        days_time = datetime.now()-date_time
        if days_time.days:
            first_non_zero = str(days_time.days) + " days"
        elif days_time.seconds // 3600:
            first_non_zero = str(days_time.seconds // 3600) + " hours"
        elif days_time.seconds // 60:
            first_non_zero = str(days_time.seconds // 60)  + " minutes"
        else:
            first_non_zero = str(days_time.seconds) + " seconds"
        time_data.append(first_non_zero)
    connection.close()
    all_notifs.append(time_data)
    print(all_notifs)
    return all_notifs

@app.route('/', methods=['GET', 'POST'])
@app.route('/home', methods=['GET', 'POST'])
def home():
    headers = {'X-M2M-Origin': 'admin:admin', "Content-Type": "application/json;ty=4"}
    link = "https://api.thingspeak.com/channels/2281910/feeds.json?results=2"
    response = requests.get(link, headers=headers)
    response = json.loads(response.text)
    notif_list = get_notifs()
    print(response)
    return render_template('index.html', data = response, notifications = notif_list, file = "home.html", open1="open")

@app.route('/statistics', methods=['GET','POST'])
def statistics():
    notif_list = get_notifs()
    return render_template('index.html',notifications = notif_list, file = "statistics.html", open2="open")
    
@app.route('/analysis', methods=['GET','POST'])
def analysis():
    headers = {'X-M2M-Origin': 'admin:admin', "Content-Type": "application/json;ty=4"}
    link = "https://api.thingspeak.com/channels/2281910/feeds.json?results=2"
    response = requests.get(link, headers=headers)
    response = json.loads(response.text)
    notif_list = get_notifs()
    print(response)
    return render_template('index.html', data = response, notifications = notif_list, file = "analysis.html", open3="open")

@app.route('/circuit', methods=['GET','POST'])
def circuit():
    notif_list = get_notifs()
    return render_template('index.html', notifications = notif_list, file = "circuit.html", open4="open")

@app.route('/history', methods=['GET','POST'])
def history():
    notif_list = get_notifs()
    return render_template('index.html', notifications = notif_list, file = "history.html", open5="open")

@app.route('/alerts', methods=['GET','POST'])
def alerts():
    notif_list = get_notifs()
    connection = sqlite3.connect("Database.db")
    curser = connection.cursor()
    query = "SELECT * FROM notifications WHERE status=0"
    results = curser.execute(query)
    all_notifs = results.fetchall()
    return render_template('index.html', file = "alerts.html", notifications = notif_list,notification = all_notifs, open6="open")
    
@app.route('/about', methods=['GET','POST'])
def about():
    notif_list = get_notifs()
    return render_template('index.html',notifications = notif_list, file = "about.html", open7="open")

@app.route('/settings', methods=['GET','POST'])
def settings():
    notif_list = get_notifs()
    return render_template('index.html',notifications = notif_list, file = "settings.html", open8="open")

@app.route('/change_seen')
def change_seen():
    connection = sqlite3.connect("Database.db")
    curser = connection.cursor()
    curser.execute("UPDATE notifications SET status = 1")
    connection.commit()
    connection.close()
    return redirect('/alerts')


if __name__ == '__main__':
    app.run(debug=True)
