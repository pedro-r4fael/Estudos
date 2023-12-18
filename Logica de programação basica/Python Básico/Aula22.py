
velocidade = 62 # velocidade atual do carro

local_carro = 102 # local em que o carro esta na estrada

#constante não tem problema ser em Maiusculo, nao atribui outros valores

RADAR_1 = 60 # velodicade maxima do radar
LOCAL_1 = 100 # local ondo o radar 1 esta
RADAR_RANGE = 1 # distancia onde o radar pega


velocidade_carro_passou_radar_1 = velocidade > RADAR_1

multar_carro_radar_1 = LOCAL_1 + RADAR_RANGE



if velocidade_carro_passou_radar_1 :
    print("Carro passou do limite de velocidade do radar 1")

if local_carro >= (multar_carro_radar_1) and \
        local_carro <= (multar_carro_radar_1) and\
        velocidade_carro_passou_radar_1:
    print("carro multado em radar 1")




