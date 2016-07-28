from flask import Flask, redirect, url_for


app = Flask(__name__)

@app.route('/')
def todo():
	return 'hello!'

@app.route('/new', methods =['POST'])
def new():
	return redirect(url_for('todo'))

if __name == "__main__":
	app.run(debug=True)