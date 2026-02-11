# Etapa 5 – Antrenarea Modelului RN pentru Mentenanță Predictivă
**Disciplina:** Rețele Neuronale – POLITEHNICA București  
**Student:** Ștefan Radu  
**Data:** 10.12.2025  

---

## 1. Scopul Etapei 5

În această etapă am antrenat modelul RN proiectat în Etapa 4, folosind:

- setul public Smart Grid Monitoring (Kaggle)
- + ≥40% date originale generate în Etapa 4
- pipeline-ul de preprocesare realizat în Etapa 3
- arhitectura RN CNN+LSTM definită în Etapa 4

Scopul este obținerea unui model complet antrenat, evaluat și integrat în UI.

---

## 2. Pipeline-ul de date utilizat

- Date brute (public + originale)
- Curățare și standardizare cu `StandardScaler`
- Construire ferestre secvențiale de **60 minute**
- Split:
  - 70% train  
  - 15% validation  
  - 15% test  

Modelul primește ca input formele:  
`(batch_size, 60 timesteps, num_features)`.

---

## 3. Arhitectura RN folosită (identică Etapa 4)

Modelul CNN + LSTM folosit:

```
Conv1D(64, kernel_size=3, activation='relu')
MaxPooling1D(2)
LSTM(128, return_sequences=True)
Dropout(0.2)
LSTM(64)
Dropout(0.2)
Dense(64, activation='relu')
Dense(1, activation='sigmoid')
```

Compilare:

```python
model.compile(
    optimizer='adam',
    loss='binary_crossentropy',
    metrics=['accuracy']
)
```

---

## 4. Hiperparametrii modelului

| Hiperparametru | Valoare | Justificare |
|----------------|---------|-------------|
| Learning rate | 0.001 | Stabil pentru Adam |
| Batch size | 32 | Bun pentru date secvențiale |
| Epoci | 30 | Convergență rapidă + EarlyStopping |
| Window size | 60 | Reprezintă 1 oră completă |
| Loss function | Binary Crossentropy | Clasificare binară |
| Optimizer | Adam | Eficient pentru time series |
| Callbacks | EarlyStopping, ReduceLROnPlateau | Previne overfitting |

---

## 5. Rezultate pe setul de test

| Metrică | Valoare |
|---------|---------|
| **Acuratețe test** | **1.0000** |
| Loss test | ~2.4e-06 |
| F1-score | 1.00 |

Curbele de antrenare sunt salvate în:
```
docs/loss_curve.png
```

---

## 6. Confusion Matrix

Fișier:  
```
docs/confusion_matrix.png
```

Confusion matrix arată clasificare perfectă a secvențelor testate.

---

## 7. Analiza erorilor

Chiar dacă performanța este excelentă, pot apărea limitări în aplicarea reală:

### 1. Situații rare (edge-cases)
Variații extreme sau combinații neobișnuite pot necesita date suplimentare.

### 2. Dezechilibru natural al claselor
În exploatarea reală, majoritatea timpului nodul este “normal”.

### 3. Zgomot de măsurare
Senzorii industriali au zgomot mai ridicat decât datele simulate.

### 4. Generalizare limitată
Modelul trebuie validat și pe alte noduri / alte stații electrice.

---

## 8. Integrarea modelului în aplicația finală

Modelul complet antrenat este salvat în:

```
models/trained_model.h5
```

A fost integrat în UI, unde:

- se încarcă ultimele 60 minute de date
- se rulează inferența cu modelul real
- se afișează probabilitatea de mentenanță necesară

---

## 9. Screenshot cu inferență reală (OBLIGATORIU)

Fișierul a fost adăugat în:

```
docs/screenshots/inference_real.png
```

---

## 10. Fișiere generate în Etapa 5

```
models/trained_model.h5
docs/screenshots/inference_real.png
docs/loss_curve.png
docs/confusion_matrix.png
results/training_history.csv
results/test_metrics.json
```

---

## 11. Instrucțiuni de rulare

### Antrenare:
```
python src/neural_network/train_maintenance_predict.py
```

### UI:
```
streamlit run src/app/main.py
```

---

## ✔️ Etapa 5 – COMPLET FINALIZATĂ

Documentul include:
- hiperparametri
- metrici de test
- analiza erorilor
- integrarea modelului în UI
- model antrenat
- screenshot cerut  
Toate cerințele Moodle sunt îndeplinite.

