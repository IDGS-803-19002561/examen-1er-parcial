
from flask import Flask, render_template, request, jsonify

from pytest import main

from arithmetic_arranger import TuclaseExamen

# create the class instance
obj = TuclaseExamen()

app = Flask(__name__)


@app.route("/")
def index():
    return render_template('index.html')


@app.route("/arimetic", methods=['POST'])
def comprar():

    operation = []
    
    num1=str(request.form.get('op1'))      
    if (len(num1) > 0) : operation.append(num1)
    
    num2=str(request.form.get('op2'))      
    if (len(num2) > 0) : operation.append(num2)

    num3=str(request.form.get('op3'))      
    if (len(num3) > 0) : operation.append(num3)

    num4=str(request.form.get('op4'))      
    if (len(num4) > 0) : operation.append(num4)
    
    response = obj.arithmetic_arranger(operation, True)
    print(response)

    return jsonify([response])

if __name__ == '__main__':
    app.run(debug=True)
