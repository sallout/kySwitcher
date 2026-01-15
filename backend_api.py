from flask import Flask, jsonify

app = Flask(__name__)

CURRENT_REAL_SERVER_URL = "https://api.my-secret2-server.com" 

@app.route('/')
def home():
    return "Tor Hidden Service is Running!"

@app.route('/get-url', methods=['GET'])
def get_secure_url():
    response = {
        "status": "success",
        "service_name": "Anti-Censorship Service",
        "new_url": CURRENT_REAL_SERVER_URL,
        "backup_ip": "142.99.xx.xx" # 
    }
    return jsonify(response)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)
