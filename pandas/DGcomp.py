import pickle
import numpy as np
import pandas as pd
import tbapy
import DatabaseGen as GBG
import os

tba = tbapy.TBA(os.environ['TBAKEY'])
GBG.genBase("2017alhu", tba)
print("2017alhu done")
GBG.genBase("2017cada", tba)
print("2017cada done")
GBG.genBase("2017code", tba)
print("2017code done")
GBG.genBase("2017iacf", tba)
print("2017iacf done")
GBG.genBase("2017lake", tba)
print("2017lake done")
GBG.genBase("2017okok", tba)
print("2017okok done")
GBG.genBase("2017tnkn", tba)
print("2017tnkn done")
GBG.genBase("2017wimi", tba)
print("2017wimi done")

data = pd.read_pickle("2017alhu" + "pandas" + ".p")
data = data.append(pd.read_pickle("2017cada" + "pandas" + ".p"))
data = data.append(pd.read_pickle("2017code" + "pandas" + ".p"))
data = data.append(pd.read_pickle("2017iacf" + "pandas" + ".p"))
data = data.append(pd.read_pickle("2017lake" + "pandas" + ".p"))
data = data.append(pd.read_pickle("2017okok" + "pandas" + ".p"))
data = data.append(pd.read_pickle("2017tnkn" + "pandas" + ".p"))
data = data.append(pd.read_pickle("2017wimi" + "pandas" + ".p"))
data.to_pickle("week3" + ".p")
