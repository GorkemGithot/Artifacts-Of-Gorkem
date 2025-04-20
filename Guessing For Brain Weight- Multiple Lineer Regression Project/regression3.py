import numpy as np
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt  


with open(r"dataset.csv", "r") as file:
    all_lines = file.readlines()
    all_lines_2 = []
    for i in all_lines:
        a = i.split(",")
        all_lines_2.append(a)
    all_lines_2.pop(0)  
    all_lines_3 = []
    for a in all_lines_2:
        new_b = a[3].rstrip("\n")
        all_lines_3.append(new_b)
    for a in all_lines_2:
        a.pop(3)
    needed = []
    for a in all_lines_2:
        needed.append(a[2])

needed = np.array(needed).astype(float)
mean_value = np.mean(needed)
std_value = np.std(needed)
needed_standardized = (needed - mean_value) / std_value

k = 0
for a in all_lines_2:
    a[2] = needed_standardized[k]
    k += 1

realFeatures = np.array(all_lines_2).astype(float)
bias = np.ones((len(realFeatures), 1))
realValues = np.array(all_lines_3).astype(float)
scaler = StandardScaler()
realFeatures_standardized = scaler.fit_transform(realFeatures)
X = np.concatenate((bias, realFeatures_standardized), axis=1)

def LossMSE(y_true, y_pred):
    return np.mean((y_true - y_pred) ** 2)

def LossRMSE(y_true, y_pred):
    mse = LossMSE(y_true, y_pred)
    return np.sqrt(mse)

def LossMAE(y_true, y_pred):
    return np.mean(np.abs(y_true - y_pred))


alpha = 0.01
n_iterations = 1000
n_samples, n_features = X.shape
beta = np.zeros((n_features, 1))


mse_list = []
rmse_list = []
mae_list = []

for iteration in range(n_iterations):
    Y_pred = np.matmul(X, beta)
    residuals = Y_pred - realValues.reshape(-1, 1)

    lossforMSE = LossMSE(realValues.reshape(-1, 1), Y_pred)
    lossforRMSE = LossRMSE(realValues.reshape(-1, 1), Y_pred)
    lossforMAE = LossMAE(realValues.reshape(-1, 1), Y_pred)

    print(f"Iteration {iteration + 1}: MSE = {lossforMSE}")
    print(f"Iteration {iteration + 1}: RMSE = {lossforRMSE}")
    print(f"Iteration {iteration + 1}: MAE = {lossforMAE}")
    print()
    

    mse_list.append(lossforMSE)
    rmse_list.append(lossforRMSE)
    mae_list.append(lossforMAE)

    gradient = (2 / n_samples) * np.matmul(X.T, residuals)
    beta = beta - alpha * gradient


plt.figure(figsize=(15, 5))

plt.subplot(1, 3, 1)
plt.plot(mse_list, label="MSE", color="blue")
plt.title("MSE Over Iterations")
plt.xlabel("Iterations")
plt.ylabel("MSE")
plt.legend()

plt.subplot(1, 3, 2)
plt.plot(rmse_list, label="RMSE", color="green")
plt.title("RMSE Over Iterations")
plt.xlabel("Iterations")
plt.ylabel("RMSE")
plt.legend()

plt.subplot(1, 3, 3)
plt.plot(mae_list, label="MAE", color="red")
plt.title("MAE Over Iterations")
plt.xlabel("Iterations")
plt.ylabel("MAE")
plt.legend()

plt.tight_layout()
plt.show()

print(f"Estimated Coefficients after Gradient Descent: \n{beta}")
print()
Estimate = np.matmul(X, beta)
print(f"Predicted Brain Weights: \n{Estimate}")

plt.figure(figsize=(8, 6))  
plt.scatter(range(len(Estimate)), Estimate, color='blue', label='Gerçek Değerler', alpha=0.7)
plt.scatter(range(len(realValues)), realValues, color='orange', label='Tahmin Edilen Değerler', alpha=0.7)
plt.xlabel('Örnek İndeksi')
plt.ylabel('Beyin Ağırlığı (grams)')
plt.title('Gerçek vs Tahmin Edilen Değerler (Farklı Renklerde)')
plt.legend()
plt.show()