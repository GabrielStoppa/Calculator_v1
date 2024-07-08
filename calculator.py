#Coleta os números que seram usado na operação
def coletar_numeros():
    numeros = []
    while True:
        entrada = input("\nInsira um valor (ou 'fim' para terminar): ").strip().lower()
        if entrada == 'fim':
            break
        try:
            num = float(entrada)
            numeros.append(num)
        except ValueError:
            print("Valor incorreto. Por favor, insira um número válido.")
    return numeros

#Soma os valores coletados
def soma():
    numeros = coletar_numeros()
    if numeros:
        resultado = sum(numeros)
        print("A soma é:", resultado)
    else:
        print("Nenhum número foi inserido.")

#Subtrai os valores coletados
def subtracao():
    numeros = coletar_numeros()
    if numeros:
        resultado = numeros[0]
        for num in numeros[1:]:
            resultado -= num
        print("A subtração é:", resultado)
    else:
        print("Nenhum número foi inserido.")

#Multiplica os valores coletados
def multiplicacao():
    numeros = coletar_numeros()
    if numeros:
        resultado = 1
        for num in numeros:
            resultado *= num
        print("A multiplicação é:", resultado)
    else:
        print("Nenhum número foi inserido.")

#Dividi os valores coletados
def divisao():
    numeros = coletar_numeros()
    if numeros:
        resultado = numeros[0]
        try:
            for num in numeros[1:]:
                resultado /= num
            print("A divisão é:", resultado)
        except ZeroDivisionError:
            print("Erro: Divisão por zero!")
    else:
        print("Nenhum número foi inserido.")

#Inicio da calculadora
print("Bem-vindo à calculadora!")

#Seleciona a operação que o usuario deseja
continuar = True
while continuar:
    resposta = input("\nO que você pretende fazer? (S)omar, (SU)btrair, (M)ultiplicar ou (D)ividir? ").upper()

    if resposta == "S":
        soma()
    elif resposta == "SU":
        subtracao()
    elif resposta == "M":
        multiplicacao()
    elif resposta == "D":
        divisao()
    else:
        print("\nNenhuma opção válida foi selecionada.")

    continuar_resposta = input("\nDeseja fazer outra operação? (S)im ou (N)ão ").upper()
    if continuar_resposta != "S":
        continuar = False

#Finaliza a opreção
print("\nFim da Operação")
