from flask import Flask, render_template, request, redirect, url_for, session
import os, random


app = Flask(__name__)

app.secret_key = os.urandom(24)
message = []

def randomid(n):
   randlst = [random.choice("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789") for i in range(n)]
   return ''.join(randlst)

id = randomid(10)

@app.route('/')
def top():
    global message
    
    new_message = session.pop('text', None)

    if new_message:
        message.append(new_message)
    

    return render_template('famCH.html', message=message, id=id)


@app.route("/famCH", methods=["POST"])
def famCH():

    session['text'] = request.form.get('text')
    
    return redirect(url_for('top'))




if __name__ == '__main__':
    app.run(debug=True)