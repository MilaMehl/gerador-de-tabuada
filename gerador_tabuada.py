import time

tabuada = input("Digite o número que você deseja a tabuada: ")
tabuada = int(tabuada)
while tabuada <= 10:
    resultado = tabuada * 1
    print(f"{tabuada} x {1} = {resultado}")
    time.sleep(1)
    resultado = tabuada * 2
    print(f"{tabuada} x {2} = {resultado}")
    time.sleep(1)
    resultado = tabuada * 3
    print(f"{tabuada} x {3} = {resultado}")
    time.sleep(1)
    resultado = tabuada * 4
    print(f"{tabuada} x {4} = {resultado}")
    time.sleep(1)
    resultado = tabuada * 5
    print(f"{tabuada} x {5} = {resultado}")
    time.sleep(1)
    resultado = tabuada * 6
    print(f"{tabuada} x {6} = {resultado}")
    time.sleep(1)
    resultado = tabuada * 7
    print(f"{tabuada} x {7} = {resultado}")
    time.sleep(1)
    resultado = tabuada * 8
    print(f"{tabuada} x {8} = {resultado}")
    time.sleep(1)
    resultado = tabuada * 9
    print(f"{tabuada} x {9} = {resultado}")
    time.sleep(1)
    resultado = tabuada * 10
    print(f"{tabuada} x {10} = {resultado}")
    print("--- Fim da tabuada, tchau! ---")
    break
