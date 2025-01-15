from flask import Flask, render_template, request, redirect, session
import csv

DELIMITER='|'
CSV_FILENAME='data/chats.csv'

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')



@app.route('/api/chat/<room>', methods=['GET'])
def get_full_chat_from_room(room):
    global CSV_FILENAME, DELIMITER
    lst=[]
    with open(CSV_FILENAME,'r',encoding='utf-8') as file:
        reader = csv.DictReader(file,delimiter=DELIMITER)
        for row in reader:
            if row['room'] == room:
                # "[2024-09-10 14:00:51] Roey: Hi everybody!"
                lst.append(f"[{row['date']} {row['time']}] {row['username']}: {row['message']}\n")
    return lst

 

@app.route('/<int:number>')
def handle_number(number):
    # in case an integer was given just show home
    return home()


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')