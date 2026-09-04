from flask import Flask, jsonify
import time

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({
        "status": "success",
        "message": "DevOps CI/CD Pipeline Executed Successfully!",
        "timestamp": time.time()
    })

@app.route('/health')
def health_check():
    return jsonify({
        "status": "healthy",
        "service": "DevOps Monitoring App"
    }), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
