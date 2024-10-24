from flask import Flask, render_template, request
import re
import string
import numpy as np
import shutil
import tensorflow as tf
from keras.models import load_model
from keras import losses
app = Flask(__name__)
model=load_model('model_1.keras')
@app.route('/')
def home():
   return render_template('home.html')

@app.route('/result',methods = ['POST', 'GET'])
def result():
   if request.method == 'POST':
      result = request.form['nm']
      
      ex=[                                                              
         f"{result}"
      ]
      l=list(model.predict(ex))
      x=0
      for i in l:
         x+=1
         i=list(i)
         maxpos = i.index(max(i))
 
   return render_template("result.html",example=maxpos+1)

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000,debug=True)