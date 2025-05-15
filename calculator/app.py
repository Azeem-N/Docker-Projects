from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/calculate", methods=["GET"])
def calculate():
    operation = request.args.get("operation")
    num1 = request.args.get("num1", type=float)
    num2 = request.args.get("num2", type=float)

    if operation not in ["add", "sub", "mul", "div"]:
        return jsonify({"error": "Invalid operation"}), 400

    try:
        if operation == "add":
            result = num1 + num2
        elif operation == "sub":
            result = num1 - num2
        elif operation == "mul":
            result = num1 * num2
        elif operation == "div":
            if num2 == 0:
                return jsonify({"error": "Cannot divide by zero"}), 400
            result = num1 / num2

        return jsonify({"operation": operation, "num1": num1, "num2": num2, "result": result})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)