import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import mean_absolute_error, mean_squared_error
from tensorflow.keras.models import load_model

# Load trained models
cnn_model = load_model("C:/DATA/cnn_sentiment.h5")
rnn_model = load_model("C:/DATA/rnn_sentiment.h5")
lstm_model = load_model("C:/DATA/lstm_sentiment.h5")

# Generate synthetic test data (Assuming we have X_test and y_test)
X_test = np.load("C:/DATA/X_test.npy")  # Load preprocessed test features
y_test = np.load("C:/DATA/y_test.npy")  # Load actual sentiment labels

# Predict sentiments
cnn_pred = cnn_model.predict(X_test)
rnn_pred = rnn_model.predict(X_test)
lstm_pred = lstm_model.predict(X_test)

# Convert predictions to labels (0 = negative, 1 = neutral, 2 = positive)
cnn_pred_labels = np.argmax(cnn_pred, axis=1)
rnn_pred_labels = np.argmax(rnn_pred, axis=1)
lstm_pred_labels = np.argmax(lstm_pred, axis=1)

# Plot sentiment distribution
plt.figure(figsize=(10, 5))
sns.histplot(cnn_pred_labels, label="CNN", kde=True, color='blue', stat="density")
sns.histplot(rnn_pred_labels, label="RNN", kde=True, color='green', stat="density")
sns.histplot(lstm_pred_labels, label="LSTM", kde=True, color='red', stat="density")
plt.xlabel("Sentiment (0: Negative, 1: Neutral, 2: Positive)")
plt.ylabel("Density")
plt.legend()
plt.title("Sentiment Distribution Across Models")
plt.show()

# Evaluate model performance
metrics = {}
for model_name, pred in zip(["CNN", "RNN", "LSTM"], [cnn_pred, rnn_pred, lstm_pred]):
    mae = mean_absolute_error(y_test, pred)
    mse = mean_squared_error(y_test, pred)
    rmse = np.sqrt(mse)
    mape = np.mean(np.abs((y_test - pred) / y_test)) * 100
    metrics[model_name] = {"MAE": mae, "MSE": mse, "RMSE": rmse, "MAPE": mape}

# Plot evaluation metrics
fig, ax = plt.subplots(2, 2, figsize=(12, 10))
metric_names = ["MAE", "MSE", "RMSE", "MAPE"]
for i, metric in enumerate(metric_names):
    values = [metrics[model][metric] for model in metrics]
    ax[i // 2, i % 2].bar(metrics.keys(), values, color=["blue", "green", "red"])
    ax[i // 2, i % 2].set_title(f"{metric} Comparison")
    ax[i // 2, i % 2].set_ylabel(metric)
plt.tight_layout()
plt.show()

print("✅ Visualization and evaluation completed!")
