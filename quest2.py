def esta_fibonacci(n):
    a, b = 0, 1 # inicia a sequência sendo os 2 primeiros números 0 e 1
    while a <= n: # verifica se o número esquerdo é menor ou igual a n (o número esquerdo sempre está na sequência)
        if a == n: # se o número esquerdo for igual ao informado no parâmetro, o informado está na sequência
            return True # retorna True, informando que o número pertence à sequência
        a, b = b, a + b # o valor a direita passa a ser o da esquerda e o da direita é a lógica de fibonacci onde o novo numero na sequência é a soma dos seus 2 anteriores

    return False

print(f'O número {4} está na sequência de fibonacci: {esta_fibonacci(4)}') # teste com o número 4
print(f'O número {21} está na sequência de fibonacci: {esta_fibonacci(21)}') # teste com o número 21
print(f'O número {2584} está na sequência de fibonacci: {esta_fibonacci(2584)}') # teste com o número 2584