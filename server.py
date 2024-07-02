from flask import Flask, render_template, redirect

app = Flask(__name__)


@app.route("/")
def index():
    return redirect("/play")


@app.route("/play")
def play():
    """This will display a 3 blue boxes"""
    return render_template("index.html", num=3, color="#17a2b8")


@app.route("/play/<int:num>/<color>")
def play_num_color(num, color):
    return render_template("index.html", num=num, color=color)


@app.route("/play/<int:num>")
def play_num(num):
    return render_template("index.html", num=num, color="#17a2b8")


if __name__ == "__main__":
    app.run(debug=True)
