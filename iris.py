import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris

df = pd.DataFrame(load_iris())
print(type(df))