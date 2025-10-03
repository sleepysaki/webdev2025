'''
Write a Flask route that accepts a number as a URL parameter and
checks if the number is prime.
Example URL: /is_prime/7
Return "Prime" if the number is prime, otherwise return "Not Prime".
'''

from flask import Flask
app = Flask(__name__)

@app.route('/is_prime/<int:number>')

def primeCheck(number):
    if number < 2:
        return "Not Prime"
    # divide by every number from 2 to sqrt(n)
    for i in range (2, int(number**0.5) + 1):
        if number % i == 0:
            return "Not Prime"
    return "Prime"
    
if __name__ == "__main__":
    app.run(debug=True)