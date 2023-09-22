from flask import Blueprint, request, jsonify

calculator_bp = Blueprint('calculator', __name__)

@calculator_bp.route('/calculator/<string:operation>', methods = ['POST'])
def calculator(operation):
    data = request.get_json()
    a = data['a']
    b = data['b']
    if operation == 'add':
        result = a + b
    elif operation == 'subtract':
        result = a - b
    elif operation == 'multiply':
        result = a * b
    elif operation == 'divide':
        result = a / b
    else:
        result = 'Invalid operation'
    return jsonify({ 'result': result })
