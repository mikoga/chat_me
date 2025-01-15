from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/<int:number>')
def handle_number(number):
    # in case an integer was given just show home
    return home()

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
