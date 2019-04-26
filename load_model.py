from keras.models import load_model
import numpy as np
from img_convert import im

model = load_model('ddsm_YaroslavNet_s10.h5')
model.summary()


# run prediction on image from other file
im = im.reshape(1, 1152, 896, 1)
model.predict([im])
