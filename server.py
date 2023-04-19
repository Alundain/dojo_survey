from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = "SECRET"

@app.route('/')
def index():
    if 'survey' not in session:
        session['survey'] = 0
    return render_template('encuestas.html', survey=session['survey'])

@app.route('/result', methods = ['POST'])
def result():
    firstname = request.form['firstname']
    location = request.form['location']
    lenguage= request.form['lenguage']
    comment = request.form['comment']
    return render_template('result.html', firstname=session['firstname'], location = session['location'], lenguage= session['lenguage'], comment = session['comment'])

if __name__ == '__main__':
    app.run(debug=True)