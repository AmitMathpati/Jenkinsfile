from flask import Flask

app = Flask(__name__)

@app.route("/")
def welcome():
    return "welcome to our website"

@app.route("/name")
def name():
    return "ITD DevOps"

@app.route("/ip")
def ip():
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    return "ip_address"

if __name__ == '__main__':
    app.run(host="0.0.0.0",port="8080")
