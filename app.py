from flask import Flask, jsonify, render_template
from main import main


app = Flask(__name__)
app.debug = True


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/generate/<category_id>', methods=["GET"])
def generate_meme(category_id: str):
    return jsonify(result_image=main(category_id))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
