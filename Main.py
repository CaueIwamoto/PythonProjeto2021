import os

#Primeira opção: criar uma conta, registrar o CPF, etc.
def criarConta():
    nome = input("Digite o seu nome: ")
    cpf = input("Digite o seu CPF: ")
    print("=" * 30)
    print("{:^30}".format("Tipos de conta"))
    print("=" * 30)
    print("\n Conta salário: cobra taxa de 5% a cada débito realizado e não permite débitos que deixem a conta com saldo negativo")
    print("\n Conta comum: cobra taxa de 3% a cada débito realizado e permite um saldo negativo de até R$500,00")
    print("\n Conta plus: cobra taxa de 1% a cada débito realizado e permite um saldo negativod e até R$5000,00")
    tipoconta = input("\nTipo de conta: ")
    valorinicial = float(input("Valor inicial da conta: R$"))
    senha = input("Crie a sua senha: ")
    print("Conta criada com sucesso!")
#Fazer com que um usuário não tente se cadastrar com o mesmo CPF de outro usuário.
    if os.path.exists(cpf + ".txt"):
        print("Cliente já registrado!")
#Arquivos para organizar no arquivo .txt o nome, cpf, tipo de conta, etc.
    else:
        arquivo = open(cpf + ".txt", "w")
        arquivo.write("%s\n" % nome)
        arquivo.write("%s\n" % cpf)
        arquivo.write("%s\n" % tipoconta)
        arquivo.write("%s\n" % valorinicial)
        arquivo.write("%s\n" % senha)
        arquivo.close()

#Segunda opção: apagar o cliente pelo CPF.
def apagaCliente():
    cpf = input("Digite o CPF: ")
    os.remove(cpf + ".txt")
    print("Usuário deletado com sucesso!")

#Terceira opção: Debita um valor na conta de um cliente.
def debitarCliente():
    cpf = input("Digite o CPF do usuário que você deseja debitar: ")
    senha = input("Digite a senha: ")
    valorDebito = float(input("Digite o valor: R$"))
 #Fazer o programa conferir o tipo de conta e senha:
    if os.path.exists(cpf + ".txt"):
        lista = []
        arquivo = open(cpf + ".txt", "r")
        for linha in arquivo.readlines():
            lista.append(linha.strip())
        arquivo.close
        if lista[4] == senha:
            if lista[2] == "Salário":
                taxa = valorDebito * 0.05
                lista[3] = float(lista[3]) - valorDebito - taxa 
                arquivo = open(cpf + ".txt", "w") 
                for i in range (len(lista)):
                    arquivo.write("%s\n" % lista[i])
                arquivo.close()
            elif lista[2] == "Comum":
                taxa = valorDebito * 0.03
                lista[3] = float(lista[3]) - valorDebito - taxa 
                arquivo = open(cpf + ".txt", "w") 
                for i in range (len(lista)):
                    arquivo.write("%s\n" % lista[i])
                arquivo.close()
            elif lista[2] == "Plus":
                taxa = valorDebito * 0.01
                lista[3] = float(lista[3]) - valorDebito - taxa 
                arquivo = open(cpf + ".txt", "w") 
                for i in range (len(lista)):
                    arquivo.write("%s\n" % lista[i])
                arquivo.close()  
        else:
            print("Senha Incorreta!")


#Quarta opção: Deposita um valor na conta de um cliente.
def depositarDinheiro():
    cpf = input("Digite o CPF do cliente desejado: ")
    valor = float(input("Digite o valor para depositar: R$"))
    lista = []
    arquivo = open(cpf + ".txt", "r")
    for linha in arquivo.readlines():
        lista.append(linha.strip())
    arquivo.close()

    valorNovo = float(lista[3]) + valor
    lista[3] = str(valorNovo)
    arquivo = open(cpf + ".txt", "w")
    for i in range (len(lista)):
        arquivo.write("%s\n" % lista[i])

    print("Valor depositado com sucesso!")



#Quinta opção: Exibe o saldo da conta do cliente.
def exibirSaldo():
    cpf = input("Digite o seu CPF: ")
    senha = input("Digite a sua senha: ")
    arquivo = open(cpf + ".txt", "r")
    saldo = arquivo.read().splitlines() 

    #Print para mostrar o saldo atual de acordo com o arquivo .txt:
    print(saldo[3])

    arquivo.close()
#Sexta opção: Exibir histórico de todas as operações realizadas.
def extrato():
    cpf = input("Digite o seu CPF: ")
    senha = input("Digite a sua senha: ")
    
    arquivo = open(cpf + ".txt", "r")
    lista = []
    for i in arquivo.readlines():
        lista.append(i.strip())
 #Fazer o programa conferir se a senha está correta ou incorreta:
    if lista[4] == senha:
        lista.pop(4)
        for i in lista:
            print(i)
    else:
        print("Senha Incorreta!")


#Selecionar as opções (no terminal).
def main():
    while True:
        print()
        print("=" * 30)
        print("{:^30}".format("MENU"))
        print("=" * 30)
        print("1 - Novo Cliente")
        print("2 - Apaga Cliente")
        print("3 - Debita")
        print("4 - Deposita")
        print("5 - Saldo")
        print("6 - Extrato")
        print("0 - Sair")
#Escolher uma das opções, no terminal:
        opcao = input("Escolha uma das opções: ")

        if opcao == "1":
            criarConta()
        elif opcao == "2":
            apagaCliente()
        elif opcao == "3":
            debitarCliente()
        elif opcao == "4":
            depositarDinheiro()
        elif opcao == "5":
            exibirSaldo()
        elif opcao == "6":
            extrato()

#Opção "sair":
        if opcao == "0":
            break
    

main()
