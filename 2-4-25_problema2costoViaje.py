# Calcular el costo de un viaje en carro

varDistancia = int(input("¿Cual sera las distancia del viaje en km?"))
varConsumo = int(
    input("¿Cuantos litros de gasolina consume el carro por kilometro?"))
varGasolina = int(input("¿Cual es el precio de la gasolina por litro?"))
varCosto = (varDistancia*varConsumo)*varGasolina

print("El costo del viaje sera", varCosto, "$")
