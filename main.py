#Bloco Dicionario/Lista
startup = {
    "nome":"CyberPulse Tech",
    "segmento":"Segurança da Informação",
    "ano_adesao":2026
}
solucoes_ativas = ["Firewall IA", "Scan de Vulnerabilidades"]
print("STARTUP===📊",startup["nome"],"===")
print("SEGMENTO===",startup["segmento"],"===")
print("PRODUTO===",solucoes_ativas[0])

#Bloco Matriz
bancadas = [
    ["Bancada N1 (1)","Bancada N2 (0)"],
    ["Bancada S1 (0)", "Bancada S2 (1)"]
]
print("A seguir teremos a ocupação atual da bancadas sendo:\n 1:Ocupado\n 0:livre")
print(bancadas[0][0])
print(bancadas[0][1])
print(bancadas[1][0]) 
print(bancadas[1][1])

with open("custos_cloud.csv", "r", encoding="utf-8") as arquivo:
    linha_cabecalho = arquivo.readline()
    linha1 = arquivo.readline()
    linha2 = arquivo.readline()
    linha3 = arquivo.readline()
    linha4 = arquivo.readline()

print(linha_cabecalho)
print(linha1)
print(linha2)
print(linha3)
print(linha4)
#Etapa 4----

nome_startup = startup["nome"]
bancada_alocada = "Bancada N1"
custo1 = float(linha1.split(",")[1].strip())
custo2 = float(linha2.split(",")[1].strip())
custo3 = float(linha3.split(",")[1].strip())
custo4 = float(linha4.split(",")[1].strip())
valor_total = custo1 + custo2 + custo3 + custo4

print("\n=== PAINEL DE CONSOLIDAÇÃO ===")
print(f"Startup: {nome_startup}")
print(f"Bancada alocada: {bancada_alocada}")
print(f"Custo total de infraestrutura Cloud: R$ {valor_total:.2f}")