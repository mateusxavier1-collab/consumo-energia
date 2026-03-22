# Entrada de dados
aparelho = input("Digite o nome do aparelho: ")
potencia = float(input("Digite a potência (em watts): "))
horas_dia = float(input("Digite as horas de uso por dia: "))
consumo_mensal = (potencia * horas_dia * 30) / 1000
valor_kwh = 0.75
custo = consumo_mensal * valor_kwh
print("\n--- Resultado ---")
print(f"Aparelho: {aparelho}")
print(f"Consumo estimado: {consumo_mensal:.2f} kWh/mês")
print(f"Custo estimado: R$ {custo:.2f}")

