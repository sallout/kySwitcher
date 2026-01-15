from flask import Flask, jsonify
import json
app = Flask(__name__)

CURRENT_REAL_SERVER_URL = "https://api.my-secret3-server.com" 

@app.route('/')
def home():
    return "Tor Hidden Service is Running!"

@app.route('/get-url', methods=['GET'])
def get_secure_url():
    response = {
        "status": "success",
         "new_ips": ["85.211.249.43", "85.211.243.22", "85.211.192.119"]
    }
    
    return json.dumps(payload)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)
