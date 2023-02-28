# pedir para o usuário informar um número
num = int(input("Digite um número: "))

# inicializa os dois valores iniciais da sequência
fibo_ant = 0
fibo_atual = 1

# verificar se o número informado pertence à sequência
while fibo_atual < num:
    #imprimi os dois primeiros valores
    if(fibo_ant==0):
        print(f"O sequencia gerada: {fibo_ant} {fibo_atual}",end=" ")
    # calcula o próximo valor da sequência
    fibo_prox = fibo_ant + fibo_atual
    # atualiza os valores dos antecessores
    fibo_ant = fibo_atual
    fibo_atual = fibo_prox
    print(f"{fibo_atual}",end=" ")

# verificar se o número informado pertence à sequência
if fibo_atual == num:
    print(f"\nO número {num} pertence à sequência de Fibonacci!")
else:
    print(f"\nO número {num} não pertence à sequência de Fibonacci!")