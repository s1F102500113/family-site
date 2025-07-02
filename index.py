from flask import Flask, render_template, request, redirect, url_for, session
import os

app = Flask(__name__)

app.secret_key = os.urandom(24)

@app.route('/')
def top():

    message = session.get('message')
    return render_template('famCH.html', message=message)

@app.route("/famCH", methods=["POST"])
def famCH():
  
    session['message'] = request.form.get('text')
    
    return redirect(url_for('top'))

if __name__ == '__main__':
    app.run(debug=True)