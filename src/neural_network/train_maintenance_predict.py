import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense, Dropout, Conv1D, MaxPooling1D
from tensorflow.keras.callbacks import EarlyStopping

# =====================================================
# 1. Load dataset
# =====================================================

df = pd.read_csv("smart_grid_dataset.csv")
df["Timestamp"] = pd.to_datetime(df["Timestamp"])
df = df.sort_values("Timestamp").reset_index(drop=True)

# =====================================================
# 2. Create maintenance label (predict next 60 minutes)
# =====================================================

HORIZON = 60  # minutes into the future

fault = df["Fault Indicator"].values
maint = np.zeros(len(fault), dtype=np.int32)

for i in range(len(fault) - HORIZON):
    future_window = fault[i+1:i+HORIZON+1]
    if np.any((future_window == 1) | (future_window == 2)):
        maint[i] = 1
    else:
        maint[i] = 0

df["MaintenanceNeeded"] = maint

# Remove last HORIZON rows because they have incomplete labels
df = df.iloc[:-HORIZON]

# =====================================================
# 3. Prepare features
# =====================================================

df["hour"] = df["Timestamp"].dt.hour
df["dayofweek"] = df["Timestamp"].dt.dayofweek

feature_cols = [c for c in df.columns 
                if c not in ["Timestamp", "Fault Indicator", "MaintenanceNeeded"]]

X = df[feature_cols].values.astype("float32")
y = df["MaintenanceNeeded"].values.astype("float32")

# =====================================================
# 4. Scale features
# =====================================================

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# =====================================================
# 5. Create sequences (past 60 minutes)
# =====================================================

WINDOW = 60

def make_sequences(X, y, win):
    Xs, ys = [], []
    for i in range(win, len(X)):
        Xs.append(X[i-win:i])
        ys.append(y[i])
    return np.array(Xs), np.array(ys)

X_seq, y_seq = make_sequences(X_scaled, y, WINDOW)

# =====================================================
# 6. Train / Val / Test split (time-based)
# =====================================================

n = len(X_seq)
train_end = int(0.7 * n)
val_end = int(0.85 * n)

X_train, y_train = X_seq[:train_end], y_seq[:train_end]
X_val, y_val = X_seq[train_end:val_end], y_seq[train_end:val_end]
X_test, y_test = X_seq[val_end:], y_seq[val_end:]

# =====================================================
# 7. Build hybrid model (Conv1D + LSTM)
# =====================================================

model = Sequential([
    Conv1D(64, kernel_size=3, activation="relu", input_shape=(WINDOW, X.shape[1])),
    MaxPooling1D(pool_size=2),

    LSTM(128, return_sequences=True),
    Dropout(0.3),

    LSTM(64),
    Dropout(0.3),

    Dense(64, activation="relu"),
    Dense(1, activation="sigmoid")
])

model.compile(
    optimizer="adam",
    loss="binary_crossentropy",
    metrics=["accuracy"]
)

model.summary()

# =====================================================
# 8. Train model
# =====================================================

early = EarlyStopping(patience=5, restore_best_weights=True)

history = model.fit(
    X_train, y_train,
    validation_data=(X_val, y_val),
    epochs=30,
    batch_size=32,
    callbacks=[early],
    verbose=1
)

# =====================================================
# 9. Evaluate
# =====================================================

loss, acc = model.evaluate(X_test, y_test)
print(f"\nTest accuracy: {acc:.4f}")
