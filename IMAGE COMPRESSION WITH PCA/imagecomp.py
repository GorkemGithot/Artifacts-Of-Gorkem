import numpy as np
import matplotlib.pyplot as plt
import cv2

image = cv2.imread('image.jpg')
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)


print(image.shape)

h,w,d=image.shape

r,g,b=cv2.split(image)

r_mean=np.mean(r,axis=0)
g_mean=np.mean(g,axis=0)
b_mean=np.mean(b,axis=0)

r_centered=r-r_mean
g_centered=g-g_mean
b_centered=b-b_mean

cov_matrix_r=(1/(h-1))*(r_centered.T@r_centered)
cov_matrix_g=(1/(h-1))*(g_centered.T@g_centered)
cov_matrix_b=(1/(h-1))*(b_centered.T@b_centered)

eigenvalues_r,eigenvector_r=np.linalg.eigh(cov_matrix_r)
eigenvalues_g,eigenvector_g=np.linalg.eigh(cov_matrix_g)
eigenvalues_b,eigenvector_b=np.linalg.eigh(cov_matrix_b)

sorted_indexes_r=np.argsort(eigenvalues_r)[::-1]
sorted_indexes_g=np.argsort(eigenvalues_g)[::-1]
sorted_indexes_b=np.argsort(eigenvalues_b)[::-1]

eigenvalues_r=eigenvalues_r[sorted_indexes_r]
eigenvalues_g=eigenvalues_g[sorted_indexes_g]
eigenvalues_b=eigenvalues_b[sorted_indexes_b]

eigenvector_r=eigenvector_r[:,sorted_indexes_r]
eigenvector_g=eigenvector_g[:,sorted_indexes_g]
eigenvector_b=eigenvector_b[:,sorted_indexes_b]
list1=[10, 20, 50, 100]
for a in list1:
    k=a

    pca_R=eigenvector_r[:,:k]
    pca_G=eigenvector_g[:,:k]
    pca_B=eigenvector_b[:,:k]


    image_pca_r=r_centered@pca_R
    image_pca_g=g_centered@pca_G
    image_pca_b=b_centered@pca_B

    reconstructed_r = (image_pca_r @ pca_R.T) + r_mean
    reconstructed_g = (image_pca_g @ pca_G.T) + g_mean
    reconstructed_b = (image_pca_b @ pca_B.T) + b_mean

    compressed_img = cv2.merge([reconstructed_r, reconstructed_g, reconstructed_b])


    compressed_img = np.clip(compressed_img, 0, 255).astype(np.uint8)

    
    plt.title(f"for first {a} principal components:")

    plt.imshow(compressed_img)
    plt.show()
    plt.imsave(f"saved_imgs/savedimage{a}.jpg",compressed_img)