import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

# ================================
# Función equivalente a ES_nuevo
# ================================
def ES_nuevo(t, p):
    # Parámetros físicos
    g = 9.81     # gravedad (m/s^2)
    m = 1.5      # masa (kg)
    l = 0.3      # longitud del péndulo (m)
    gamma = 90   # valor gamma

    # Coeficientes auxiliares
    a = 1 / gamma**2
    b = 1 / (4 * (l**4) * (m**2))
    c = a - b
    h = g / l

    # Sistema de ecuaciones diferenciales
    dp1 = (2 * h * p[1]) - (c * p[1]**2) - (a * p[0]**2) - 2
    dp2 = (h * p[2]) - p[0] - (a * p[0] * p[1]) - (c * p[1] * p[2])
    dp3 = -2 * p[1] - (c * p[2]**2) - (a * p[1]**2) - (2 * 0.1 * m * l)

    return [dp1, dp2, dp3]

# ================================
# Simulación (equivalente a ESRUN_nuevo)
# ================================
# Condiciones iniciales
p0 = [-250, 0.0001, -16]  # [P11, P12, P22]

# Intervalo de tiempo de la simulación
t_inicio = 0
t_fin = 10
t_eval = np.linspace(t_inicio, t_fin, 1000)

# Resolver usando método RK45 (similar a ode45)
sol = solve_ivp(
    ES_nuevo,
    (t_inicio, t_fin),
    p0,
    method='RK45',
    t_eval=t_eval,
    rtol=1e-2,
    max_step=1e-3
)

# ================================
# Gráfica de resultados
# ================================
plt.figure(figsize=(10, 6))
plt.plot(sol.t, sol.y[0], label='P11')
plt.plot(sol.t, sol.y[1], label='P12')
plt.plot(sol.t, sol.y[2], label='P22')
plt.xlabel('Tiempo [s]')
plt.ylabel('P_i')
plt.title('Evolución de P11, P12, P22 en el tiempo')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
