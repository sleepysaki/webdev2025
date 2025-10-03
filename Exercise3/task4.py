'''
Write a Flask route that accepts a number as a URL parameter and
calculates the factorial of the number.
- Example URL: /factorial/5
 - The function should return the factorial of the number using Python’s
math module.
'''

from flask import Flask
app = Flask(__name__)

@app.route('/factorial/<int:number>')
def factorialCalculation(number):
    result = 1
    for i in range (number, 0, -1):
        result = result * i
    return str(result)

if __name__ == "__main__":
    app.run(debug = True)    
    

'''
using Python math module:

from flask import Flask
import math

app = Flask(__name__)

@app.route('/factorial/<int:number>')
def factorialCalculation(number):
    result = math.factorial(number)
    return f"The factorial of {number} is {result}"

if __name__ == "__main__":
    app.run(debug=True)

'''    