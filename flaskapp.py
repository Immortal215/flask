from flask import Flask,jsonify, request

app = Flask("contacts")

tasks = [
    {
        'id': 1,
        'name': 'Sharul Shah',
        'contact': '123-123-1234', 
        'done': False
    },
    {
        'id': 2,
        'name': 'Keshav Shah',
        'contact': '123-123-1235', 
        'done': False
    }
]

@app.route("/add-data", methods=["POST"])
def add_contact():
    if not request.json:
        return jsonify({
            "status":"error",
            "message": "Wrong Contact!"
        },400)

    task = {
        'id': tasks[-1]['id'] + 1,
        'name': request.json['name'],
        'contact': request.json.get('contact', ""),
        'done': False
    }
    tasks.append(task)
    return jsonify({
        "status":"success",
        "message": "Right Contact!"
    })
    

@app.route("/get-data")
def get_task():
    return jsonify({
        "data" : tasks
    }) 

if ("contacts" == "__main__"):
    app.run(debug=True)