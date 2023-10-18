# Exercício Python 10: faça um algoritimo que receba a velocidade em Km/h de um veiculo e:
# se maior que 60km/h aplicar multa de 7 vezes a da velocidade permitida

print("velocimetro")
velocidade = float(input("insira a velocidade em km/h:"))
if velocidade > 60:
    print(f"voce ultrapassou a velocidade permitida de 60 km/h voce recebeu uma multa de R$:{velocidade*7} ")
else:
    print("velocidade dentro dos limites de velocidade")