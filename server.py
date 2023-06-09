from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = "SECRET"

@app.route('/')
def index():
    return render_template('encuestas.html')

@app.route('/process', methods = ['POST'])
def process():
    session['name'] = request.form['name']
    session['location'] = request.form['location']
    session['lenguage'] = lenguage= request.form['lenguage']
    session['comment'] = comment = request.form['comment']
    return redirect('success' )

@app.route('/success')
def success():
    return render_template('success.html')

if __name__ == '__main__':
    app.run(debug=True)
