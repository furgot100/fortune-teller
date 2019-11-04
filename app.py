from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/fortune')
def fortune():
    return render_template('fortune_form.html')

@app.route('/fortune_results')
def fortune_results():
    user_