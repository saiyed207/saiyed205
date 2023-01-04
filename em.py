import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.cluster import KMeans
df1 = pd.read_csv("dataset.csv")
print(df1)
f1 = df1['Distance_Feature'].values
f2 = df1['Speeding_Feature'].values

x = np.matrix(list(zip(f1,f2)))
plt.plot(1)
plt.subplot(511)
plt.xlim([0, 100])
plt.ylim([0, 50])
plt.title('dataset')
plt.ylabel('speeding_feature')
plt.xlabel('distance_feature')
plt.scatter(f1,f2)

colors = ['b', 'g', 'r']
markers = ['o', 'v', 's']

ax=plt.subplot(513)
kmeans_model =KMeans(n_clusters=3).fit(x)

for i,l in enumerate(kmeans_model.labels_):
    plt.plot(f1[i], f2[i], color=colors[l],marker=markers[l])

plt.xlim([0, 100])
plt.ylim([0, 50])
plt.title('k- Means')
plt.ylabel('Speeding_Feature')
plt.xlabel('Distance_Feature')

plt.show()

