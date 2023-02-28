# Solicitando uma string ao usuario
frase = input("Digite uma frase: ")

# Inicializando uma string para armazenar a string invertida
frase_inv = ""

# loop for para iterar sobre os caracteres da string original
for i in range(len(frase)-1, -1, -1):
    # adicionando o caractere atual da string inicial a string invertida
    frase_inv += frase[i]

# imprimindo a string digitado pelo usuario e a string invertida
print(f"Frase Original: {frase}")
print(f"Frase Invertida: {frase_inv}")