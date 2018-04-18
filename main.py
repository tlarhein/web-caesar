from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True

form = """
<!doctype html>
<html>
    <head>
        <style>
            form {{
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }}
            textarea {{
                margin: 10px 0;
                {0}
                width: 540px;
                height: 120px;
            }}
        </style>
    </head>
    <body>
        <form class="cipher-form" action = "/" method="post">
        <textarea name="text" placeholders="Enter Message to Encrypt:">{0}</textarea>
        <div>
            <label for="rot">Rotate by:</label>
            <input type="text" id="Rotate_by" name="Rotate_by" value ="0">           
        </div>   

        
        
        <input type="submit" value="Submit Query" >
            
        </form>
    </body>
</html>
"""

@app.route("/")
def index():
    return form.format("")


@app.route("/", methods=['POST'])
def encrypt():
    rot = int(request.form['Rotate_by'])
    rotated_text = str(request.form['text'])
    encrypted_text = rotate_string(rotated_text, rot)
    return form.format(encrypted_text)

app.run()