from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    
    return render_template("index.html")

@app.route("/anim")
def animales():
    
    return render_template("animales.html")

@app.route("/vehi")
def vehiculos():
    
    return render_template("vehiculos.html")

@app.route("/mara")
def maravillas():
    
    return render_template("maravillas.html")

@app.route("/acer")
def acercas():
    
    return render_template("acerca.html")

if __name__ == "__main__":
    app.run(debug=True)