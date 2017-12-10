from flask import Flask, render_template
from addiction_controller.model import data

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('index.html', data=data)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
