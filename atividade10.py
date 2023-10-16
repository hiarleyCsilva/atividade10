# Exercício Python 10: faça um algoritimo que receba a velocidade em Km/h de um veiculo e:
# se maior que 60km/h aplicar multa de 7 vezes a da velocidade permitidave
vel = float(input("Digite a velocidade do veículo em Km/h: "))

limite_velocidade = 60  # Velocidade permitida

if vel> limite_velocidade:
    multa = (vel - limite_velocidade) * 7
    print(f"Velocidade acima do limite! Multa a ser aplicada: R${multa:.2f}")
else:
    print("Velocidade dentro do limite permitido.")
