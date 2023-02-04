from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'This is a repository which discusses git, github and vscode integration!'


if __name__=="__main__":
    app.run(debug=True)