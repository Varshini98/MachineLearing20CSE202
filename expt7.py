import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_breast_cancer
cancer=load_breast_cancer()
df=pd.DataFrame(cancer['data'],columns=cancer['feature_names'])
df.head()
from sklearn.preprocessing import StandardScaler
scalar=StandardScaler()
scalar.fit(df)
scaled_data=scalar.transform(df)
from sklearn.decomposition import PCA
pca=PCA(n_components=2)
pca.fit(scaled_data)
x_pca=pca.transform(scaled_data)
x_pca.shape
plt.figure(figsize=((10,8)))
plt.show()
plt.scatter(x_pca[:,0],x_pca[:,1],c=cancer['target'],cmap='plasma')
plt.xlabel('first principal component')
plt.ylabel('second principal component')
pca.components_
df_comp=pd.DataFrame(pca.components_,columns=cancer['feature_names'])
plt.figure(figsize=(14,6))
sns.heatmap(df_comp)
