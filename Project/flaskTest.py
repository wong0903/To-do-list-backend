from flask import Flask, jsonify, request
import json
import controller as control

app = Flask(__name__)

@app.route("/api/getTask", methods = ['GET'])
def getTask(): 
	return jsonify(control.getTask())

@app.route("/api/createTask", methods = ['POST'])
def createTask(): 
	content = request.get_json(silent=True)
	return jsonify(control.createTask(content))
	# return jsonify(control.createTask(request.form))


@app.route("/api/removeTask", methods = ['POST'])
def removeTask():
	return jsonify(control.removeTask(request.form.get('id')))

@app.route("/api/viewUserTask", methods = ['POST'])
def viewUserTask():
	return jsonify(control.viewUserTask(request.form.get('id')))

@app.route("/api/register", methods = ['POST'])
def register():
	return jsonify(control.register(request.form))

@app.route("/api/login", methods = ['POST'])
def login():
	return jsonify(control.login(request.form))


if __name__ == "__main__":
	app.run(debug=True)


