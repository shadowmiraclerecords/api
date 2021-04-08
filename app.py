from flask import Flask, request, jsonify
from store import store
app = Flask(__name__)

port = 5100
# Set the secret key to some random bytes. Keep this really secret!
# app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

@app.route('/write', methods=['POST'])
def write():
    message = request.json
    print('testing')
    email = message.get('email', '')
    print(email)
    print('testing')
    store(email)
    return jsonify(message)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=port)