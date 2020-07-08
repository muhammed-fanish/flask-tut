from flask import *
app = Flask(__name__)

@app.route('/hello')
def hello_world():
	x={'numbers':[1,2,3,4]}
	return jsonify(x)


@app.route('/hai')
def hello_world():
	return render_template('index.html')

if __name__ == '__main__':
   app.run()