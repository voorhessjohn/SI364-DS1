## Discussion Section 1
## SI 364 F17

# Running Instructions
## We would not be setting up a virtual environment to run this application, and instead would use the flask package that comes with anaconda3.
## To run this application, cd to the folder containing this application
## First type into terminal export FLASK_APP=SI364-DS1.py
## If you are on Windows you need to use set instead of export.
## Next, type : python -m flask run

# Part 1
## Below is code for one of the simplest possible Flask applications.
## We will edit the code for discussion function so that once we run this application locally and
## go to the URL 'http://localhost:5000/discussion', we will see a page that says "Welcome to first discussion of SI 364!"

from flask import Flask
app = Flask(__name__)
app.debug = True

@app.route('/')
@app.route('/index')
def index():
    return 'Hello, World!'

@app.route('/discussion')
#def discussion():
    # type a return statement to return "Welcome to first discussion of SI 364!"

# Part 2
## We will now edit the code so that once we run this application locally and go to the
## URL 'http://localhost:5000/discussion/<sectionNumber>', we will see a page that says "Welcome to discussion <number> of SI 364!"
## For this, edit the function discussionId to take the variable sectionNumber as a parameter.
## Use the format method in return statement to say 'Welcome to discussion <sectionNumber> of SI 364!'
## HINT: 'Hello {}!'.format('world') would result in string 'Hello world!'

@app.route('/discussion/<sectionNumber>')
#def discussionId():

if __name__ == '__main__':
    app.run()
