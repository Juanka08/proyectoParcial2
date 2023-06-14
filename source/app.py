from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    variable = "Hello, world!"
    variable1 = variable
    variable2 = variable1
    return variable2

if __name__ == "__main__":
    app.run()
