'''
Create a Flask application and write a route that displays the following
strings:
– ”Welcome to Flask Development!”
– ”This is Labwork 3: Flask/MySQL/API”
 Display these strings at the /welcome route.
'''

from flask import Flask
app = Flask(__name__) # similar to the public static void main thingy

@app.route('/welcome')
def welcome():
    return 'Welcome to Flask Development!\nThis is Labwork 3: Flask/MySQL/API'

# make the server run when executing the file directly
if __name__ == "__main__":
    app.run(debug=True)
