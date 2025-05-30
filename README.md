
# Simulación Numérica de Ecuaciones Diferenciales para un Sistema de Péndulo

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)  
![NumPy](https://img.shields.io/badge/NumPy-NumPy-informational)  
![SciPy](https://img.shields.io/badge/SciPy-ODE-green)  
![Matplotlib](https://img.shields.io/badge/Matplotlib-Plotting-orange)  

---

## Descripción

Este script realiza la simulación numérica de un sistema de ecuaciones diferenciales ordinarias (ODEs) que modelan la evolución de parámetros asociados a un sistema tipo péndulo. Utiliza el método de integración `RK45` de SciPy (similar a `ode45` de MATLAB) y grafica la evolución temporal de las variables de interés.

---

## Características

- **Modelo físico:** Incluye parámetros de gravedad, masa y longitud del péndulo.  
- **Resolución numérica:** Utiliza `solve_ivp` de SciPy para integrar el sistema de ODEs.  
- **Visualización:** Grafica la evolución de las variables `P11`, `P12` y `P22` a lo largo del tiempo.  
- **Código claro y comentado:** Fácil de adaptar a otros sistemas o condiciones iniciales.  

---

## Requisitos

- Python 3.8 o superior  
- [NumPy](https://numpy.org/)  
- [SciPy](https://scipy.org/)  
- [Matplotlib](https://matplotlib.org/)  

Puedes instalar las dependencias con:

```sh
pip install numpy scipy matplotlib
```

---

## Uso

1. Asegúrate de tener las dependencias instaladas.  
2. Ejecuta el script:

```sh
python test_matlab.py
```

3. Se mostrará una gráfica con la evolución de las variables del sistema.

---

## Estructura del Código

### Definición del sistema de ODEs:
La función `ES_nuevo` implementa el sistema de ecuaciones diferenciales basado en los parámetros físicos del péndulo.

### Simulación:
Se resuelve el sistema usando `solve_ivp` con condiciones iniciales y un intervalo de tiempo definido.

### Visualización:
Se grafican las variables `P11`, `P12` y `P22` en función del tiempo.

---

## Archivo `requirements.txt`

```txt
numpy>=1.20.0
scipy>=1.6.0
matplotlib>=3.3.0
```

Puedes usar este archivo con:

```sh
pip install -r requirements.txt
```

---

## Créditos

Desarrollado por [Miguel Angel Enríquez García].  
Contacto: [miguel.egk@gmail.com]
