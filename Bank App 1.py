class ContaCorrente:
    def __init__(self, nome_cliente, cpf_cliente):
        self.nome_cliente = nome_cliente
        self.cpf_cliente = cpf_cliente
        self.saldo = 0
        self.extrato = []

    def depositar(self, valor):
        self.saldo += valor
        self.extrato.append(f"Depósito: +{valor}")

    def sacar(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
            self.extrato.append(f"Saque: -{valor}")
        else:
            print("Saldo insuficiente!")

    def mostrar_extrato(self):
        print(f"Extrato de {self.nome_cliente} (CPF: {self.cpf_cliente}):")
        for operacao in self.extrato:
            print(operacao)
        print(f"Saldo atual: {self.saldo}")

# Criar um usuário e conta corrente
nome = input("Digite o nome do cliente: ")
cpf = input("Digite o CPF do cliente: ")
conta = ContaCorrente(nome, cpf)

while True:
    print("\nMenu:")
    print("1. Depositar")
    print("2. Sacar")
    print("3. Ver Extrato")
    print("0. Sair")

    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        valor = float(input("Digite o valor para depósito: "))
        conta.depositar(valor)
    elif opcao == 2:
        valor = float(input("Digite o valor para saque: "))
        conta.sacar(valor)
    elif opcao == 3:
        conta.mostrar_extrato()
    elif opcao == 0:
        break
    else:
        print("Opção inválida. Tente novamente.")
