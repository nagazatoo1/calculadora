# Função para adição
def adicao(num1, num2):
    return num1 + num2

# Função para subtração
def subtracao(num1, num2):
    return num1 - num2

# Função para multiplicação
def multiplicacao(num1, num2):
    return num1 * num2

# Função para divisão
def divisao(num1, num2):
    if num2 != 0:
        return num1 / num2
    else:
        return "Erro: Divisão por zero não é permitida!"

# Função principal da calculadora
def calculadora():
    print("Selecione a operação:")
    print("1. Adição")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")

    escolha = input("Digite a opção (1/2/3/4): ")

    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))

    resultado = 0

    if escolha == '1':
        resultado = adicao(num1, num2)
    elif escolha == '2':
        resultado = subtracao(num1, num2)
    elif escolha == '3':
        resultado = multiplicacao(num1, num2)
    elif escolha == '4':
        resultado = divisao(num1, num2)
    else:
        print("Opção inválida!")

    print("O resultado é: ", resultado)

# Chamando a função principal
calculadora()