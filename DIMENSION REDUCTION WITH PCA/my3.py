from gensim.models import Word2Vec
import numpy as np
import matplotlib.pyplot as plt
model_path = 'harry_potter_word2vec.model'
model = Word2Vec.load(model_path)

list_characters_names=["rubeus",'harry',"severus","neville","lord","ron","hermione","dobby"]
listnp=[]

for a in list_characters_names:
    listnp.append(model.wv[a])

listnp=np.array(listnp).astype(np.float32)
print(listnp)
sam,att=listnp.shape
listnp_mean=np.mean(listnp,axis=0)
listnp_centered=listnp-listnp_mean

cov_matrix=(1/(sam-1))*(listnp_centered.T@listnp_centered)

eigenvalues,eigenvectors=np.linalg.eigh(cov_matrix)

sorted_eigenvalues_indexes=np.argsort(eigenvalues[::-1])
eigenvalues=eigenvalues[sorted_eigenvalues_indexes]
eigenvectors=eigenvectors[:,sorted_eigenvalues_indexes]

dimension_needed=2

pcomponents=eigenvectors[:,:dimension_needed]

theDataOn2DforCharNames=listnp_centered@pcomponents

plt.title("2D Visualization of Character Names from Harry Potter Books")
plt.scatter(theDataOn2DforCharNames[:,0],theDataOn2DforCharNames[:,1])
for a in range(len(list_characters_names)):
    plt.text(theDataOn2DforCharNames[a,0],theDataOn2DforCharNames[a,1],list_characters_names[a])
plt.xlabel("PCA Component-1")
plt.ylabel("PCA Component-2")
plt.grid()
plt.show()

