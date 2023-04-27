import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import missingno as msno

# GHI 2000>2021
ghi_2021_df = pd.read_csv("global-hunger-index.csv")
# sous poids chez l'enfant
df_underweight = pd.read_csv("share-of-children-underweight.csv")
# retard de croissance enfant -5ans
df_stunting = pd.read_csv(
    "share-of-children-younger-than-5-who-suffer-from-stunting.csv")
# émaciation enfant de -5ans
df_wasting = pd.read_csv(
    "share-of-children-with-a-weight-too-low-for-their-height-wasting.csv")

ghi_2021_df.head()

df_underweight.head()

df_stunting.head()

df_wasting.head()

ghi_2021_df = ghi_2021_df.pivot(
    index='Entity', columns='Year', values='Global Hunger Index (2021)')

ghi_2021_df = ghi_2021_df.reset_index()
ghi_2021_df.head()

ghi_2021_df.columns = ["Country", "ghi_2000",
                       "ghi_2006", "ghi_2012", "ghi_2021"]
ghi_2021_df

# GHI 2000>2021 - DATA CLEANING
ghi_2021_df["Country"] = ghi_2021_df["Country"].apply(
    lambda x: x.split(' (')[0])
ghi_2021_df["Country"] = ghi_2021_df["Country"].apply(
    lambda x: ''.join([a for a in x if not a.isnumeric()]))
ghi_2021_df["Country"].unique()

ghi_2021_df["Country"].shape


# GHI 2014_2022 - DATA CLEANING
ghi_2022_df = pd.read_excel("GHI 2022-version2.xlsx")
ghi_2022_df

ghi_2022_df["Country"] = ghi_2022_df["Country"].apply(
    lambda z: z.split(' (')[0])
ghi_2022_df["Country"] = ghi_2022_df["Country"].apply(
    lambda z: ''.join([b for b in z if not b.isnumeric()]))
ghi_2022_df["Country"] = ghi_2022_df["Country"].replace("&", "and", regex=True)
ghi_2022_df["Country"] = ghi_2022_df["Country"].replace(
    "Syrian", "Syria", regex=True)
ghi_2022_df["Country"] = ghi_2022_df["Country"].replace(
    "Türkiye", "Turkey", regex=True)
ghi_2022_df["Country"] = ghi_2022_df["Country"].replace(
    "Rep,", "Republic", regex=True)
ghi_2022_df["Country"] = ghi_2022_df["Country"].replace(
    "Dem,", "Democratic", regex=True)
ghi_2022_df["Country"] = ghi_2022_df["Country"].replace(
    "the Congo", "Congo", regex=True)
ghi_2022_df["Country"] = ghi_2022_df["Country"].replace(
    "Russian Federation", "Russia", regex=True)
# ghi_2022_df["Country"] = ghi_2022_df["Country"].apply(lambda r: r.split('Dem,')[0])
ghi_2022_df["Country"] = ghi_2022_df["Country"].replace(
    "Timor-Leste", "Timor Leste", regex=True)
ghi_2022_df["Country"] = ghi_2022_df["Country"].replace(
    "Cabo Verde", "Cape Verde", regex=True)
ghi_2022_df["Country"] = ghi_2022_df["Country"].replace(
    "Côte d'Ivoire", "Cote d'Ivoire", regex=True)
ghi_2022_df["Country"] = ghi_2022_df["Country"].replace(
    "Korea", "North Korea", regex=True)
ghi_2022_df["Country"] = ghi_2022_df["Country"].replace(
    "Slovak Republic", "Slovakia", regex=True)
ghi_2022_df["Country"] = ghi_2022_df["Country"].replace(
    "Lao PDR", "Laos", regex=True)
ghi_2022_df["Country"] = ghi_2022_df["Country"].replace(
    "", "Slovakia", regex=True)
ghi_2022_df["Country"].unique()
# ghi_2022_df.shape

ghi_2022_df

# JOINTURE DES TABLES GHI
ghi_merged = ghi_2021_df.merge(ghi_2022_df, on="Country", how='outer')
ghi_merged.head(15)

ghi_merged.columns = ["Country", "ghi_2000", "ghi_2006",
                      "ghi_2012", "ghi_2014", "ghi_2021", "ghi_2022"]
ghi_merged.head()
ghi_merged.shape  # 134 lignes et 7 colonnes

# GESTION DES VALEURS MANQUANTES
# dropna() supprime
# fillna() : remplir avec la valeur moyenne, la valeur la plus commune
# interpolate() : remplacer la moyenne de la valeur d'avant et la moyenne d'après
# moyenne mobile : moyenne des 3 valeurs pour remplacer la valeur NaN
ghi_merged.isna().sum()  # True = proportions de valeurs manquantes
# en 2000, nous avons +16% de valeurs manquantes sur un tableau de 134 lignes ! Nous décidons d'interpoler les valeurs manquantes

(ghi_merged['ghi_2000'] == ghi_merged['ghi_2000']).sum()  # 112 True
len(ghi_merged) - (ghi_merged['ghi_2000'] == ghi_merged['ghi_2000']).sum()
# 22 valeurs manquantes dans colonne ghi_2000

msno.matrix(ghi_merged)

# distribution du GHI par année et par pays
ghi_merged.value_counts()

# visualisation colonne le plus marqué par valeurs manquantes
ghi_merged["ghi_2021"].plot()

# interpolation avec méthode quadratic pour remplir les nan de manière plus réaliste
ghi_merged.interpolate(method='quadratic').plot()
