from flask import Flask, render_template
import random
 
app = Flask(__name__)
 
@app.route("/sea")
def hello():
    return render_template("april\index.html")
 
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
