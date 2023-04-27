import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

ghi_2021_df = pd.read_csv("global-hunger-index.csv")
df_underweight = pd.read_csv("share-of-children-underweight.csv")
# retard de croissance enfant -5ans
df_stunting = pd.read_csv(
    "share-of-children-younger-than-5-who-suffer-from-stunting.csv")
# émaciation enfant de -5ans
df_wasting = pd.read_csv(
    "share-of-children-with-a-weight-too-low-for-their-height-wasting.csv")
