import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress

# Dados fornecidos
posicao = np.array([0, 1.228, 2.432, 3.632])  # Posições dos piezômetros ao longo do tubo
piezometros = np.array([0.4690, 0.4600, 0.4540, 0.4460])  # Elevação em metros que define a linha piezométrica
incerteza_piezometros = 0.0005
velocidade = 0.08509174185  # Velocidade em m/s
incerteza_velocidade = 0.0022127404216  # Incerteza na velocidade em m/s
gamma = 9786.41  # Peso específico da água em N/m³
incerteza_pesoespecifico = 0.01
alpha = 2  # Coeficiente de correção de energia cinética
g = 9.78641  # Aceleração da gravidade em m/s²
incerteza_g = 0.00001
energia_cinetica = 0.0007398631909
incerteza_energia_cinetica = 0.00003847906163

# Linha piezométrica (LP)
LP = piezometros
incerteza_LP = incerteza_piezometros

# Termo de energia cinética
term_cinetico = alpha * (velocidade**2) / (2 * g)

# Linha de energia (LE)
LE = term_cinetico + LP
incerteza_LE = np.sqrt(incerteza_energia_cinetica**2 + incerteza_LP**2)

# Ajuste linear para a linha piezométrica
slope, intercept, r_value, p_value, std_err = linregress(posicao, LP)

# Ajuste linear para a linha de energia
slope_LE, intercept_LE, r_value_LE, p_value_LE, std_err_LE = linregress(posicao, LE)

# Equação da reta média para LP
LP_fit = slope * posicao + intercept

# Equação da reta média para LE
LE_fit = slope_LE * posicao + intercept_LE

perda_carga_distribuida = (posicao[3] - posicao[0]) * (-slope)

# Gráficos
plt.figure(figsize=(10, 6))

# Gráfico da linha piezométrica
plt.errorbar(posicao, LP, yerr=incerteza_LP, fmt='o', label='Linha Piezométrica (LP)')
plt.plot(posicao, LP_fit, label=f'Reta média LP: y = {slope:.5f}x + {intercept:.5f} (R² = {r_value**2:.5f})')

# Gráfico da linha de energia
plt.errorbar(posicao, LE, yerr=incerteza_LE, fmt='o', label='Linha de Energia (LE)', color='r')
plt.plot(posicao, LE_fit, label=f'Reta média LE: y = {slope_LE:.5f}x + {intercept_LE:.5f} (R² = {r_value_LE**2:.5f})', color='r')

plt.annotate(f'Perda de carga distribuída: {perda_carga_distribuida:.5f} m', xy=(0.5, 0.9), xycoords='axes fraction', fontsize=12, color='b')
print(perda_carga_distribuida)
# Configurações do gráfico
plt.xlabel('Posição (m)')
plt.ylabel('Altura do piezômetro em relação ao PHR (m)')
plt.title('Linha Piezométrica (LP) e Linha de Energia (LE) para Vazão 5')
plt.legend()
plt.grid(True)
plt.show()
