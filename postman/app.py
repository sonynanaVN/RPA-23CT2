from flask import Flask, request, jsonify

app = Flask(__name__)

# API GET
@app.route("/", methods=["GET"])
def home():
    return "Hello Postman!"

# API POST
@app.route("/login", methods=["POST"])
def login():
    data = request.json

    username = data.get("username")
    password = data.get("password")

    if username == "admin" and password == "123":
        return jsonify({
            "message": "Đăng nhập thành công"
        })
    else:
        return jsonify({
            "message": "Sai tài khoản hoặc mật khẩu"
        })

if __name__ == "__main__":
    app.run(debug=True)