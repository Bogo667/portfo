from flask import Flask, render_template, url_for, request, redirect
import csv

app = Flask(__name__)

@app.route('/')
def my_home():
    return render_template('index.html')

@app.route('/<string:page_name>')
def kill(page_name):
    return render_template(page_name)

def write_file(data):
    with open('database.txt',mode='a') as database:
        email=data['email']
        subject=data['subject']
        message=data['message']
        file=database.write(f'\n{email},{subject},{message}')

def write_csv(data):
    with open('database.csv',mode='a',newline='') as database2:
        email=data['email']
        subject=data['subject']
        message=data['message']
        file2=csv.writer(database2,delimiter=' ',quotechar='|',quoting=csv.QUOTE_MINIMAL)
        file2.writerow([email,subject,message])


@app.route('/submit_form',methods=['POST','GET'])
def kill2():
    if request.method=='POST':
        try:
            data=request.form.to_dict()
            print(data)
            email=request.form.get('email')
            write_csv(data)
            print('Email',email)
            return redirect(url_for('thank_s', email=email))
        except:
            return 'Not appearing'
    else:
        return 'something went worng'

@app.route('/thank_s')
def thank_s():
    email=request.args.get('email')
    return render_template('thankyou.html',email=email)


