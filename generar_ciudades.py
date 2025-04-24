import random  # Aseguramos que el módulo random esté importado
from ciudad import Ciudad

def generar_ciudades():
    nombres_ciudades = [
        'Madrid', 'Barcelona', 'Valencia', 'Sevilla', 'Zaragoza',
        'Málaga', 'Murcia', 'Palma', 'Bilbao', 'Alicante'
    ]

    ciudades = []  # Aseguramos que la variable se llama "ciudades"
    for nombre in nombres_ciudades:
        temperatura_maxima = random.randint(20, 35)  # 20°C - 35°C
        temperatura_minima = random.randint(10, 20)  # 10°C - 20°C
        llueve = random.random() < 0.3  # 30% de probabilidad de lluvia
        estado_cielo = 'soleado' if random.random() < 0.5 else 'nublado'

        ciudad = Ciudad(nombre, temperatura_maxima, temperatura_minima, llueve, estado_cielo)
        ciudades.append(ciudad)

    return ciudades
