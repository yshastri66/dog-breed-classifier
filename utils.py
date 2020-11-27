import os
#os.environ["CUDA_DEVICE_ORDER"]="PCI_BUS_ID"
#os.environ["CUDA_VISIBLE_DEVICES"]="-1"  # or even "-1"

from tensorflow.keras.preprocessing import image
from tensorflow.keras.models import load_model
import tensorflow as tf
import numpy as np
from glob import glob

model = load_model('smart_model_mobile.h5')



labels = {0:'Afghan Hound',1:'Basenji', 2:'Basset',3:'Beagle',4:'Bloodhound',5:'Boxer',6:'Bull Mastiff',7:'Chihuahua',8:'Collie',
            9:'Doberman',10:'French Bulldog',11:'German Shepherd',12:'Golden Retriever',13:'Great Dane',
         14:'Irish Water Spaniel',15:'Italian Greyhound',16:'Kerry Blue Terrier',17:'Labrador Retriever',
         18:'Miniature Pinscher',19:'Miniature Poodle',20:'Old English Sheepdog',21:'Pug', 22:'Rottweiler',23:'Saint Bernard',
         24:'Samoyed', 25:'Shih-tzu',26:'Siberian Husky',27:'Standard Poodle',28:'Tibetan Mastiff',29:'Yorkshire Terrier'}


def pipeline_model(path):
    img = image.load_img(path,target_size=(299,299))
    img = image.img_to_array(img)
    img = img/255.0
    img = np.expand_dims(img,axis=0)

    pred = model.predict(img)
    max_preds = []
    pred = pred[0]
    for i in range(5):
        name = labels[pred.argmax()]
        per = round(np.amax(pred)*100,2)
        max_preds.append([name,per])
        ele = pred.argmax()
        pred = np.delete(pred,ele)

    paths = glob('static/uploads/*')
    if len(paths)>5:
        for path in paths[:4]:
            os.remove(path)
    return max_preds
