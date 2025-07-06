from flask import Flask, render_template, request, redirect, url_for, session
from datetime import datetime
import os, random


app = Flask(__name__)

app.secret_key = os.urandom(24)
message = []

def randomid(n):
   randlst = [random.choice("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789") for i in range(n)]
   return ''.join(randlst)
id = randomid(10)

current_time = datetime.now().isoformat(sep='-', timespec='seconds')



@app.route('/')
def top():
    global message
    
    new_message = session.pop('text', None)

    if new_message:
        message.append(new_message)
    

    return render_template('famCH.html', message=message, id=id, current_time=current_time)


@app.route("/famCH", methods=["POST"])
def famCH():

    session['text'] = request.form.get('text')
    
    return redirect(url_for('top'))




if __name__ == '__main__':
    app.run(debug=True)