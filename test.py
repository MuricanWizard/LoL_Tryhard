import numpy as np
import pandas as pd
import keras
from keras import backend as K
from keras.models import Sequential
from keras.layers import Activation
from keras.layers.core import Dense
from keras.optimizers import Adam
from keras.metrics import categorical_crossentropy
from keras.models import model_from_json
import requests
from requests.auth import HTTPBasicAuth
from sys import argv

key = open('key.txt', 'r').read()
filePath = argv[1]
lockFile = ""

while(lockFile == ""):
    try:
        lockFile = open(filePath+'/lockFile', 'r').read()
    except:
        x = int(10)

lockFile = lockFile.split(":")


print('Port: '+str(lockFile[2])+'<br> Password: '+str(lockFile[3]))
