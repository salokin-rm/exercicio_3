"""
Programa: Ler, Somar e Imprimir Números
Descrição: Este programa lê 2 números quaisquer, soma e imprime na tela o resultado.
Autor: Nikolas Martins
Data: 21/06/2023
Versão: 0.0.1
"""

# Atribuição de variáveis

variavel = []
tamanho = [0, 0]
x=0
soma = 0

# Entrada de dados

print("Digite 2 numeros separados por enter: ")

# Processamento de dados

for y in range(len(tamanho)):
    x=x+1
    coringa = float(input(f"{x}º numero: ")) #variável transição
    variavel.append(coringa)
    soma = soma + variavel[y]
    if x==2:
        break
        
# Saída de dados
   
if len(variavel)==2:
    print("Números digitados:",variavel,".\nSoma dos números = ",soma,".")