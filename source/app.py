from flask import Flask

app = Flask(__name__)
variable = "Hello mundo"
variable1 = variable
variable2 = variable1
    
@app.route("/")
def index():
    variable2 = variable1
    variable2 = variable1
    variable2 = variable1
    return variable2

def indexvacio():
    return

if __name__ == "__main__":
    app.run()
