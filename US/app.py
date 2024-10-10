from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/fibonacci', methods=['GET'])
def get_fibonacci():
    hostname = request.args.get('hostname')
    fs_port = request.args.get('fs_port')
    number = request.args.get('number')
    as_ip = request.args.get('as_ip')
    as_port = request.args.get('as_port')

    if not all([hostname, fs_port, number, as_ip, as_port]):
        return 'Missing parameters', 400
    
    # Simulating a response from Fibonacci server
    try:
        number = int(number)
    except ValueError:
        return 'Invalid number format', 400
    
    # For now, just return the number itself as Fibonacci result
    return jsonify(fibonacci_number=number), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)