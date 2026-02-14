from flask import Flask, render_template, request
import os

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    user_input = ""
    if request.method == "POST":
        user_input = request.form.get("user_input")
    return render_template("index.html", output=user_input)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
