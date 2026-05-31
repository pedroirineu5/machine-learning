# %% 
import pandas as pd 

df = pd.read_excel(r"C:/Estudos/machine-learning/dados/dados_frutas.xlsx")
df

# %%
from sklearn import tree

arvore = tree.DecisionTreeClassifier(random_state=42)

y = df["Fruta"]

# %%
caracteristicas = ["Arredondada","Suculenta","Vermelha", "Doce"]
X = df[caracteristicas]
#%%
"""
Aqui elas precisam ter o mesmo tamanho, por conta que as caracteristicas podem estar discrepantes, e para ensinar a alguma

Btw, Isso aqui é machine learning
"""

arvore.fit(X,y)

# %%

arvore.predict([[1,0,0,0]])