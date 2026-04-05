from flask import Flask, jsonify
import math

app = Flask(__name__)

def is_prime_number(n):
    """
    Check if a number is prime.

    Args:
        n (int): Number to check

    Returns:
        bool: True if prime, False otherwise
    """
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    limit = int(math.sqrt(n)) + 1
    for i in range(3, limit, 2):
        if n % i == 0:
            return False
    return True

@app.route('/prime_number/<int:number>', methods=['GET'])
def check_prime(number):
    """
    Check if a number is prime and return JSON response.

    Args:
        number (int): Number to check (from URL parameter)

    Returns:
        JSON: {"Number": number, "isPrime": boolean}
    """
    is_prime = is_prime_number(number)

    return jsonify({
        "Number": number,
        "isPrime": is_prime
    })

@app.route('/prime_number/<path:invalid>', methods=['GET'])
def handle_invalid_number(invalid):
    """
    Handle non-integer inputs.
    """
    return jsonify({
        "error": f"'{invalid}' is not a valid integer",
        "message": "Please provide an integer number"
    }), 400

@app.route('/', methods=['GET'])
def home():
    """
    Home endpoint with usage information.
    """
    return jsonify({
        "service": "Prime Number Checker",
        "usage": "/prime_number/{number}",
        "example": "/prime_number/31",
        "examples": {
            "prime": "/prime_number/31",
            "not_prime": "/prime_number/100",
            "edge_case": "/prime_number/1"
        }
    })

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)