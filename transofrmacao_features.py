import pandas as pd
import numpy as np
from scipy import stats

pd.set_option("display.width", None)

df = pd.read_csv("clientes-v2-tratados.csv")

print(df.head())

# Transformação Logarítmica
df["salario_log"] = np.log1p(df["salario"]) # log1p evitar problemas com valores zero

print("\nDataFrame após a transformação logarítmica no ""salario:\n", df.head())

# Transformação Box-Cox
df["salario_boxcox"], _ = stats.boxcox(df["salario"] + 1)

print("\nDataFrame após transformação Box-Cox no ""salario"":\n", df.head())

# Codificação de frequência para "estado"