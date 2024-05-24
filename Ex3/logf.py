import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress
from matplotlib.ticker import ScalarFormatter

# Dados fornecidos
f = np.array([0.0682765309, 0.0734494596, 0.0710197483, 0.0819217404, 0.1174828601])
incerteza_f = np.array([0.002392547, 0.002766637, 0.002741598, 0.003007908, 0.006167283])
Re = np.array([1091, 974, 959, 874, 673])
incerteza_Re = np.array([20, 19, 19, 17, 18])

# Transformação logarítmica (base 10)
log_f = np.log10(f)
log_Re = np.log10(Re)

# Regressão linear nos dados transformados
slope, intercept, r_value, p_value, std_err = linregress(log_Re, log_f)

# Constantes A e C
A = slope
log_C = intercept
C = 10**log_C

# Linha ajustada
log_Re_fit = np.linspace(np.min(log_Re), np.max(log_Re), 100)
log_f_fit = A * log_Re_fit + log_C

# Plotando f vs Re em escala bilogarítmica
plt.figure(figsize=(10, 6))
plt.errorbar(log_Re, log_f, xerr=incerteza_Re / Re / np.log(10), yerr=incerteza_f / f / np.log(10), fmt='o', label='Dados experimentais', capsize=5)
plt.plot(log_Re_fit, log_f_fit, '-', label=f'Ajuste linear: log f = {A:.4f} x + {log_C:.4f} (R² = {r_value**2:.4f})')

# Configurando os eixos em escala logarítmica e formato decimal
plt.gca().xaxis.set_major_formatter(ScalarFormatter())
plt.gca().ticklabel_format(axis='x', style='plain')
plt.xlabel('log(Re)')
plt.ylabel('log(f)')
plt.title('Coeficiente de perda de carga (f) vs Número de Reynolds (Re) em escala log-log')
plt.grid(True, which="both", ls="--")
plt.legend()
plt.text(0.1, 0.1, f'A = {A:.4f}\nC = {C:.4f}', transform=plt.gca().transAxes, fontsize=12, bbox=dict(facecolor='white', alpha=0.5))

plt.show()
