import pandas as pd
import numpy as np
import pickle
from tensorflow.keras.models import load_model
import os

# Setări
INPUT_FILE = 'date_live.txt'
MODEL_FILE = 'mentenanta_model.h5'
SCALER_FILE = 'scaler.pkl'
WINDOW_SIZE = 60

def prezice_mentenanta():
    if not os.path.exists(INPUT_FILE):
        print(f"Fișierul {INPUT_FILE} nu a fost găsit. Rulează generatorul întâi.")
        return

    try:
        model = load_model(MODEL_FILE)
        with open(SCALER_FILE, 'rb') as f:
            scaler = pickle.load(f)
    except Exception as e:
        print(f"Eroare la încărcarea modelului: {e}")
        return

    try:
        df_new = pd.read_csv(INPUT_FILE, header=None)
        
        if len(df_new) < WINDOW_SIZE:
            print(f"Nu sunt destule date. Am nevoie de minim {WINDOW_SIZE} rânduri, am găsit doar {len(df_new)}.")
            return
            
        last_60_rows = df_new.tail(WINDOW_SIZE).values
        
        
        last_60_scaled = scaler.transform(last_60_rows)
        
        X_input = np.expand_dims(last_60_scaled, axis=0)
        
        prediction_prob = model.predict(X_input, verbose=0)[0][0]
        
        threshold = 0.5
        
        print("\n" + "="*40)
        print(f"Probabilitate defect: {prediction_prob:.4f}")
        
        if prediction_prob > threshold:
            print(" ALERTA: MENTENANȚĂ NECESARĂ! (Defect prezis)")
        else:
            print(" SISTEM OK. Funcționare normală.")
        print("="*40 + "\n")

    except Exception as e:
        print(f"Eroare la procesarea datelor: {e}")

if __name__ == "__main__":
    prezice_mentenanta()