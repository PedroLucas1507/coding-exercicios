total_pares = int(input("Digite o total de pares produzidos: "))

caixas = total_pares // 12   # divisão inteira: caixas completas
sobra = total_pares % 12     # resto: pares que não completam caixa

print(f"Caixas completas: {caixas}")
print(f"Pares sobrando: {sobra}")