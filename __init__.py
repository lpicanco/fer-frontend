from flask import Flask, render_template
from flask_bootstrap import Bootstrap

def create_app():
    app = Flask(__name__)
    Bootstrap(app)
    return app

app = create_app()

@app.route("/", methods=['GET'])
def hello():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)  