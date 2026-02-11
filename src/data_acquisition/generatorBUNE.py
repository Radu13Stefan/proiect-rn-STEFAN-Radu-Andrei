import numpy as np
import random

def genereaza_date(tip='bune', filename='date_live.txt'):
    lines = []
    
    print(f"Generare date EXTREME de tip: {tip.upper()}...")

    for _ in range(70):
        
        if tip == 'bune':
            # Valori ideale, fără nicio variație (linie dreaptă)
            voltage = 230.0       # Tensiune perfectă
            current = 10.0        # Curent mic și stabil
            power = 2.3           # P = U*I
            freq = 50.0           # Frecvență fixă
            
           
            fft_values = [0.001] * 128 
            
        else: 
            # Valori care indică o avarie gravă
            voltage = 150.0       # Cădere masivă de tensiune (Brownout)
            current = 100.0       # Curent uriaș (Scurtcircuit)
            power = 15.0          # Putere foarte mare
            freq = 45.0           # Frecvență complet greșită
            
           
            fft_values = [random.uniform(10.0, 50.0) for _ in range(128)]

        row = [voltage, current, power, freq] + fft_values
        row_str = ",".join(map(str, row))
        lines.append(row_str)

    with open(filename, 'w') as f:
        f.write('\n'.join(lines))
    
    print(f" Gata! Datele în {filename} sunt acum foarte clare.")

if __name__ == "__main__":
    genereaza_date('bune')