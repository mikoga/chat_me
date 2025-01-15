from flask import Flask, render_template, request, redirect, session, jsonify
import csv 
from datetime import datetime as dt

app = Flask(__name__)

DELIMITER='|'
CSV_FILE = "./data/chat.csv"


@app.route('/')
def home():
    return render_template('index.html'), 200


@app.route('/<int:number>')
def handle_number(number):
    # in case an integer was given just show home
    return home()


def get_full_chat_from_room(room):
    print(room)
    lst=[]
    with open(CSV_FILE,'r',encoding='utf-8') as file:
        reader = csv.DictReader(file,delimiter=DELIMITER)
        for row in reader:
            if row['room'] == str(room):
                # "[2024-09-10 14:00:51] Roey: Hi everybody!"
                lst.append(f"[{row['date']} {row['time']}] {row['username']}: {row['message']}")
    print(lst)
    return '\n'.join(lst)

 
@app.route('/api/chat/<int:room>', methods=['GET', 'POST'])
def chat(room):
    if request.method == 'GET':
        return get_full_chat_from_room(room)
    # extract the data
    username = request.form.get('username')
    message = request.form.get('msg')
    print(username)
    print(message)

    # validation + return status 400 if failed
    if not username or not message:
        return jsonify({"error": "Username and message are required"}), 400
    
    # handle time and date
    curr_date = dt.now().strftime('%Y-%m-%d')
    curr_time = dt.now().strftime('%H:%M:%S')

    # write to the CSV
    try:
        with open(CSV_FILE, 'a') as file:
            writer = csv.writer(file, delimiter = DELIMITER)
            writer.writerow([curr_date, curr_time, room, username, message])

    # handle error while writing to CSV + return status 500      
    except Exception as e:
        return jsonify({"error": f"Failed to save data: {str(e)}"}), 500
    
    # Return a success response
    return jsonify({"message": "Chat saved successfully"}), 201


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')