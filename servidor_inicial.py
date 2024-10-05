from flask import Flask, request

app = Flask(__name__) 
		
@app.route("/") 
def index():
    return "Bem vindo pessoal"

if __name__ == "__main__": 
    app.run(debug=True) 