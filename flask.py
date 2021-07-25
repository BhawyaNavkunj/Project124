from flask import Flask, jsonify, request

app = Flask(__name__)

list = [
    {
        "id":1,
        "name":"Rahul",
        "contact":"9987644456",
        "done":False
    },
    {
        "id":2,
        "name":"Raja",
        "contact":"9876543222",
        "done":False
    }
]

@app.route("/")
def hello_World():
    return "hello world"

@app.route("/add-data",methods=["POST"])
def add_task():
    if not request.json:
        return jsonify({
            "status":"error",
            "message":"please provide the data"
        },400)

    contact = {
        "id":list[-1]["id"] + 1,
        "name":request.json["name"],
        "contact":request.json.get("contact",""),
        "done":False
    }
    list.append(contact)
    return jsonify({
        "status":"success",
        "message":"contact added successfully"
    })

@app.route("/get-data")
def get_task():
    return jsonify({
        "data":list
    })
if __name__ == '__main__':
    app.run(debug=True)