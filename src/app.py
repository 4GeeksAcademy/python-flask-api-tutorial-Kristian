from flask import Flask, jsonify, request
app = Flask(__name__)

todos = [
    { "label": "Make the bed", "done": False }
]

@app.route('/todos', methods=['GET'])
def hello_world():
    json_text = jsonify(todos)
    return json_text

@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.json
    todos.append(request_body)
    print("Incoming request with the following body", request_body)
    return jsonify(todos)

@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    if 0 <= position < len(todos):
        todos.pop(position)
        return jsonify(todos), 200
    else:
        return jsonify({"msg": f"todo {position} not found"}, 404)

if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = 3245, debug = True)