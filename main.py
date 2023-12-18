pi = 3.14159
raio_da_orbita = 1496e8 #Distância média da terra em Km (1496^8)
periodo = 3156e7 #Duração de um ano em segundos (3156^7)

print("Hello Universe!")
print("Vamos calcular a velocidade que a terra se move ao longo de sua órbita ao redor do sol")

velocidade = (2 * pi * raio_da_orbita) / periodo

print("Velocidade da órbita = {:5.2f} km/s".format(velocidade))