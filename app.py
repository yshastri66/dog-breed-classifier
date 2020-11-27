from flask import Flask,render_template,request
import os
from utils import pipeline_model

app = Flask(__name__)

@app.route('/')
def main():
    return render_template("main.html")


@app.route('/breed')
def breed():
    return render_template("breed.html")

@app.route('/predict',methods=['GET','POST'])
def predict():
    if request.method=='POST':
        img = request.files['image']
        filename = img.filename
        path = os.path.join('static/uploads',filename)
        img.save(path)
        print(filename)

        predictions = pipeline_model(path)
        return render_template("predict.html",p="uploads/{}".format(filename),pred=predictions)
    return render_template("predict.html",p="images/dog.jpg",pred="")


if __name__ == '__main__':
    app.run(port=8000,debug=True)



