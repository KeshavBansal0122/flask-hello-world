from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return '''
<!DOCTYPE html>
<html lang="en">
<head>
    <title>My Webpage</title>
</head>
<body>
    <h1>My Webpage</h1>
    {{ flask.Flask.config }}

    
</body>
</html>
    '''

@app.route('/about')
def about():
    return 'About'