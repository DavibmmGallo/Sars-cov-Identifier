from flask import Flask, render_template
import os

app = Flask(__name__,template_folder=os.getcwd() + "\\Html",static_folder=os.getcwd() + "\\static")

@app.route("/")
def homepage():
    return (
        render_template('test.html')
    ) 
if __name__ == '__main__':
    app.run(debug=True)