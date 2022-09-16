# Verifica/valida um CPF. O programa inicia com duas opções ao usuário:
# Opção 1 - digitar um CPF para saber se é válido
# Opção 2 - gerar os dígitos verificadores de um CPF baseado nos nove primeiros
# dígitos informados
# O programa só deve aceitar CPFs no formato xxx.xxx.xxx-xx ou xxx.xxx.xxx conforme cada caso
# descrito acima. Para a opção 1, mostre se o CPF é válido ou não. Para a opção 2, mostre os dois
# dígitos verificadores encontrados. O programa deve solicitar se o usuário deseja realizar mais
# alguma ação. Caso sim, o programa reinicia, caso não, o programa encerra.
# Exemplo de saída:

from operator import index


def digitoVerificador(lista):
    lista_base = [10,9,8,7,6,5,4,3,2]
    lista_base2 = [11,10,9,8,7,6,5,4,3,2]
    
    soma = 0

    for i in range (9):
        numero = lista[i] * lista_base[i] 
        soma += numero
   
    x = soma % 11
    if x < 2:
        x = 0
    else:
        x = 11 - x
    lista.append(x)
    
    soma = 0
    for i in range (10):
        numero = lista[i] * lista_base2[i] 
        soma += numero
     
    x = soma % 11 
    if x < 2:
        x = 0
    else:
        x = 11 - x
    lista.append(x)

    return lista



continuar = 'sim'
while continuar in 'sim':

    print("Verificação de CPF, seja bem-vindo(a)!")
    print("1 – Validar CPF")
    print("2 – Gerar dígitos verificadores de um CPF")
    opcao = int(input("Escolha uma opção:"))

    if opcao == 1:
        cpf = str(input("Digite o CPF (no formato XXX.XXX.XXX-XX): "))

        while len(cpf) < 14:
            cpf = str(input("Digite o CPF no formato correto (XXX.XXX.XXX-XX): "))

        while cpf[3] not in "." and cpf[7] not in "." and cpf[11] not in "-": # verificação aqui
            cpf = str(input("Digite o CPF no formato correto (XXX.XXX.XXX-XX): "))

        
        cpf = cpf.replace(".", "").replace("-", "")
        lista = list(map(int, cpf))
        lista1 = []

        for i in range(9):
            lista1.append(lista[i])

        listaRetorno1 = digitoVerificador(lista1)

        if lista == listaRetorno1:
            print("CPF é válido!")
        else:
            print("CPF é inválido!")


    elif opcao == 2:
        cpf = str(input("Informe os primeiros 9 dígitos do CPF (no formato XXX.XXX.XXX): "))

        while len(cpf) < 11:
            cpf = str(input("Digite o CPF no formato correto (XXX.XXX.XXX): "))

        while cpf[3] not in "." and cpf[7] not in ".": # verificação aqui
            cpf = str(input("Digite o CPF no formato correto (XXX.XXX.XXX): "))

        cpf = cpf.replace(".", "")
        lista2 = list(map(int, cpf))
        
        listaRetorno2 = digitoVerificador(lista2)
        print('Os dígitos verificadores são:', listaRetorno2[9],listaRetorno2[10])
        
        listaRetorno2.insert(3,".")
        listaRetorno2.insert(7,".")
        listaRetorno2.insert(11,"-")
        
        respostaFinal = ""
        respostaFinal = "".join(str(elem) for elem in listaRetorno2)

        print("O CPF completo é: ", respostaFinal)
    
    controle = input("Deseja realizar outra operação? Digite sim ou nao ")
    
    if controle == "nao":
        continuar = "nao"


print("Obrigado por utilizar nosso serviço!")

    

