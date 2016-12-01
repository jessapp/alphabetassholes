from flask import Flask, flash, redirect, render_template, request, session, abort, url_for

app = Flask(__name__)

@app.route("/")
def hello():
	return render_template(
		'home.html',**locals())

@app.route("/about")
def about():
	return render_template(
		'about.html',**locals())

@app.route("/lettera")
def lettera():
	return render_template(
		'lettera.html',**locals())

@app.route("/letterb")
def letterb():
	return render_template(
		'letterb.html',**locals())

@app.route("/letterc")
def letterc():
	return render_template(
		'letterc.html',**locals())

if __name__ == "__main__":
	app.run()