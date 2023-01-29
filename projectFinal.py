while True:

    try:
        temperatura = float(input("Digite o valor da temperatura: \n"))
        tipo = str(input("Digite o tipo de medida: C, K, F. Caso queira sair, digite SAIR. \n").upper())
        tipoFinal = str(input("Digite o tipo desejado como resultado: C, K, F.\n").upper())
        erroTipo = "Desculpe, o tipo digitado não é aceito, tente novamente."
    except:
        print("Ops, o valor digitado não é aceito. Favor, tente novamente.\n")
        continue
        
    valorFinal = 0

    if tipo == 'C' :
        if tipoFinal == 'C':
            valorFinal = temperatura

        elif tipoFinal == 'F':
            valorFinal = (temperatura * 9/5) + 32

        elif tipoFinal == 'K':
            valorFinal = temperatura + 273.15

        else:
            print(erroTipo)
            continue

    elif tipo == 'F' :
        if tipoFinal == 'C':
            valorFinal = (temperatura -32) * 5/9

        elif tipoFinal == 'F':
            valorFinal = temperatura

        elif tipoFinal == 'K':
            valorFinal = (temperatura - 32) * 5/9 + 273.15

        else:
            print(erroTipo)
            continue

    elif tipo == 'K' :
        if tipoFinal == 'C':
            valorFinal = temperatura - 273.15

        elif tipoFinal == 'F':
            valorFinal = (temperatura - 273.15) * 9/5 + 32

        elif tipoFinal == 'K':
            valorFinal = temperatura

        else:
            print(erroTipo)
            continue

    elif tipo == 'SAIR' :
        print("Bye Bye!")
        exit()

    else:
        print(erroTipo)
        continue
        
    print("O tipo inicial foi : " + tipo + ", com o tipo final sendo: " + tipoFinal + ", e a temperatura sendo: " + str(temperatura) + ". Portanto o resultado final dessa linha é : " + str(valorFinal) + ".")
    continue