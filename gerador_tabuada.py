import time
#importa a biblioteca de tempo

print(f'--- Gerador de tabuada ---')
#vai anunciar no terminal que é um gerador de tabuada

numero = int(input('Digite o número da tabuada: '))
#pergunta qual a tabuada que o usuário quer

n = int(input('Digite até quanto calcular: '))
# pergunta até qual número calcular a tabuada

def conta (numero, n):
    for i in range(1, n + 1):
        print(f'{i} x {numero} = {numero * i}')
        time.sleep(0.5)
#cria um laço de repetição pra calcular a tabuada, logo ele mostra o resultado do calculo e dá um intervalo de 0.5s (da biblioteca tempo)

conta(numero, n)
#chama a função pra ela aparecer no terminal

print('---- fim da tabuada ----')
#anuncia o fim da tabuada