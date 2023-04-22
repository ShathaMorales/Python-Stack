from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html', rows=8, cols=8)


@app.route('/<x>')
def refresh(x):
    return render_template('index.html', rows=int(x), cols=8)


@app.route('/<x>/<y>')
def checkerboard(x, y):
    rows = int(x)
    cols = int(y)
    return render_template('index.html', rows=rows, cols=cols)


if __name__ == '__main__':
    app.run(debug=True)
