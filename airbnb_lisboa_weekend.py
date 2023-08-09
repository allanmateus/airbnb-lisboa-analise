# %%
# Informações
# Este dataset contém dados sobre imóveis da plataforma AirBnb situados em Lisboa - PT


# %%
# Com o python instalado, execute no terminal o comando: "pip install pandas"

# Importando as bibliotecas
import seaborn as sn
import pandas as pd
import matplotlib.pyplot as plt

# %%
# Carregando o dataframe
df = pd.read_csv("./dataset/lisbon_weekends.csv")
df

# %%
# Informações gerais sobre o dataframe
df.shape
df.head()
df.describe()
df.info

# %%
# Excluindo colunas desnecessárias
df_dropped = df.drop(columns="Unnamed: 0")
df_dropped

# %%
_ = plt.hist(df_dropped.guest_satisfaction_overall)

# %%
df_corr = df_dropped.corr(numeric_only=True)
df_corr

# %%
sn.heatmap(df_corr, annot = True, linewidth=.5, cmap="crest")
