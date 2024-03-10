from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api/data', methods=['GET'])
def get_data():
    data = {'message': 'Hello from Python server!'}
    return jsonify(data)

@app.route('/')
def home():
    return 'Welcome to the Finance App!'

@app.route('/api/accounts')
def get_accounts():
    #Implement logic to fetch and return account information
    accounts_data={
        'accounts': [
            {'name': 'Savings', 'balance' : 5000},
            {'name': 'Checking', 'balance' :2500}
        ]
    }
    return jsonify(accounts_data)




if __name__ == '__main__':
    app.run(debug=True, port=5001)