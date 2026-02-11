import streamlit as st
import pandas as pd
import numpy as np
import pickle
from tensorflow.keras.models import load_model
import time

# --- CONFIGURARE PAGINĂ ---
st.set_page_config(
    page_title="Predictor Mentenanță AI",
    page_icon="",
    layout="centered"
)

# --- FUNCȚII PENTRU ÎNCĂRCAREA MODELULUI ---
# Folosim cache pentru a nu reîncărca modelul la fiecare click (mărește viteza)
@st.cache_resource
def load_resources():
    try:
        model = load_model('mentenanta_model.h5')
        with open('scaler.pkl', 'rb') as f:
            scaler = pickle.load(f)
        return model, scaler
    except Exception as e:
        st.error(f"Eroare critică: Nu găsesc modelul sau scaler-ul! ({e})")
        return None, None

model, scaler = load_resources()

# --- INTERFAȚA GRAFICĂ ---
st.title(" AI Maintenance Predictor")
st.markdown("incarca")

# 1. Zona de Upload
uploaded_file = st.file_uploader("Alege fișierul text/csv", type=['txt', 'csv'])

if uploaded_file is not None and model is not None:
    try:
        # 2. Citirea datelor
        # Citim fișierul direct din memorie (fără header)
        df = pd.read_csv(uploaded_file, header=None)
        
        # Redenumim primele coloane pentru grafice
        # Presupunem ordinea: Voltage, Current, Power, Freq, FFT...
        df.rename(columns={0: 'Voltage', 1: 'Current', 2: 'Power', 3: 'Frequency'}, inplace=True)

        st.write("###  Analiză Date")
        
        # Verificare lungime
        if len(df) < 60:
            st.warning(f" Fișierul are doar {len(df)} rânduri. Am nevoie de minim 60.")
        else:
            # Luăm ultimele 60 de rânduri
            last_60_df = df.tail(60)
            last_60_values = last_60_df.values
            
            # 3. Preprocesare & Predicție
            # Scalăm datele
            scaled_data = scaler.transform(last_60_values)
            # Reshape pentru LSTM (1, 60, features)
            X_input = np.expand_dims(scaled_data, axis=0)
            
            # Bara de progres pentru efect vizual
            progress_bar = st.progress(0)
            for percent_complete in range(100):
                time.sleep(0.01)
                progress_bar.progress(percent_complete + 1)
            
            # Predicția efectivă
            prediction = model.predict(X_input, verbose=0)[0][0]
            
            # 4. Afișare Rezultat
            st.divider()
            col1, col2 = st.columns([2, 1])
            
            with col1:
                st.subheader("Rezultat Diagnostic:")
                if prediction > 0.5:
                    st.error(" ALERTĂ: MENTENANȚĂ NECESARĂ!")
                    st.markdown("**Motiv:** Modelul a detectat anomalii severe (probabil cădere de tensiune sau zgomot pe rețea).")
                else:
                    st.success(" SISTEM OK: Funcționare Normală")
                    st.markdown("**Status:** Parametrii sunt în limitele optime.")
            
            with col2:
                st.metric(label="Probabilitate Defect", value=f"{prediction:.1%}")

            # 5. Grafice Explicative (Ca să vezi DE CE a luat decizia)
            st.divider()
            st.subheader("📈 Vizualizare Parametri (Ultimele 60 secunde)")
            
            tab1, tab2 = st.tabs(["Tensiune (Voltage)", "Curent (Current)"])
            
            with tab1:
                st.line_chart(last_60_df['Voltage'])
                # Adăugăm o notă dacă tensiunea e suspectă
                avg_volt = last_60_df['Voltage'].mean()
                if avg_volt < 215 or avg_volt > 245:
                    st.caption(" Observație: Tensiunea medie este în afara limitelor normale (230V).")
            
            with tab2:
                st.line_chart(last_60_df['Current'])

    except Exception as e:
        st.error(f"Eroare la procesarea fișierului: {e}")