'''
Write a Flask route that accepts a string as a URL parameter and
returns the reversed string.
 Example URL: /reverse string/hello
 Output should be "olleh".
'''

from flask import Flask
app = Flask(__name__)

@app.route("/reverse_string/<string:text>")
def reverse(text):
    # slicing
    return text[::-1]

if __name__ == "__main__":
    app.run(debug=True)
