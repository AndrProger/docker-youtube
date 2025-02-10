from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "Привет, Docker! Hello!"

@app.route('/info')
def info():
    data = {
        "status": "success",
        "message": "Это JSON-ответ от Flask-приложения, запущенного в Docker"
    }
    return jsonify(data)

if __name__ == '__main__':
    # Приложение слушает все интерфейсы на порту 5000
    app.run(host='0.0.0.0', port=5000)
