import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import numpy as np # linear algebra
import matplotlib.pyplot as plt # for data visualization purposes
import seaborn as sns # for statistical data visualization
import warnings
import pickle

class IaModel:
    def __init__(self) -> None:
        pass

    def predict(self, dataArray):
        gnb = pickle.load('./didydoc.gnb')
