from flask import Flask, render_template
from flask import request, redirect
from calculadora import calculadora
import this



app = Flask(__name__) #Referência ao objeto Flask, criando uma variável APP que guarda os elementos do Flask.
calc = calculadora()

this.resultadoFinal = ""

@app.route("/") #Página Index - primeira página de qualquer site.
def homepage():
    return render_template("index.html")


@app.route("/soma", methods=['POST','GET'])
def soma():
        if request.method == 'POST':
            numero1 = request.form['num1']
            numero2 = request.form['num2']
            this.resultadoFinal = calc.somar(numero1, numero2)
        return render_template("soma.html", titulo = "Soma", resultado = this.resultadoFinal)
            


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    app.run(debug=True)