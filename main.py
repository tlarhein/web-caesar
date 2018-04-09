from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True


form = """
<!doctype html>
<html>
    <head>
        <style>
            form {
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 560px;
                font: 20px sans-serif;
                border-radius: 15px;
            }
            textarea {
                margin: 10px 0;
                width: 560px;
                height: 120px;
            }
        </style>
    </head>
    <body>
        <form action="/rot" method="post">
            <label for="Rotate-by">Rotate by:</label>
            <input id="Rotate-by" value = 0 type="text" name="Rotate_by" />           
            

            <label>
            <textarea name="text"></textarea>
            </label>
            <input type="submit"  />

             
        </form>
    </body>
</html>
"""
def encrypt():
    
@app.route("/")
def index():
    return form

@app.route("/rot", methods=['POST'])
def rot():
    Rotate_by = request.form['Rotate_by']
    return '<h1>Rotate By: ' + Rotate_by + '</h1>'

    

app.run()