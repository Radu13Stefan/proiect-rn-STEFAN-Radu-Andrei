import pandas as pd
import numpy as np
import pickle
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense, Dropout


df = pd.read_csv('smart_grid_dataset.csv')


if 'Timestamp' in df.columns:
    df = df.drop(columns=['Timestamp'])

target_col = 'Fault Indicator'
df['Need_Maintenance'] = df[target_col].apply(lambda x: 1 if x > 0 else 0)

features = [c for c in df.columns if c not in [target_col, 'Need_Maintenance']]
data_values = df[features].values
labels = df['Need_Maintenance'].values

scaler = MinMaxScaler(feature_range=(0, 1))
data_scaled = scaler.fit_transform(data_values)

with open('scaler.pkl', 'wb') as f:
    pickle.dump(scaler, f)

X = []
y = []
window_size = 60

for i in range(window_size, len(data_scaled)):
    X.append(data_scaled[i-window_size:i])
    y.append(labels[i])

X, y = np.array(X), np.array(y)

model = Sequential()
model.add(LSTM(units=50, return_sequences=True, input_shape=(X.shape[1], X.shape[2])))
model.add(Dropout(0.2))
model.add(LSTM(units=50))
model.add(Dropout(0.2))
model.add(Dense(units=1, activation='sigmoid')) # Sigmoid pentru ieșire 0 sau 1

model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

print("Se antrenează modelul...")
model.fit(X, y, epochs=10, batch_size=32, validation_split=0.1)

model.save('mentenanta_model.h5')
print("Modelul și scaler-ul au fost salvate cu succes!")