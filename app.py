from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculator/addition')
def addition():
    return render_template('addition.html')

@app.route('/calculator/subtraction')
def sub():
    return render_template('sub.html')

@app.route('/calculator/division')
def div():
    return render_template('div.html')

@app.route('/calculator/multiplication')
def mult():
    return render_template('mult.html')

@app.route('/calculator/exponents')
def exp():
    return render_template('exp.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
