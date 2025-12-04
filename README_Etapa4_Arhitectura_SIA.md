# 📘 README – Etapa 4: Arhitectura Completă a Aplicației SIA bazată pe Rețele Neuronale

**Disciplina:** Rețele Neuronale  
**Instituție:** POLITEHNICA București – FIIR  
**Student:** ȘTEFAN Radu  
**Link Repository GitHub:** [https://github.com/Radu13Stefan/proiectRN.git]  
**Data:** 04.12.2025  


## 1. Tabel Nevoie Reală → Soluție SIA → Modul Software

Aplicația vizează **mentenanța predictivă pentru un nod din rețeaua electrică de joasă tensiune** (smart-grid). Nevoile și soluțiile software sunt:

| **Nevoie reală concretă** | **Cum o rezolvă SIA-ul meu** | **Modul software responsabil** |
|---------------------------|------------------------------|--------------------------------|
| Detectarea din timp a unui comportament anormal într-un nod de rețea înainte să apară o problema | Analiză secvențială pe ferestre de 60 min și → etichetă `MaintenanceNeeded = 0/1` | Modul 2 – RN (Conv1D + LSTM) + Modul 1 – Data Logging & Preprocessing |

| Reducerea timpului de reacție al personalului de mentenanță la incidente în nod| Web UI / API care afișează în timp real probabilitatea de mentenanță necesară și generează o alertă dacă `P(MaintenanceNeeded) > threshold` | Modul 3 – Web Service / UI |

| Evaluarea stării nodului în funcție de condiții variabile de încărcare | Generare și logare de date (reale + sintetice) pentru diferite scenarii de sarcină, apoi antrenarea RN  → model robust la situații de sarcină variate | Modul 1 – Data Logging / Acquisition + `data/generated/` |

---

## 3. Contribuția originală la setul de date

> **Notă importantă pentru profesor:** baza de pornire este datasetul public *Smart Grid Monitoring* (Kaggle). 
### Contribuția originală la setul de date:

- **Total observații finale:** 1 000 mostre 
 
**Tipul contribuției:**

- ✅ Date generate prin simulare fizică  
- ⬜ Date achiziționate cu senzori proprii  
- ⬜ Etichetare/adnotare manuală  
- ⬜ Date sintetice prin metode avansate (GAN etc.)

### Descriere detaliată

Am pornit de la semnalele reale din datasetul public (tensiune, curent, putere, frecvență + componente FFT) 

- variații ale tensiunii în jurul valorii nominale (+/- 10%) în funcție de sarcină;
- curenți care cresc sau scad în trepte, asociate cu apariția/oprirea unor consumatori mari;
- pattern-uri de frecvență ușor deviată (49.5–50.5 Hz) pentru scenarii de instabilitate;
- componente FFT coerente cu aceste modificări.

Sunt definite două tipuri mari de scenarii:

1. **Funcționare normală** – sarcină variabilă, dar parametrii rămân în limite admise → `MaintenanceNeeded = 0`.  
2. **Funcționare degradată** – combinații de:
   - tensiune sub 210 V sau peste 245 V pe perioade prelungite;
   - curent aproape de limitele admise;
   - frecvență instabilă;  
   → aceste scenarii sunt etichetate ca `MaintenanceNeeded = 1`, ele cer verificare/mentenanță în următoarea oră.

Generatorul creează ferestre secvențiale de 60 de minute cu rezoluție 1 minut. Datele trec printr-un pipeline de preprocesare (scalare, creare de secvențe).

**Locația codului:**

- `src/data_acquisition/generate_smartgrid_synthetic.py` – script de generare date originale  

**Locația datelor:**

- `data/raw/kaggle_smartgrid/` – datasetul original  

**Dovezi:**

## 4. Diagrama State Machine a Întregului Sistem



### Justificarea State Machine-ului ales

Aplicația mea este un **sistem de monitorizare continuă a unui nod din rețeaua electrică** cu predicție de mentenanță. Din acest motiv, arhitectura de tip *monitorizare continuă + inferență RN + alertare* este cea mai potrivită.


Tranziții critice:

- `IDLE → ACQUIRE_DATA` la pornirea aplicației sau la un nou ciclu de predicție.  
- `ACQUIRE_DATA → PREPROCESS` atunci când un buffer de date (de ex. cel puțin 60 de minute de măsurători) este complet.  
- `PREPROCESS → RN_INFERENCE` după ce datele sunt scalate și organizate în ferestre.  
- `RN_INFERENCE → THRESHOLD_CHECK` după ce s-a calculat probabilitatea de mentenanță.  
- `THRESHOLD_CHECK → DISPLAY_AND_LOG` pentru caz normal;  
  `THRESHOLD_CHECK → ALERT` pentru caz critic.  
- `ANY_STATE → ERROR` în caz de excepție 


## 5. Scheletul celor 3 Module Cerute

### 5.1 Modul 1 – Data Logging / Acquisition


## 6. Structura Repository-ului după Etapa 4

```text
proiect-rn-stefan-radu/
├── data/
│   ├── raw/
│   │   └── kaggle_smartgrid.csv
│   ├── generated/  
│   ├── processed/  
│   ├── train/
│   ├── validation/
│   └── test/
├── src/
│   ├── data_acquisition/
│   ├── preprocessing/
│   ├── neural_network/
│   │   └── train_maintenance_predict.py
│   └── app/
├── docs/
│   └── screenshots/
├── models/
├── config/
├── README.md
├── README_Etapa3.md
└── README_Etapa4_Arhitectura_SIA.md  
