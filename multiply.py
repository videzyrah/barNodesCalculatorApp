from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/success", methods=['POST'])
def success():
    if request.method=='POST':
       factor1=request.form["factor1"]
       factor2=request.form["factor2"]
       theSum = int(factor1)*int(factor2)
       print(factor1, factor2)
       return render_template("index.html", theSum= theSum)

if __name__ == '__main__':
    app.debug=True
    app.run()
