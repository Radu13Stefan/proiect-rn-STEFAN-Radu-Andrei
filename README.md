## 1. Identificare Proiect

| Câmp | Valoare |
|------|---------|
| **Student** | [Stefan Radu-Andrei] |
| **Grupa / Specializare** | [633AB / Informatică Industrială] |
| **Disciplina** | Rețele Neuronale |
| **Instituție** | POLITEHNICA București – FIIR |
| **Link Repository GitHub** | [https://github.com/Radu13Stefan/proiectRN.git] |
| **Acces Repository** | [PublicN] |
| **Stack Tehnologic** | [Python] |
| **Domeniul Industrial de Interes (DII)** | [Energie] |
| **Tip Rețea Neuronală** | [LSTM] |

### Rezultate Cheie (Versiunea Finală vs Etapa 6)

| Metric | Țintă Minimă | Rezultat Etapa 6 | Rezultat Final | Îmbunătățire | Status |
|--------|--------------|------------------|----------------|--------------|--------|
| Accuracy (Test Set) | ≥70% | [52%] | [99.2%] | [+47.2%] | [✓] |
| F1-Score (Macro) | ≥0.65 | [0.51] | [0.99] | [+0.48] | [✓] |
| Latență Inferență | [ <100 ms] | [45 ms] | [48 ms] | [+3 ms] | [✗] |
| Contribuție Date Originale | ≥40% | [0%] | [50%] | [+50%] | [✓] |
| Nr. Experimente Optimizare | ≥4 | [1] | [4] | [+3] | [✓] |

### Declarație de Originalitate & Politica de Utilizare AI

**Acest proiect reflectă munca, gândirea și deciziile mele proprii.**

Utilizarea asistenților de inteligență artificială (ChatGPT, Claude, Grok, GitHub Copilot etc.) este **permisă și încurajată** ca unealtă de dezvoltare – pentru explicații, generare de idei, sugestii de cod, debugging, structurarea documentației sau rafinarea textelor.

**Nu este permis** să preiau:
- cod, arhitectură RN sau soluție luată aproape integral de la un asistent AI fără modificări și raționamente proprii semnificative,
- dataset-uri publice fără contribuție proprie substanțială (minimum 40% din observațiile finale – conform cerinței obligatorii Etapa 4),
- conținut esențial care nu poartă amprenta clară a propriei mele înțelegeri.

**Confirmare explicită (bifez doar ce este adevărat):**

| Nr. | Cerință                                                                 | Confirmare |
|-----|-------------------------------------------------------------------------|------------|
| 1   | Modelul RN a fost antrenat **de la zero** (weights inițializate random, **NU** model pre-antrenat descărcat) | [✓] DA     |
| 2   | Minimum **40% din date sunt contribuție originală** (generate/achiziționate/etichetate de mine) | [✓] DA     |
| 3   | Codul este propriu sau sursele externe sunt **citate explicit** în Bibliografie | [✓] DA     |
| 4   | Arhitectura, codul și interpretarea rezultatelor reprezintă **muncă proprie** (AI folosit doar ca tool, nu ca sursă integrală de cod/dataset) | [✓] DA     |
| 5   | Pot explica și justifica **fiecare decizie importantă** cu argumente proprii | [✓] DA     |

**Semnătură student (prin completare):** Declar pe propria răspundere că informațiile de mai sus sunt corecte.

---

## 2. Descrierea Nevoii și Soluția SIA

### 2.1 Nevoia Reală / Studiul de Caz

Echipamentele moderne pot fi extrem de sensibile la fluctuatii de tensiune si armonici. Releele clasice reactioneaza reactiv si de multe ori declanseaza alarme false din cauza zgomotului de pe retea, sau rateaza defecte in stadiul incipient care nu trec de pragul critic ales. Aceste limitari ale releelor clasice duc la degradarea echipamentelor in timp.

Proiectul se bazeaza pe rezolvarea acestei probleme prin detectarea defectelor bazata pe un model de inteligenta artificiala LSTM ce analizeaza o fereastra temporala bazata pe ultimele 60 de mostre de date colectate. Sistemul este capabil sa faca diferenta intre o fluctuatie momentana si un tipar ce duce spre avarii. Este mult mai eficient un model bazat pe mentenanta predictiva fata de unul reactiv.


### 2.2 Beneficii Măsurabile Urmărite

*[Listați 3-5 beneficii concrete cu metrici țintă]*

1. [Latenta < 50 ms]
2. [False positives reduse cu 80%]
3. [Monitorizare 24/7]
4. [Acuratete >99%]

### 2.3 Tabel: Nevoie → Soluție SIA → Modul Software

| **Nevoie reală concretă** | **Cum o rezolvă SIA-ul** | **Modul software responsabil** | **Metric măsurabil** |
|---------------------------|--------------------------|--------------------------------|----------------------|
| [Detectarea caderilor de tensiune] | [Analiza serii temporale cu LSTM] | [Modul RN] | [Recall>99%] |
| [Validare vizuala alarma de catre utilizator] | [Generare grafice tensiune vs timp in timp real] | [Modul UI streamlit] | [Latenta < 50 ms] |
| [Eliminare erori pe date incomplete] | [State Machine cu stare de input validation] | [Madul Data logging] | [Nu am detectat crashes] |

---

## 3. Dataset și Contribuție Originală

### 3.1 Sursa și Caracteristicile Datelor

| Caracteristică | Valoare |
|----------------|---------|
| **Origine date** | [Mixt] |
| **Sursa concretă** | [Kaggle + Script Python propriu] |
| **Număr total observații finale (N)** | [20,000] |
| **Număr features** | [132] |
| **Tipuri de date** | [Numerice + Serii temporale] |
| **Format fișiere** | [CSV] |
| **Perioada colectării/generării** | [ex: Noiembrie 2025 - Ianuarie 2026] |

### 3.2 Contribuția Originală (minim 40% OBLIGATORIU)

| Câmp | Valoare |
|------|---------|
| **Total observații finale (N)** | [20000] |
| **Observații originale (M)** | [10000] |
| **Procent contribuție originală** | [50%] |
| **Tip contribuție** | [Simulare fizică si reetichetare] |
| **Locație cod generare** | `generatorRELE.py``generatorBUNE.py` |
| **Locație date originale** | `data_live.txt` |

**Descriere metodă generare/achiziție:**

Am dezvoltat doua scripturi de generare care simuleaza comportamentul real al unui Smart Grid. Am folosit formule din electrotehnica pentru a genera valori coerente pentru tensiune curent si putere. Peste ele am suprapus zgomot gaussian si armonici FFT.

Dataset-ul public continea etichete inconsistente. Am generat propriile scenarii pentru a forta modelul sa invete regulile fizice reale ci nu doar zgomotul statistic din dataset-ul orignial.



### 3.3 Preprocesare și Split Date

| Set | Procent | Număr Observații |
|-----|---------|------------------|
| Train | 70% | [14000] |
| Validation | 15% | [3000] |
| Test | 15% | [3000] |

**Preprocesări aplicate:**
- [Normalizare Min-Max]
- [Physics-informed labeling]
- [Sliding window]
- [Eliminare coloane irelevante]

**Referințe fișiere:** `scaler.pk1` `antrenare.py` 

---

## 4. Arhitectura SIA și State Machine

### 4.1 Cele 3 Module Software

| Modul | Tehnologie | Funcționalitate Principală | Locație în Repo |
|-------|------------|---------------------------|-----------------|
| **Data Logging / Acquisition** | [Python(NumPy Random)] | [simulare senzori] | `generatorRELE.py``generatorBUNE.py` |
| **Neural Network** | [Python (Keras/TensorFlow)] | [Detectie anomalii LSTM] | `antrenare.py``mentenanta_model.h5` |
| **Web Service / UI** | [Web Service/UI] | [Streamlit] | `app.py` |

### 4.2 State Machine

**Locație diagramă:** `docs/state_machine.png` *(sau `state_machine_v2.png` dacă actualizată în Etapa 6)*

**Stări principale și descriere:**

| Stare | Descriere | Condiție Intrare | Condiție Ieșire |
|-------|-----------|------------------|-----------------|
| `IDLE` | [asteptare incarcare fisier date_live.txt in streamlit] | [Start aplicație] | [Fisier incarcat] |
| `INPUT_VALIDATION` | [Verificare integritate fisier] | [Fisier primit] | [Valid] |
| `PREPROCESS` | [incarcare scaler.pk1] | [Date validate] | [Tensor format (1,60,132)] |
| `INFERENCE` | [Rulare model LSTM] | [tensor pregatit] | [Probabilitate] |
| `DECISION` | [Comparare probabilitate cu pragul de 0.5] | [Scor disponibil] | [Clasa decisa] |
| `OUTPUT/ALERT` | [Afisare verdict] | [Decizie luata] | [asteptare input nou] |
| `ERROR` | [Afisare mesaj eroare] | [Excepție detectată] | [Revenire la IDLE] |

**Justificare alegere arhitectură State Machine:**

Am ales arhitectura care respecta constrangerile LSTM, care necesita un input cu dimensiune temporala fixa. Starea critica inainte de preprocesare elimina riscul de runtime crash. Separarea logica a starii de decision si inference permite ajustarea pragului de sensibilitate.


## 5. Modelul RN – Antrenare și Optimizare

### 5.1 Arhitectura Rețelei Neuronale

Input (shape: [None, 60, 132]) 
  → LSTM(50 units, return_sequences=True, activation='tanh') 
  → Dropout(0.2)
  → LSTM(50 units, return_sequences=False, activation='tanh') 
  → Dropout(0.2)
  → Dense(1, activation='sigmoid')
Output: 1 clasă (Probabilitate Defect: 0.0 - 1.0)

**Justificare alegere arhitectură:**

Am ales arhitectura LSTM pentru ca este cea mai potrivita pentru analiza seriilor de timp. Avand capacitatea de a retinere a contextului temporal. Am respins CNN-urile 1D deoarece nu capteaza starile anterioare ale retelei.

### 5.2 Hiperparametri Finali (Model Optimizat - Etapa 6)

| Hiperparametru | Valoare Finală | Justificare Alegere |
|----------------|----------------|---------------------|
| Learning Rate | [0.001] | [Valoare standard pentru optimizatorul Adam] |
| Batch Size | [32] | [Balans optim intre viteza si stabilire gradient] |
| Epochs | [20] | [early stopping opreste antrenarea in jurul epocii 8 contra overfitting] |
| Optimizer | [Adam] | [Algoritm adaptiv] |
| Loss Function | [Binary Crossentropy] | [Iesire binara] |
| Regularizare | [Dropout 0.2] | [inserat dupa fiecare strat pentru a nu memora zgomotul specific datelor] |
| Early Stopping | [patience=3] | [Daca eroarea nu scape timp de 3 epoci antrenare se opreste singura] |

### 5.3 Experimente de Optimizare (minim 4 experimente)

| Exp# | Modificare față de Baseline | Accuracy | F1-Score | Timp Antrenare | Observații |
|------|----------------------------|----------|----------|----------------|------------|
| **Baseline** | Dataset original | [52%] | [0.51] | [5 min] | Modelul nu convergea |
| Exp 1 | [extindere arhitectura 100+ neuroni +Dense] | [54.1%] | [0.53] | [8 min] | [Overfitting] |
| Exp 2 | [regularizare agresiva dropout 0.5] | [53.5%] | [0.52] | [6 min] | [Performanta slaba] |
| Exp 3 | [Data engineering] | [98%] | [0.98] | [6 min] | [Reetichetare] |
| Exp 4 | [batch size 32 + learning rate 0.001 Adam] | [99.1%] | [0.99] | [7 min] | [Stabilitate maxima gradient] |
| **FINAL** | [Conf exp 4 + early stopping] | **[99.2%]** | **[0.99]** | [7 min] | **Modelul folosit în producție** |

**Justificare alegere model final:**

Am selectat configuratia din experimentul 4 (2 straturi LSTM cu dopout 0.2 si optimizer Adam) deoarece a fost cea mai echilibrata intre viteza de inferenta si capacitatea de generalizre. Am ales o arhitectura compacta care mentine latenta mica si acurateatea mare, fara sa depinda de forta bruta computationala.



## 6. Performanță Finală și Analiză Erori

### 6.1 Metrici pe Test Set (Model Optimizat)

| Metric | Valoare | Target Minim | Status |
|--------|---------|--------------|--------|
| **Accuracy** | [99.2%] | ≥70% | [✓] |
| **F1-Score (Macro)** | [0.99] | ≥0.65 | [✓] |
| **Precision (Macro)** | [0.99] | - | - |
| **Recall (Macro)** | [0.99] | - | - |

**Îmbunătățire față de Baseline (Etapa 5):**

| Metric | Etapa 5 (Baseline) | Etapa 6 (Optimizat) | Îmbunătățire |
|--------|-------------------|---------------------|--------------|
| Accuracy | [52%] | [99.2%] | [+47.2%] |
| F1-Score | [0.51] | [0.99] | [+0.48] |



### 6.4 Validare în Context Industrial

**Ce înseamnă rezultatele pentru aplicația reală:**

In domeniul energitic costul unei erori false negative este critic si poate duce la avarierea echipamentelor sensibile. Costul unui verificator uman este neglijabil compoarativ cu costul inlocuirii unui utilaj ars.


## 7. Aplicația Software Finală


### 7.1 Screenshot UI cu Model Optimizat

**Locație:** `docs/screenshots/inference_optimized.png`

Aceast screenshot arata starea idle a aplicatiei web streamlit. Asteapta input-ul operatorului prin componenta file uploader. Sistemul preia date de tip .txt sau .csv pentru a declansa pipeline-ul

### 7.3 Demonstrație Funcțională End-to-End

**Locație dovadă:** `docs/demo/` *(GIF / Video / Secvență screenshots)*

**Fluxul demonstrat:**

| Pas | Acțiune | Rezultat Vizibil |
|-----|---------|------------------|
| 1 | Input | [Incarcare CSV/TXT] |
| 2 | Procesare | [Bara de progres] |
| 3 | Inferență | [Predictie afisata] |
| 4 | Decizie | [Alerta verde/rosie in functie de raspuns] |

**Latență măsurată end-to-end:** [50] ms  
**Data și ora demonstrației:** [11.01.2026, 20:33]

---

## 8. Structura Repository-ului Final

```
proiect-rn-[nume-prenume]/
│
├── README.md                               # ← ACEST FIȘIER (Overview Final Proiect - Pe moodle la Evaluare Finala RN > Upload Livrabil 1 - Proiect RN (Aplicatie Sofware) - trebuie incarcat cu numele: NUME_Prenume_Grupa_README_Proiect_RN.md)
│
├── docs/
│   ├── etapa3_analiza_date.md              # Documentație Etapa 3
│   ├── etapa4_arhitectura_SIA.md           # Documentație Etapa 4
│   ├── etapa5_antrenare_model.md           # Documentație Etapa 5
│   ├── etapa6_optimizare_concluzii.md      # Documentație Etapa 6
│   │
│   ├── state_machine.png                   # Diagrama State Machine inițială
│   ├── state_machine_v2.png                # (opțional) Versiune actualizată Etapa 6
│   ├── confusion_matrix_optimized.png      # Confusion matrix model final
│   │
│   ├── screenshots/
│   │   ├── ui_demo.png                     # Screenshot UI schelet (Etapa 4)
│   │   ├── inference_real.png              # Inferență model antrenat (Etapa 5)
│   │   └── inference_optimized.png         # Inferență model optimizat (Etapa 6)
│   │
│   ├── demo/                               # Demonstrație funcțională end-to-end
│   │   └── demo_end_to_end.gif             # (sau .mp4 / secvență screenshots)
│   │
│   ├── results/                            # Vizualizări finale
│   │   ├── loss_curve.png                  # Grafic loss/val_loss (Etapa 5)
│   │   ├── metrics_evolution.png           # Evoluție metrici (Etapa 6)
│   │   └── learning_curves_final.png       # Curbe învățare finale
│   │
│   └── optimization/                       # Grafice comparative optimizare
│       ├── accuracy_comparison.png         # Comparație accuracy experimente
│       └── f1_comparison.png               # Comparație F1 experimente
│
├── data/
│   ├── README.md                           # Descriere detaliată dataset
│   ├── raw/                                # Date brute originale
│   ├── processed/                          # Date curățate și transformate
│   ├── generated/                          # Date originale (contribuția ≥40%)
│   ├── train/                              # Set antrenare (70%)
│   ├── validation/                         # Set validare (15%)
│   └── test/                               # Set testare (15%)
│
├── src/
│   ├── data_acquisition/                   # MODUL 1: Generare/Achiziție date
│   │   ├── README.md                       # Documentație modul
│   │   ├── generate.py                     # Script generare date originale
│   │   └── [alte scripturi achiziție]
│   │
│   ├── preprocessing/                      # Preprocesare date (Etapa 3+)
│   │   ├── data_cleaner.py                 # Curățare date
│   │   ├── feature_engineering.py          # Extragere/transformare features
│   │   ├── data_splitter.py                # Împărțire train/val/test
│   │   └── combine_datasets.py             # Combinare date originale + externe
│   │
│   ├── neural_network/                     # MODUL 2: Model RN
│   │   ├── README.md                       # Documentație arhitectură RN
│   │   ├── model.py                        # Definire arhitectură (Etapa 4)
│   │   ├── train.py                        # Script antrenare (Etapa 5)
│   │   ├── evaluate.py                     # Script evaluare metrici (Etapa 5)
│   │   ├── optimize.py                     # Script experimente optimizare (Etapa 6)
│   │   └── visualize.py                    # Generare grafice și vizualizări
│   │
│   └── app/                                # MODUL 3: UI/Web Service
│       ├── README.md                       # Instrucțiuni lansare aplicație
│       └── main.py                         # Aplicație principală
│
├── models/
│   ├── untrained_model.h5                  # Model schelet neantrenat (Etapa 4)
│   ├── trained_model.h5                    # Model antrenat baseline (Etapa 5)
│   ├── optimized_model.h5                  # Model FINAL optimizat (Etapa 6) ← FOLOSIT
│   └── final_model.onnx                    # (opțional) Export ONNX pentru deployment
│
├── results/
│   ├── training_history.csv                # Istoric antrenare - toate epocile (Etapa 5)
│   ├── test_metrics.json                   # Metrici baseline test set (Etapa 5)
│   ├── optimization_experiments.csv        # Toate experimentele optimizare (Etapa 6)
│   ├── final_metrics.json                  # Metrici finale model optimizat (Etapa 6)
│   └── error_analysis.json                 # Analiza detaliată erori (Etapa 6)
│
├── config/
│   ├── preprocessing_params.pkl            # Parametri preprocesare salvați (Etapa 3)
│   └── optimized_config.yaml               # Configurație finală model (Etapa 6)
│
├── requirements.txt                        # Dependențe Python (actualizat la fiecare etapă)
└── .gitignore                              # Fișiere excluse din versionare
```

### Legendă Progresie pe Etape

| Folder / Fișier | Etapa 3 | Etapa 4 | Etapa 5 | Etapa 6 |
|-----------------|:-------:|:-------:|:-------:|:-------:|
| `data/raw/`, `processed/`, `train/`, `val/`, `test/` | ✓ Creat | - | Actualizat* | - |
| `data/generated/` | - | ✓ Creat | - | - |
| `src/preprocessing/` | ✓ Creat | - | Actualizat* | - |
| `src/data_acquisition/` | - | ✓ Creat | - | - |
| `src/neural_network/model.py` | - | ✓ Creat | - | - |
| `src/neural_network/train.py`, `evaluate.py` | - | - | ✓ Creat | - |
| `src/neural_network/optimize.py`, `visualize.py` | - | - | - | ✓ Creat |
| `src/app/` | - | ✓ Creat | Actualizat | Actualizat |
| `models/untrained_model.*` | - | ✓ Creat | - | - |
| `models/trained_model.*` | - | - | ✓ Creat | - |
| `models/optimized_model.*` | - | - | - | ✓ Creat |
| `docs/state_machine.*` | - | ✓ Creat | - | (v2 opțional) |
| `docs/etapa3_analiza_date.md` | ✓ Creat | - | - | - |
| `docs/etapa4_arhitectura_SIA.md` | - | ✓ Creat | - | - |
| `docs/etapa5_antrenare_model.md` | - | - | ✓ Creat | - |
| `docs/etapa6_optimizare_concluzii.md` | - | - | - | ✓ Creat |
| `docs/confusion_matrix_optimized.png` | - | - | - | ✓ Creat |
| `docs/screenshots/` | - | ✓ Creat | Actualizat | Actualizat |
| `results/training_history.csv` | - | - | ✓ Creat | - |
| `results/optimization_experiments.csv` | - | - | - | ✓ Creat |
| `results/final_metrics.json` | - | - | - | ✓ Creat |
| **README.md** (acest fișier) | Draft | Actualizat | Actualizat | **FINAL** |

*\* Actualizat dacă s-au adăugat date noi în Etapa 4*

### Convenție Tag-uri Git

| Tag | Etapa | Commit Message Recomandat |
|-----|-------|---------------------------|
| `v0.3-data-ready` | Etapa 3 | "Etapa 3 completă - Dataset analizat și preprocesat" |
| `v0.4-architecture` | Etapa 4 | "Etapa 4 completă - Arhitectură SIA funcțională" |
| `v0.5-model-trained` | Etapa 5 | "Etapa 5 completă - Accuracy=X.XX, F1=X.XX" |
| `v0.6-optimized-final` | Etapa 6 | "Etapa 6 completă - Accuracy=X.XX, F1=X.XX (optimizat)" |

---

## 9. Instrucțiuni de Instalare și Rulare

### 9.1 Cerințe Preliminare

```
Python >= 3.8 (recomandat 3.10+)
pip >= 21.0
[sau LabVIEW >= 2020 pentru proiecte LabVIEW]
```

### 9.2 Instalare

```bash
# 1. Clonare repository
git clone [URL_REPOSITORY]
cd proiect-rn-[nume-prenume]

# 2. Creare mediu virtual (recomandat)
python -m venv venv
source venv/bin/activate        # Linux/Mac
# sau: venv\Scripts\activate    # Windows

# 3. Instalare dependențe
pip install -r requirements.txt
```

### 9.3 Rulare Pipeline Complet

```bash
# Pasul 1: Preprocesare date (dacă rulați de la zero)
python src/preprocessing/data_cleaner.py
python src/preprocessing/data_splitter.py --stratify --random_state 42

# Pasul 2: Antrenare model (pentru reproducere rezultate)
python src/neural_network/train.py --config config/optimized_config.yaml

# Pasul 3: Evaluare model pe test set
python src/neural_network/evaluate.py --model models/optimized_model.h5

# Pasul 4: Lansare aplicație UI
streamlit run src/app/main.py
# sau: python src/app/main.py (pentru Flask/FastAPI)
# sau: [instrucțiuni LabVIEW dacă aplicabil]
```

### 9.4 Verificare Rapidă 

```bash
# Verificare că modelul se încarcă corect
python -c "from src.neural_network.model import load_model; m = load_model('models/optimized_model.h5'); print('✓ Model încărcat cu succes')"

# Verificare inferență pe un exemplu
python src/neural_network/evaluate.py --model models/optimized_model.h5 --quick-test
```




## 10. Concluzii și Discuții

### 10.1 Evaluare Performanță vs Obiective Inițiale

| Obiectiv Definit (Secțiunea 2) | Target | Realizat | Status |
|--------------------------------|--------|----------|--------|
| [Detectarea Defectelor (siguranta)] | [recall > 95%] | [realizat] | [✓] |
| [Reactie in timp real] | [latenta< 50ms] | [realizat] | [✓] |
| Accuracy pe test set | ≥70% | [99.2%] | [✓] |
| F1-Score pe test set | ≥0.65 | [0.99] | [✓] |
| [Reducere alarme false] | [>90%] | [98.9] | [✓] |

### 10.2 Ce NU Funcționează – Limitări Cunoscute


1. **Limitare 1:** [Diferenta intre simulare si realitate. Modelul nu este complet validat. Exista riscul scaderii acuratetei in medii cu interferente extreme]
2. **Limitare 2:** [Granularitate. Modelul ofera o decizie binara dar nu distinge intre tipurile de defectiuni.]
3. **Limitare 3:** [LSTM creeaza un blind spot la pornire pana cand fereastra sliding window se completeaza]
4. **Funcționalități planificate dar neimplementate:** [Deployment pe hardware embedded, integrare protocol industrial pentru a nu citi din fisiere txt]

### 10.3 Lecții Învățate (Top 5)

1. **[Lecție 1]:** [Etichetarea corecta a datelor este importanta. ]
2. **[Lecție 2]:** [Physics informed ai ajuta reteaua sa nu ghiceasca aproape de 50/50]
3. **[Lecție 3]:** [early stopping a salvat modelul de la overfitting]
4. **[Lecție 4]:** [lstm are nevoie de validare altfel aplicatie va da crash]
5. **[Lecție 5]:** [recallul este mai important decat acuratetea. Este mult mai grav sa ratezi un defect decat o alarma falsa]

### 10.4 Retrospectivă

**Ce ați schimba dacă ați reîncepe proiectul?**

As adopta o abordare bazata pe data engineering din prima zi. As documenta mai bine procesul cu videoclipuri, screenshoturi si tabele standardizate inca de la inceput. As proiecta o arhitectura de clasificare non binara pentru a capta mai multa informatie.


11. Bibliografie

    Hochreiter, S., & Schmidhuber, J., Long Short-Term Memory, 1997. Neural Computation, 9(8), 1735–1780. DOI: https://doi.org/10.1162/neco.1997.9.8.1735 (Lucrarea fundamentală care a introdus rețelele LSTM)

    TensorFlow Core, Recurrent Neural Networks (RNN) with Keras, 2024. URL: https://www.tensorflow.org/guide/keras/rnn (Documentația oficială utilizată pentru implementarea straturilor LSTM)

    Streamlit Inc., Streamlit Documentation: Build and deploy data apps, 2024. URL: https://docs.streamlit.io/ (Sursa pentru dezvoltarea interfeței grafice și a logicii de sesiune)

    Harris, C.R., et al., Array programming with NumPy, 2020. Nature 585, 357–362. DOI: https://doi.org/10.1038/s41586-020-2649-2 (Referință pentru generarea numerică a semnalelor și calculul FFT)

    Hossain, E., et al., A Comprehensive Review on Smart Grid: Operation, Architecture and Protection, 2019. IEEE Access. DOI: https://doi.org/10.1109/ACCESS.2019.2891704 (Contextul industrial pentru detecția defectelor în rețele inteligente)

## 12. Checklist Final (Auto-verificare înainte de predare)

### Cerințe Tehnice Obligatorii

- [✓] **Accuracy ≥70%** pe test set (verificat în `results/final_metrics.json`)
- [✓] **F1-Score ≥0.65** pe test set
- [✓] **Contribuție ≥40% date originale** (verificabil în `data/generated/`)
- [✓] **Model antrenat de la zero** (NU pre-trained fine-tuning)
- [✓] **Minimum 4 experimente** de optimizare documentate (tabel în Secțiunea 5.3)
- [✓] **Confusion matrix** generată și interpretată (Secțiunea 6.2)
- [✓] **State Machine** definit cu minimum 4-6 stări (Secțiunea 4.2)
- [✓] **Cele 3 module funcționale:** Data Logging, RN, UI (Secțiunea 4.1)
- [] **Demonstrație end-to-end** disponibilă în `docs/demo/`

### Repository și Documentație

- [✓] **README.md** complet (toate secțiunile completate cu date reale)
- [✓] **4 README-uri etape** prezente în `docs/` (etapa3, etapa4, etapa5, etapa6)
- [✓] **Screenshots** prezente în `docs/screenshots/`
- [ ] **Structura repository** conformă cu Secțiunea 8
- [ ] **requirements.txt** actualizat și funcțional
- [✓] **Cod comentat** (minim 15% linii comentarii relevante)
- [✓] **Toate path-urile relative** (nu absolute: `/Users/...` sau `C:\...`)

### Acces și Versionare

- [✓] **Repository accesibil** cadrelor didactice RN (public sau privat cu acces)
- [ ] **Tag `v0.6-optimized-final`** creat și pushed
- [✓] **Commit-uri incrementale** vizibile în `git log` (nu 1 commit gigantic)
- [✓] **Fișiere mari** (>100MB) excluse sau în `.gitignore`

### Verificare Anti-Plagiat

- [✓] Model antrenat **de la zero** (weights inițializate random, nu descărcate)
- [✓] **Minimum 40% date originale** (nu doar subset din dataset public)
- [✓] Cod propriu sau clar atribuit (surse citate în Bibliografie)

---

## Note Finale

**Versiune document:** FINAL pentru examen  
**Ultima actualizare:** [11.02.2026]  
**Tag Git:** `v0.6-optimized-final`

---

*Acest README servește ca documentație principală pentru Livrabilul 1 (Aplicație RN). Pentru Livrabilul 2 (Prezentare PowerPoint), consultați structura din RN_Specificatii_proiect.pdf.*
