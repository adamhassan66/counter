from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe'


@app.route('/')
def index():
    if 'count' not in session:
        session['count'] = 0
        return render_template('index.html')


@app.route('/count')
def count():
    if 'count' in session:
        session['count'] += 1
        return redirect('/')


@app.route('/incriment_2')
def counter():
    if "count" in session:
        session['count'] += 2
        return redirect('/')


@app.route('/destroy_session')
def destroy_session():
        session.clear()
        return redirect('/')

if __name__ == "main":
    app.run(debug=True, port=5000)
