from flask import Flask, jsonify, request
from waitress import serve

app= Flask(__name__)

@app.route("/")
def home():
    return "Hello Ssekamatte"

if __name__=="__main__":
    serve(app, host="0.0.0.0", port=3319)
    #app.run(debug=True,host="0.0.0.0",port=80)