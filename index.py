from flask import Flask, render_template, request, redirect, url_for, session
import os

app = Flask(__name__)

app.secret_key = os.urandom(24)
message = ["匿名の投稿サイトです"]

@app.route("/famCH", methods=["POST"])
def famCH():

    session['text'] = request.form.get('text')
    
    return redirect(url_for('top'))

@app.route('/')
def top():
    global message
    if session.get('text') == "":
        print("空白")
    else:
        message.append(session.get('text'))
    return render_template('famCH.html', message=message)




if __name__ == '__main__':
    app.run(debug=True)