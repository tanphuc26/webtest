from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

@app.route('/')
def home():
    title = "haaay, world! I'm a Flask app" 
    message = ""
    return render_template('index.html', title=title, message=message)

    
if __name__ == '__main__':
    app.run(debug=True, port=8000)
