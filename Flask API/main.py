# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import flask

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print('Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

from flask import Flask,render_template,request

app = Flask(__name__)


def multiplication(num1,num2):
    return (num1*num2)

def addition(num1,num2):
    return (num1+num2)

def subtraction(num1,num2):
    return (num1-num2)

def division(num1,num2):
    return (num1/num2)


ans=0
@app.route("/returnjson" , methods=['POST','GET'])
def hello():
    if request.method=='GET':
        num1 = int( request.form['num1'])
        num2 = int(request.form['num2'])
        if(request.form['button']=='calculate'):
            add=addition(num1, num2)
            msg= "Addition of {num1} and {num2} is {add} \n".format( num1=num1, num2 = num2, add=add)
            sub = subtraction(num1, num2)
            msg += " Subtraction of {num1} and {num2} is {sub} \n".format(num1=num1, num2=num2, sub=sub)
            mul = multiplication(num1, num2)
            msg += " Multiplication of {num1} and {num2} is {mul} \n".format(num1=num1, num2=num2, mul=mul)
            div = division(num1, num2)
            msg += " Division of {num1} and {num2} is {div} \n".format(num1=num1, num2=num2, div=div)
            print(msg)
            return jsonify(msg)
            #return render_template('home.html', msg=(msg))
    return render_template('home.html')


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('Jerome Edwin')
    app.run(debug=True)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
