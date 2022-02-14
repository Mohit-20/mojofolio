import csv
from flask import Flask, render_template, request, redirect


app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')


def save_data(data):
    database = open('data.csv', newline='', mode = 'at')
    name = data['name']
    email = data['email']
    subject = data['subject']
    message = data['message']
    save = csv.writer(database, delimiter = ',', quotechar='"', quoting = csv.QUOTE_MINIMAL)
    save.writerow([name,email,subject,message])
    

 
@app.route('/submit', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            save_data(data)
            return thankyou()
        except:
            return 'Database Error'
    else:
        return 'Someting Went Wrong'


@app.route('/thankyou')
def thankyou():
    return render_template('thankyou.html')

app.run(debug = True)
