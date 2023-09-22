from flask import Flask, request, jsonify
from calculator import calculator_bp

app = Flask(__name__)
app.register_blueprint(calculator_bp, url_prefix='/api')

@app.route('/', methods=['GET'])
def health():
    return "Server is Up and Running"

if __name__ == '__main__':
    app.run(debug=True)