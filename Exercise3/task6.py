'''
Write a Flask route that accepts a list of numbers (via URL query
parameters) and returns the sorted array.
 Example URL: /sort?numbers=4,2,9,1
 Return the sorted array in ascending order
'''

from flask import Flask, request

app = Flask(__name__)

@app.route('/sort')
def sort_numbers():
    numbers_str = request.args.get("numbers")   # get query param value as string
    if not numbers_str:
        return "Please provide numbers like ?numbers=4,2,9,1"

    # Split the string into a list of strings → convert to integers
    numbers = [int(x) for x in numbers_str.split(",")]

    # Sort the list
    numbers.sort()

    return str(numbers)   # Flask must return string (or JSON if requested)

if __name__ == "__main__":
    app.run(debug=True)
