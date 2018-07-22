#%%
import pandas as pd

df = pd.read_csv('E:\Git_Projects\machine learning\MachineLearningWithPython\iris.csv', header=None)
df.head()

#%%
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np

#%%
x = np.linspace(0, 25, 100)
plt.plot(x, np.cos(x))
plt.show() 