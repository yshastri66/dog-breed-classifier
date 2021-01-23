# Dog Breed Classifier with Heroku deployment
[![TensorFlow 2.3](https://img.shields.io/badge/TensorFlow-2.3-FF6F00?logo=tensorflow)](https://github.com/tensorflow/tensorflow/releases/tag/v2.3.0)
[![Python 3.6](https://img.shields.io/badge/Python-3.6-3776AB)](https://www.python.org/downloads/release/python-360/)<br>

This is a project which detects 30 different dog breeds.

### Key features are :

<ul>
  <li> This model is trained on Tensorflow 2.3.0 object classification.</li>
  <li> To train the model, famous <a href="https://www.kaggle.com/c/dog-breed-identification/data">Kaggle Dataset</a> which consists of 120 different breeds, out of which 30 famous breeds were taken for simplicity.</li>
  <li> Took nearly 2.5k images of 30 breeds.</li>
  <li> For training,<b>Inception v3</b> model as base model is used for feature extraction.</li>
  <li> After training, training accuracy reached <b>99%</b> with testing accuracy nearing <b>94%.</b></li>
  <li> Deployed the model with python and having <b>'Flask'</b> as backend and <b>'gunicorn'</b> as server.</li>
</ul>
<br>

<h3><b>Visit dog-breed-classification website with <a href ="https://dog-breeds-detector.herokuapp.com/"> This link </a>.</b></h3>
<h3> Detailed training is explained in final_building_model.ipynb file. </h3>
<h4>Trained model 'smart_model_mobile.h5' is available in google drive with <a href="https://drive.google.com/drive/folders/1RE_mwLyMT_rVyvokb5OPnHKOQXRWvZu5?usp=sharing">this link</a></h4>



<b>Snapshot of the website's Front page and Breed page where name of breeds which model can predict are mentioned.</b>

  <img src="https://github.com/yshastri66/dog-breed-classifier/blob/main/static/website%20photos/Screenshot%20from%202020-11-27%2018-26-14.png" alt="homepage"  width="800" height="450">
  <img src="https://github.com/yshastri66/dog-breed-classifier/blob/main/static/website%20photos/Screenshot%20from%202020-11-27%2018-26-18.png" alt="homepage"      width="800" height="450">
<br>
<h4>This is the prediction page before uploading and after uploading and getting predictions:-<br></h4>

  <img src="https://github.com/yshastri66/dog-breed-classifier/blob/main/static/website%20photos/Screenshot%20from%202020-11-27%2018-26-28.png" alt="homepage" width="800" height="450">
  <img src="https://github.com/yshastri66/dog-breed-classifier/blob/main/static/website%20photos/Screenshot%20from%202020-11-27%2018-26-49.png" alt="homepage" width="800" height="450">

#### Feel free to contact me incase on any quaries
### Yashodhara Shastri G
#### yashodharashastri6@gmail.com
