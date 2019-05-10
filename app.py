from flask import Flask, render_template, request, redirect, flash
from flask_bootstrap import Bootstrap
from predictor import Predictor

predictor = Predictor()

def create_app():
    app = Flask(__name__)
    Bootstrap(app)

    app.config['SECRET_KEY'] = 'devkey'
    app.config['MAX_CONTENT_LENGTH'] = 50 * 1024 * 1024
    return app

app = create_app()

@app.route("/", methods=['GET'])
def index():
    return render_template('index.html')

@app.route("/", methods=['POST'])
def submit_image():
    file = request.files['file']

    if file.filename == '':
        flash('No selected file')
        return render_template('index.html')

    predictor.predict(file.read())

    return render_template('index.html')



if __name__ == '__main__':
    app.run(debug=True)  