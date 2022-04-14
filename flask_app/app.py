from flask import Flask,render_template,request
import numpy as np
import pandas as pd
import pickle

app = Flask(__name__)

@app.route("/", methods=["POST","GET"])

def test():
    if request.method=="POST" and "size" in request.form:
        None
    
    return render_template("index.html")



if __name__=="__main__":
  app.run()