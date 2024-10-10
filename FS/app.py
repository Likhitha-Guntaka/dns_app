from flask import Flask, request, jsonify
import json

app = Flask(__name__)

fibonacci_cache = {}

def fibonacci(n):
    if n in fibonacci_cache:
        return fibonacci_cache[n]
    if n <= 1:
        return n
    else:
        fib = fibonacci(n-1) + fibonacci(n-2)
        fibonacci_cache[n] = fib
        return fib

@app.route('/register', methods=['PUT'])
def register():
    data = request.get_json()
    hostname = data.get('hostname')
    ip = data.get('ip')
    as_ip = data.get('as_ip')
    as_port = data.get('as_port')

    # Simulate UDP registration with AS (not implemented yet)
    return jsonify({'status': 'registered'}), 201

@app.route('/fibonacci', methods=['GET'])
def get_fibonacci():
    number = request.args.get('number')
    try:
        number = int(number)
    except ValueError:
        return 'Invalid number format', 400

    result = fibonacci(number)
    return jsonify(fibonacci_number=result), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9090)