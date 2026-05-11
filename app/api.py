from flask import request, jsonify
from app import app
from app.model_handler import predict


@app.route('/predict', methods=['POST'])
def predict_route():
    data = request.get_json()
    return jsonify(predict(data))


@app.route('/health', methods=['GET'])
def health():
    return jsonify({'status': 'healthy'}), 200


# запуск сервера
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)