from flask import Flask, send_file
app = Flask(__name__)

@app.route("/", methods=['GET'])
def callbackAaio():
    return send_file("/root/lil-time-tracker/front.html")


if __name__ == '__main__':
    app.run(host="0.0.0.0", port="8080")