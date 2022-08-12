def get_quantidade_moedas(moeda: int, nome_unidade: str) -> str:
    texto: str = ""
    quantidade: int = 0
    global valor_inicial
    if valor_inicial < moeda:
        texto = " "
    while valor_inicial >= moeda:
        valor_inicial -= moeda
        quantidade += 1
        texto = f"\n{quantidade} {nome_unidade}"
    return texto


entrada_certa: bool = False
print("Bem vindo ao programa de converter moedas")
while not entrada_certa:
    valor_inicial = input("Digite um valor: ")
    try:
        valor_inicial = float(valor_inicial)
        valor_inicial *= 100
        valor_inicial = int(valor_inicial)
        if valor_inicial < 5:
            print("valor muito baixo, digite no mínimo 5 centavos")
        else:
            entrada_certa = True
    except ValueError:
        print("valor inválido, digite apenas numeros")

cedulas: list[int] = [10000, 5000, 2000, 1000, 500, 200, 100, 50, 25, 10, 5]
nomes_cedulas: list[str] = [
   "cédulas de 100 reais",
   "cédulas de 50 reais",
   "cédulas de 20 reais",
   "cédulas de 10 reais",
   "cédulas de 5 reais",
   "cédulas de 2 reais",
   "moedas de 1 real",
   "moedas de 50 centavos",
   "moedas de 25 centavos",
   "moedas de 10 centavos",
   "moedas de 5 centavos",
]

print(f"Valor total a ser retirado: {float(valor_inicial)/100 :.2f} reais", end="")
for i in range(len(cedulas)):
    print(get_quantidade_moedas(cedulas[i], nomes_cedulas[i]), end="")

# valor que mostra todas as cédulas: 188.90