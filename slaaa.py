while True:
    try:
        numero = int(input("Digite um número inteiro: "))
        resultado = 100 / numero
        print(f"O resultado da divisão é: {resultado:.2f}")
        break  # Sai do loop se a operação for bem-sucedida
    except ZeroDivisionError:
        print("Erro: Não é possível dividir por zero. Tente novamente.")