import tkinter as tk
from generar_ciudades import generar_ciudades

def mostrar_informacion():
    try:
        ciudades = generar_ciudades()
        texto_resultado = ""

        for ciudad in ciudades:
            texto_resultado += f'Ciudad: {ciudad.nombre}\n'
            texto_resultado += f'  Temperatura Máxima: {ciudad.temperatura_maxima}°C\n'
            texto_resultado += f'  Temperatura Mínima: {ciudad.temperatura_minima}°C\n'
            texto_resultado += f'  Llueve: {"Sí" if ciudad.llueve else "No"}\n'
            texto_resultado += f'  Estado del Cielo: {ciudad.estado_cielo}\n'
            texto_resultado += '-----------------------------------\n'

        resultado_label.config(text=texto_resultado)
    except Exception as e:
        resultado_label.config(text=f"Error: {e}")

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Clima en Ciudades Españolas")

# Crear un botón para mostrar la información
boton_mostrar = tk.Button(ventana, text="Mostrar Información", command=mostrar_informacion)
boton_mostrar.pack(pady=10)

# Crear un label para mostrar los resultados
resultado_label = tk.Label(ventana, text="", justify="left", anchor="w")
resultado_label.pack(padx=10, pady=10)

# Iniciar el bucle principal de la ventana
if __name__ == '__main__':
    ventana.mainloop()
