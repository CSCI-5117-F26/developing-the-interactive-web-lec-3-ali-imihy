from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def hello_world():
  return render_template('hello.html')
    



@app.route("/catch", methods=["POST"])
def catch():
  return request.form.get("name")