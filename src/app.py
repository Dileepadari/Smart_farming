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

def get_user():
    connection = sqlite3.connect("Database.db")
    curser = connection.cursor()
    query = "SELECT * FROM users WHERE Userid=1 LIMIT 1"
    results = curser.execute(query)
    results = results.fetchall()
    connection.close()
    return results[0]

@app.route('/', methods=['GET', 'POST'])
@app.route('/home', methods=['GET', 'POST'])
def home():
    headers = {'X-M2M-Origin': 'admin:admin', "Content-Type": "application/json;ty=4"}
    link = "https://api.thingspeak.com/channels/2281910/feeds.json?results=2"
    response = requests.get(link, headers=headers)
    response = json.loads(response.text)
    notif_list = get_notifs()
    print(response)
    return render_template('index.html', data = response,user= get_user(), notifications = notif_list, file = "home.html", open1="open")

@app.route('/statistics', methods=['GET','POST'])
def statistics():
    notif_list = get_notifs()
    return render_template('index.html',notifications = notif_list,user= get_user(), file = "statistics.html", open2="open")
    
@app.route('/analysis', methods=['GET','POST'])
def analysis():
    headers = {'X-M2M-Origin': 'admin:admin', "Content-Type": "application/json;ty=4"}
    link = "https://api.thingspeak.com/channels/2281910/feeds.json?results=10"
    response = requests.get(link, headers=headers)
    response = json.loads(response.text)
    notif_list = get_notifs()
    connection = sqlite3.connect("Database.db")
    curser = connection.cursor()
    user= get_user()
    query = "SELECT * FROM plants WHERE plant_name='"+user[6]+"'"
    results = curser.execute(query)
    all_thres = results.fetchall()
    print(response)
    return render_template('index.html', data = response,user=user, notifications = notif_list,thresholds = all_thres, file = "analysis.html", open3="open")

@app.route('/circuit', methods=['GET','POST'])
def circuit():
    notif_list = get_notifs()
    return render_template('index.html', notifications = notif_list,user= get_user(), file = "circuit.html", open4="open")

@app.route('/history', methods=['GET','POST'])
def history():
    notif_list = get_notifs()
    return render_template('index.html', notifications = notif_list, user= get_user(), file = "history.html", open5="open")

@app.route('/alerts', methods=['GET','POST'])
def alerts():
    notif_list = get_notifs()
    connection = sqlite3.connect("Database.db")
    curser = connection.cursor()
    query = "SELECT * FROM notifications WHERE status=0"
    results = curser.execute(query)
    all_notifs = results.fetchall()
    return render_template('index.html', file = "alerts.html", notifications = notif_list, user= get_user(), notification = all_notifs, open6="open")
    
@app.route('/about', methods=['GET','POST'])
def about():
    notif_list = get_notifs()
    return render_template('index.html',notifications = notif_list, user= get_user(), file = "about.html", open7="open")

@app.route('/settings', methods=['GET','POST'])
def settings():
    if(request.method == 'POST'):
        connection = sqlite3.connect("Database.db")
        curser = connection.cursor()
        name_var = request.form['name']
        plant_var = request.form['plant']
        reading_var = request.form['reading']
        query = "UPDATE users SET Name = '"+name_var+"', plant = '"+plant_var+"', reading_no = '"+reading_var+"' WHERE Userid = 1"
        print(query)
        curser.execute(query)
        connection.commit()
        connection.close()
    notif_list = get_notifs()
    return render_template('index.html',notifications = notif_list, user= get_user(), file = "settings.html", open8="open")

@app.route('/change_seen/<noti_id>')
def change_seen(noti_id):
    connection = sqlite3.connect("Database.db")
    curser = connection.cursor()
    query = "UPDATE notifications SET status = 1 WHERE notification_id = "+noti_id
    curser.execute(query)
    connection.commit()
    connection.close()
    return redirect('/alerts')

@app.route('/receive', methods=['GET','POST'])
def receive_notif():
    if(request.method == 'POST'):
        connection = sqlite3.connect("Database.db")
        curser = connection.cursor()
        
        data = request.get_json()
        if(data['secret'] == "secretanicheppaga"):
            msg = data['msg']
            plant_name = data['plant_name']
            notif_type = data['notif_type']
            query = "SELECT * FROM notifications WHERE status=0"
            results = curser.execute(query)
            all_notifs = results.fetchall()
            for notis in all_notifs:
                if(notis[1] == plant_name and notis[2] == msg):
                    return jsonify({"status": "error", "message": "already sent"})
            
            date_format = "%d-%m-%Y %H:%M"
            date_var = datetime.now().strftime(date_format)
            query = "INSERT INTO notifications (plant_name,msg,notif_type, date_time) VALUES (?, ?,?, ?)"
            curser.execute(query, (plant_name, msg, notif_type, date_var))
            connection.commit()
            connection.close()
            return jsonify({"status": "success"})
        else:
            return jsonify({"status": "error", "message": "you don't have access to it"})
    else:
        return jsonify({"status": "error", "message": "you don't have access to it"})

@app.route('/query', methods=['GET', 'POST'])
def apply_query():
    if(request.method == 'POST'):
        connection = sqlite3.connect("Database.db")
        curser = connection.cursor()
    
        data = request.get_json()
        if(data['secret'] == "secretanicheppaga"):
            query = data['query']
            results = curser.execute(query)
            connection.commit()
            connection.close()
            return jsonify({"status": "success"})
        else:
            return jsonify({"status": "error", "message": "you don't have access to it"})
    else:
        return jsonify({"status": "error", "message": "you don't have access to it"})

if __name__ == '__main__':
    app.run(debug=True)
