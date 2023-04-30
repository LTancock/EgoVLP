import numpy as np
from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
import matplotlib.patches as ptc
import seaborn as sns
import pandas as pd
import umap
#%matplotlib inline

sns.set(style='white', context='notebook', rc={'figure.figsize':(14,10)})
#penguins = pd.read_csv("https://raw.githubusercontent.com/allisonhorst/palmerpenguins/c19a904462482430170bfe2c718775ddb7dbb885/inst/extdata/penguins.csv")
#penguins = penguins.dropna()
#
#reducer = umap.UMAP()
#penguin_data = penguins[
#    [
#        "bill_length_mm",
#        "bill_depth_mm",
#        "flipper_length_mm",
#        "body_mass_g",
#    ]
#].values
#scaled_penguin_data = StandardScaler().fit_transform(penguin_data)
#
#embedding = reducer.fit_transform(scaled_penguin_data)
#print(embedding.shape)
#
#plt.scatter(
#    embedding[:, 0],
#    embedding[:, 1],
#    c=[sns.color_palette()[x] for x in penguins.species.map({"Adelie":0, "Chinstrap":1, "Gentoo":2})])
#plt.gca().set_aspect('equal', 'datalim')
#plt.title('UMAP projection of the Penguin dataset', fontsize=24);
#
#plt.savefig('penguin_plot.png')

t_embeds = np.load('./zero/text_She.npy')
v_embeds = np.load('./zero/video_She.npy')
embeds = np.concatenate((t_embeds, v_embeds), axis = 0)
print(t_embeds.shape)
print(v_embeds.shape)
#print(t_embeds)
#print(v_embeds)
print(embeds.shape)

reducer = umap.UMAP()

scaled = StandardScaler().fit_transform(embeds)

embedding = reducer.fit_transform(scaled)
print(embedding.shape)

#v_scaled = StandardScaler().fit_transform(v_embeds)

#v_embedding = reducer.fit_transform(v_scaled)
#print(v_embedding.shape)


plt.scatter(
    embedding[:len(t_embeds),0],
    embedding[:len(t_embeds),1],
    c=['red'], alpha=0.2, s=5
)
plt.scatter(
    embedding[len(t_embeds):,0],
    embedding[len(t_embeds):,1],
    c=['green'], alpha=0.2, s=5
)


plt.title('UMAP projection of the "She" prompts and the videos', fontsize=24);

#ax.axis([min(embedding([:, 0]))-1, max(embedding[:, 0])+1, min(embedding[:, 1])-1, max(embedding[:, 1])+1])

plt.savefig('plot.png')