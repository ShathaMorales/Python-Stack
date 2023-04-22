from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'safe'


@app.route('/')
def index():
    counter = session.get('counter', 0)
    session['counter'] = counter + 1
    return render_template('index.html')


@app.route('/destroy_session')
def destroy_session():
    session.pop('counter', 0)
    return redirect('/')


@app.route('/incerement_session')
def increment_session():
    session['counter'] = session.get('counter') + 1
    return redirect('/')


@app.route('/reset')
def reset():
    session['counter'] = 0
    return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)
