from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    
    return render_template("index.html")

@app.route("/animal")
def animales():
    
    return render_template("animales.html")

@app.route("/vehic")
def vehiculos():
    
    return render_template("vehiculos.html")

@app.route("/marav")
def maravillas():
    
    return render_template("maravillas.html")

@app.route("/acerc")
def acercas():
    
    return render_template("acerca.html")

if __name__ == "__main__":
    app.run(debug=True)