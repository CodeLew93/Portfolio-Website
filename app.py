from flask import Flask, render_template, redirect, url_for
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/redirecting")
def returnhome():
    return redirect(url_for("home"))

@app.route("/nichecycle")
def nichecycle():
    return render_template("nichecycle.html")

@app.route("/flaskwp")
def flaskwp():
    return render_template("flaskwp.html")

@app.route("/mlproject")
def mlproject():
    return render_template("mlproject.html")

@app.route("/sudoko")
def sudokosolver():
    return render_template("sudoko.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/savefood")
def savefood():
    return render_template("savefood.html")

if __name__ == "__main__":
    app.run(debug=True)       