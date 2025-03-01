from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
        <body style="display:flex;justify-content:center;align-items:center;">
            <h1>Hello from Server 1</h1>
        </body>
    """

if __name__ == "__main__":
    app.run(port=5001)