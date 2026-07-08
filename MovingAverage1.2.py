import numpy as np
import matplotlib.pyplot as plt

#DATOS INVENTADOS COMO EN SAV GOL

np.random.seed(0)

# Eje x
x = np.linspace(-50, 50, 201)

# Señal real
signal = 0.01*x**2 + 2*np.sin(x/5)

# Ruido aleatorio igual que el de Sav Gol
noise = np.random.normal(0, 2, len(x))

# Señal con ruido
y = signal + noise


# Metodo de moving average a partir de aqui


window_size = 15

# Mitad de ventana
half_window = window_size // 2

# Lista vacía
moving_average = []

# Recorrer toda la señal
for i in range(len(y)):

    suma = 0
    contador = 0

    # Ventana centrada
    for k in range(i - half_window,
                   i + half_window + 1):

        # Evitar índices fuera del arreglo
        if 0 <= k < len(y):

            suma += y[k]
            contador += 1

    promedio = suma / contador

    moving_average.append(promedio)

# Convertir a array para operaciones matematicas
moving_average = np.array(moving_average)


# GRAFICA

plt.figure(figsize=(10,5))

plt.plot(x,
         y,
         label='Original Signal')

plt.plot(x,
         moving_average,
         linewidth=2,
         label='Centered Moving Average')

plt.xlabel('Wavelength / Sample')
plt.ylabel('Intensity')

plt.title('NIR Signal Smoothing')

plt.legend()
plt.grid(True)

plt.show()