from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/fortune', methods=['GET', 'POST'])
def fortune():
    return render_template('fortune_form.html')

@app.route('/fortune_results')
def fortune_results():
    name = request.args.get('name')
    food = request.args.get('food')
    petlist = request.args.get('petlist')
    age = request.args.get('age')

    fortune = {
        'name' : name,
        'food' : food,
        'petlist' : petlist,
        'age' : age
    }

    return render_template('results.html', fortune=fortune)
if __name__ == "__main__":
    app.run()