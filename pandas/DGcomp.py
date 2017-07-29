import pickle
import numpy as np
import pandas as pd
import tbapy
import DatabaseGen as GBG

tba = tbapy.TBA('w4sdTrGh4f4ueC0pfm5ZceCZp3yM3I0SRsJLrn1oblRowvr3Zx2UbcXQpaWnZSpK')
GBG.genBase("2017alhu", tba)
GBG.genBase("2017cada", tba)
GBG.genBase("2017code", tba)
GBG.genBase("2017iacf", tba)
GBG.genBase("2017lake", tba)
GBG.genBase("2017okok", tba)
GBG.genBase("2017tnkn", tba)
GBG.genBase("2017wimi", tba)

data = pd.read_pickle("2017alhu" + "pandas" + ".p")
data = data.append(pd.read_pickle("2017cada" + "pandas" + ".p"))
data = data.append(pd.read_pickle("2017code" + "pandas" + ".p"))
data = data.append(pd.read_pickle("2017iacf" + "pandas" + ".p"))
data = data.append(pd.read_pickle("2017lake" + "pandas" + ".p"))
data = data.append(pd.read_pickle("2017okok" + "pandas" + ".p"))
data = data.append(pd.read_pickle("2017tnkn" + "pandas" + ".p"))
data = data.append(pd.read_pickle("2017wimi" + "pandas" + ".p"))
data.to_pickle("week3" + ".p")
