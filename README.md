# Dog Breed Classifier with Heroku deployment
[![TensorFlow 2.3](https://img.shields.io/badge/TensorFlow-2.3-FF6F00?logo=tensorflow)](https://github.com/tensorflow/tensorflow/releases/tag/v2.3.0)
[![Python 3.6](https://img.shields.io/badge/Python-3.6-3776AB)](https://www.python.org/downloads/release/python-360/)<br>

This is a project which detects 30 different dog breeds.

### Key features are :

<ul>
  <li> This model is trained on Tensorflow 2.3.0 object classification.</li>
  <li> I used famous <a href="https://www.kaggle.com/c/dog-breed-identification/data">Kaggle Dataset</a> which consists of 120 different breeds out of which I took 30 famous breeds for simplicity</li>
  <li> I took nearly 2.5k images of 30 breeds.</li>
  <li> Here I used <b>Inception v3</b> model as my base model for feature extraction </li>
  <li> I got training accuracy reaching <b>99%</b> with testing accuracy of <b>94%.</b></li>
</ul>
<br>

#### Detailed training is explained in final_building_model.ipynb file.
<br>
#### Trained model is available in my drive with <a href="https://drive.google.com/drive/folders/1RE_mwLyMT_rVyvokb5OPnHKOQXRWvZu5?usp=sharing">this link</a>
<br>
#### I had deployed this model with python and having Flask as my backend and gunicorn as server.
<br>
#### Snapshot of the website Front page and Breed page where name of breeds which model can predict are mentioned.
<br>
<div>
<img src="https://github.com/yshastri66/dog-breed-classifier/blob/main/static/website%20photos/Screenshot%20from%202020-11-27%2018-26-14.png" alt="homepage" width="475" height="500">
<img src="https://github.com/yshastri66/dog-breed-classifier/blob/main/static/website%20photos/Screenshot%20from%202020-11-27%2018-26-18.png" alt="homepage" width="475" height="500">
</div>
<br>
#### This is the prediction page before uploading and after uploading and getting predictions:-<br>
<div>
  <img src="https://github.com/yshastri66/dog-breed-classifier/blob/main/static/website%20photos/Screenshot%20from%202020-11-27%2018-26-28.png" alt="homepage" width="475" height="500">
  <img src="https://github.com/yshastri66/dog-breed-classifier/blob/main/static/website%20photos/Screenshot%20from%202020-11-27%2018-26-49.png" alt="homepage" width="475" height="500">
</div>
