from flask import Flask, render_template 

app = Flask(__name__)

@app.route("/")
def hello_world():
#    return "<p>Hello, World! HOLA !!!</p>"
    data = {
        'titulo':'Bienvenida',
        'saludo':'Saludos !!!'
    }
    return render_template('index.html',data=data)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8080)