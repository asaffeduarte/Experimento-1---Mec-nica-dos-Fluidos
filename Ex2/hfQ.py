import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress

# Dados fornecidos
h = np.array([3.43728728173582, 2.942525293973975, 2.7616376321660314, 2.6416742843186347, 2.251768597497837])
Q_m3s = np.array([0.000005323193916, 0.000004748603352, 0.000004678362573, 0.000004260299625, 0.000003284541235])
incerteza_Q_m3s = np.array([0.0000000507150389, 0.00000005588166624, 0.0000000584955293, 0.00000004682709977, 0.00000007141269858])

# Convertendo vazão de m³/s para cm³/s
Q_cm3s = Q_m3s * 1e6
incerteza_Q_cm3s = incerteza_Q_m3s * 1e6

# Regressão linear dos dados
slope, intercept, r_value, p_value, std_err = linregress(Q_cm3s, h)

# Linha ajustada
Q_fit = np.linspace(np.min(Q_cm3s), np.max(Q_cm3s), 100)
h_fit = slope * Q_fit + intercept

# Plotando h_f vs Q
plt.figure(figsize=(10, 6))
plt.errorbar(Q_cm3s, h, xerr=incerteza_Q_cm3s, fmt='o', label='Dados experimentais', capsize=5)
plt.plot(Q_fit, h_fit, '-', label=f'Ajuste linear: h_f = {slope:.4f} Q + {intercept:.4f} (R² = {r_value**2:.4f})')
plt.xlabel('Vazão (Q) [cm³/s]')
plt.ylabel('Perda de carga (h_f) [cm]')
plt.title('Perda de carga (h_f) vs Vazão (Q) no escoamento laminar')
plt.grid(True)
plt.legend()
plt.show()

# Imprimindo os resultados da regressão linear
print(f"Slope (inclinação): {slope:.5e}")
print(f"Intercept (intercepto): {intercept:.5f}")
print(f"R-squared (R²): {r_value**2:.5f}")
