import numpy as np
import os

def read_one(path):
    band = np.loadtxt(path, delimiter=";")
    return band

def read_many(path):
    lband = []
    for root, dirs, files in os.walk(path):
        for file in files:
            tmp = path + "\\" + file
            band = read_one(tmp)
            lband.append(band)
    stack = np.dstack(np.array(lband))
    return stack



path_in = r"c:/MY_PATH_TO_CSV_FOLDER\csv"
stack = read_many(path_in)
print(stack.shape)





