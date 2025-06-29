# /*******************************************************************************
# Autor: Gustavo Leão de Jesus
# Componente Curricular: MI Algoritmos I
# Concluido em: 01/06/2025
# Declaro que este código foi elaborado por mim de forma individual e não contém nenhum
# trecho de código de outro colega ou de outro autor, tais como provindos de livros e
# apostilas, e páginas ou documentos eletrônicos da Internet. Qualquer trecho de código
# de outra autoria que não a minha está destacado com uma citação para o autor e a fonte
# do código, e estou ciente que estes trechos não serão considerados para fins de avaliação.
# Este software foi criado em Python versão 3.13.1 e desenvolvido no sistema operacional 
# Windows 10 de 64 bits.
# ******************************************************************************************/

import os 
import time

class Usuario:
    def __init__(self):
        self.nome = ""
        self.categoria = ""
        self.cashback = 0.00

    def __repr__(self): # Representa um objeto como uma string.
        return f"{self.nome} {self.categoria} {self.cashback}"
    
    # Função que verifica a existência de um usuário na lista de informações.
    def banco(self, dados):
        print(dados)
        
        # A lista "dados" contém as informações de todos os clientes.
        for i in range(len(dados)): 
            linha = dados [i] # Acesso individualmente cada índice.  

            # Reparto a linha em partes individuais com o método split() e obtenho 
            # informações especificas de acordo com seus indices, dado que:
            # repartição [0]: Nome do usuário.
            # repartição [1]: Categoria.
            # repartição [2]: Cashback.

            repartição = str(linha).split() 
            
            if repartição [0] == self.nome: # Verifico se o nome do usuário existe nos dados.
                
                limpar()
                titulo("-.+ Comprar Bubble Tea +.-")
                print("Que bom te ver denovo!")
                return linha, i # Retorno as informações do cliente e seu indice na lista.
            
        # Cadastramento de novos clientes.
        limpar()
        titulo("-.+ Cadastrando um novo usuário +.-")
        print("Obrigado por escolhe nosso Bubble Tea!\n")

        print("[1] Estudante")
        print("[2] Professor ou Funcionário")
        print("[3] Comunidade\n")

        categoria = input("Digite a sua categoria: ")

        while categoria != "1" and categoria != "2" and categoria != "3":
            categoria = input("Digite a categoria: ")

        if categoria == "1":
            cliente.categoria = "Estudante"
        elif categoria == "2":
            cliente.categoria = "Professor-ou-Funcionário"
        elif categoria == "3":
            cliente.categoria = "Comunidade"

        dados.append(cliente)

        return dados [-1], -1

class Pedido:
    def __init__(self):

        self.base = ""
        self.complemento = ""

    def valor(self):
        
        custo = 0
        limpar()
        titulo("-.+ Escolha a base do Chá +.-")

        print("    [1] Leite ................ R$ 4,35")
        print("    [2] Maracujá ............. R$ 4,60")
        print("    [3] Rosa ................. R$ 5,85")
        print("    [4] Manga ................ R$ 5,47")
        print()

        base = str(input("Escolha uma opção: "))
        while base != "1" and base != "2" and base != "3" and base != "4":
            base = str(input("Escolha uma opção:: "))

        if base == "1":
            custo += 4.35 
            self.base = "Leite"

        elif base == "2":
            custo += 4.60
            self.base = "Maracujá"

        elif base == "3":
            custo += 5.85
            self.base = "Rosa"

        elif base == "4":
            custo += 5.47
            self.base = "Manga"
        
        on = 0
       
        controle = [1, 1, 1, 1, 1] # Limita a quantidade de complementos por opção.
        
        complementos = [] # Armazena os complementos escolhidos.

        while 1 in controle and on == 0:
            limpar()
            titulo("-.+ Escolha os complementos +.-")

            if controle [0] == 1:
                print("    [1] Boba ................. R$ 0,50")
            
            if controle [1] == 1:
                print("    [2] Lichia ............... R$ 0,75")
            
            if controle [2] == 1:
                print("    [3] Geleia ............... R$ 0,65")
            
            if controle [3] == 1:
                print("    [4] Taro ................. R$ 1,00")
            
            if controle [4] == 1:
                print("    [5] Chia ................. R$ 0,35")  
            
            print()
            print("    [6] Não adicionar")
            print()
            sabores = str(input("Escolha as opções: "))
            
            if sabores == "1":
                if controle [0] == 1:
                    controle [0] = 0
                    custo += 0.50
                    complementos.append(", Boba")
                else:
                    print("Apenas um complemento de cada.")
                    time.sleep(1)
            elif sabores == "2":
                if controle [1] == 1:
                    controle [1] = 0
                    custo += 0.75
                    complementos.append(", Lichia")
                else:
                    print("Apenas um complemento de cada.")
                    time.sleep(1)
            elif sabores == "3":
                if controle [2] == 1:
                    controle [2] = 0
                    custo += 0.65
                    complementos.append(", Geleia")
                else:
                    print("Apenas um complemento de cada.")
                    time.sleep(1)
            elif sabores == "4":
                if controle [3] == 1:
                    controle [3] = 0
                    custo += 1.00
                    complementos.append(", Taro")
                else:
                    print("Apenas um complemento de cada.")
                    time.sleep(1)
            elif sabores == "5":
                if controle [4] == 1:
                    controle [4] = 0
                    custo += 0.35
                    complementos.append(", Chia")
                else:
                    print("Apenas um complemento de cada.")
                    time.sleep(1)
            elif sabores == "6":
                on += 1

            else: 
                print("Entrada inválida!")
                time.sleep(1)
                
        self.complemento = complementos
        return custo

    def resumo(self, valor, cliente, indice, dados):

        usuario = str(cliente)
        elementos = usuario.split()

        nome = ((elementos [0]).replace("-", " ")).title() 
        categoria = (elementos [1]).replace("-", " ")
        cashback = float(elementos [2])
        
        cb = 0.00 # Cashback usado
        v_scb = 0.00 # Valor sem cashback

        if elementos [1] == "Estudante":
            desconto = valor * 0.75
        elif elementos [1] == "Professor-ou-Funcionário":
            desconto = valor - 1
        elif elementos [1] == "Comunidade":
            desconto = valor
        
        limpar()

        print("RESUMO DO PEDIDO")
        print(f"Cliente: {nome}") 
        print(f"Base: {self.base}")
        print(f"Adicionais:", end="")
        for i in range(len(self.complemento)):
            if i == 0:
                print(f"{(self.complemento[i]).replace(",", "")}", end="") 
            else:
                print(f"{self.complemento[i]}", end="")
        print()

        if desconto != valor:
            print(f"Cliente com desconto especial de {categoria}")
        else:
            print("Cliente sem desconto especial.")

        print(f"Valor total: R$ {desconto:.2f}") 

        # Variáveis de apoio para armazemento do histórico de pedidos.
        v_scb = desconto
        com_cb = cashback
        cb = cashback
        saldo = cashback

        if cashback > 0.00: 
            
            print()
            print("[1] Sim      [2] Não")
            print()

            cash = input(f"Deseja usar o cashback de R$ {cashback}? ")

            while cash != "1" and cash != "2":
                cash = input(f"Deseja usar o cashback de R$ {cashback}? ")

            if cash == "1":
                desconto -= cashback 
                
                if desconto < 0.00:

                    cb = cashback + desconto
                    v_scb = cb
                    com_cb = cb
                    cashback = (desconto * -1)
                    desconto = 0.00 

                    print(f"\nValor final: R$ {desconto:.2f}")
                else:
                    print(f"\nValor final: R$ {desconto:.2f}")
                    cashback = 0.00

                
            elif cash == "2":
                print("\nCashback não utilizado.")
                com_cb = cashback
                cb = 0.00
        
        cashback += desconto * 0.10 # 10% do valor total.

        print(f"Saldo de cashback: R$ {cashback:.2f}")  

        continua = input("\nPrecione ENTER: ")
        # Teste de qualidade.
        print()
        # Atualizando o saldo de cashback do cliente atual.
        dados [indice] = elementos [0] + " " + elementos [1] + " " + str(round(cashback, 2))  + "\n"
        # Guardo as informações do pedido em uma lista.
        historico = []
        historico.append(f"\nCliente: {(elementos [0]).title()}\n")
        historico.append(f"Base: {self.base}\n")
        historico.append("Complementos:")
    
        for i in range(len(self.complemento)):
            if i == 0:
                historico.append(f"{(self.complemento [i]).replace(",", "")}")
            else:
                historico.append(f"{self.complemento [i]}")
 
        historico.append(f"\nSaldo de cashback: R$ {saldo:.2f}\n")
        historico.append(f"Cashback utilizado: R$ {cb:.2f}\n")
        historico.append(f"Valor com cashback: R$ {(v_scb - com_cb):.2f}\n")
        historico.append(f"Valor sem cashback: R$ {v_scb:.2f}\n")
        historico.append(f"Valor total sem desconto: R$ {valor:.2f}\n")
        historico.append(f"Valor final: R$ {desconto:.2f}\n")

        gravar_historico(historico)

# Função responsável por escrever no final do arquivo o pedido mais recente. 
def gravar_historico(registros):

    with open("historico.txt", "a+") as pedidos:
        for i in range(len(registros)):
            pedidos.write(f"{str(registros [i])}")

# Função responsável por abrir no modo de leitura o arquivo que guarda o histórico de pedidos.
def historico():
    historico = []
    if os.path.isfile("historico.txt"): # Verifica se o arquivo existe no computador.
        with open("historico.txt", "r") as pedidos:
            historico = pedidos.readlines()
        return historico

    return historico

# Limpar o terminal de acordo o sistema operacional. 
def limpar():
    if os.name == "nt": 
        os.system("cls") # Windows
    else:
        os.system("clear") # Linux/Mac

def titulo(textos):
    tamanho = len(textos)
    meio = ((42 - tamanho) // 2) - 1
    print("=" * 42)
    print(" " * meio, textos)
    print("=" * 42)
    print()

# Ao final do programa os dados dos clientes são guardados no arquivo.
def gravar(dados):

    with open("banco.txt", "w") as arquivo:
        for i in dados:
            arquivo.write(f"{str(i)}")

# Verifico se o arquivo existe no computador, caso contrário, retorno uma lista vázia. 
def arquivo():
    dados = []
    if os.path.isfile("banco.txt"): # Verifica se o arquivo existe no computador.

        with open("banco.txt", "r") as arquivo:
            dados = arquivo.readlines()
        return dados

    return dados

# Programa principal

# A variável "dados" receberá as informações dos clientes durante o programa. 
dados = arquivo()

# Variável que controla o Loop do Menu principal.
on = 0

while on == 0:

    # Opções do Menu.
    titulo("-.+ Bubble Tea UEFS +.-")

    print("[1] Comprar")
    print("[2] Histórico")
    print("[3] Sair")
    print()
    comando = (str(input("Escolha uma opção: "))).strip()

    limpar()

    if comando == "1":
        titulo("-.+ Comprar Bubble Tea +.-")

        # Declaração do objeto chamado cliente.
        cliente = Usuario()

        # Indentificação do cliente.
        nome = str(input("Qual é o seu nome: "))
        # Impede que o usuário insira um nome "vázio" atráves do método strip().
        while nome.strip() == "": 
            print("Indentificação inválida!")
            nome = str(input("Qual é o seu nome: "))

        # Substituo os espaços vázios por hifens e removo as barras invertidas, evitando erros posteriores.
        nome = nome.replace(" ", "-")
        nome = nome.replace("\\", "")

        # O programa não é case sensitive.
        name = nome.lower()
        cliente.nome = name

        # Verifico se o usuário possui cadastro para recuperar suas informações. Caso não exista, 
        # será criado um novo usuário. Em ambas as situações, o retorno será 
        # uma tupla contendo o usuário e seu índice na lista.
        cliente = cliente.banco(dados) 
        usuario = cliente [0] # Retornará as informações do usuário atual.
        indice = cliente [1]  # Armazena a posição do usuário na lista para futuras alterações.

        # Realizando a compra.

        # Declaração do objeto pedido.
        pedido = Pedido()

        # Anota o pedido calculando o valor final.
        valor = pedido.valor()

        # Imprimi ao usuário o resumo do pedido.
        conta = pedido.resumo(valor, usuario, indice, dados)
        limpar()
        # Questiona o processamento de um novo pedido ao final.
        titulo("-.+ Novo pedido +.-")
        print("[1] Sim      [2] Não")
        print()
        processar = (input("Deseja processar um novo pedido? ")).strip()
        while processar != "1" and processar != "2":
            processar = input("Deseja processar um novo pedido? ")

        limpar()
        if processar == "2":         
            gravar(dados)
            titulo("-.+ Encerrando o programa +.-")
            continua = input("Precione ENTER: ")
            on += 1

    elif comando == "2":
        
        titulo("-.+ Histórico de pedidos +.-")

        print("Pedidos registrados:")

        registros = historico()

        if registros:
            for i in range(len(registros)):
                print((registros[i].strip()).replace("-", " "))
        else:
            print("Histórico vazio no momento.")
        print()
        continua = input("Precione ENTER: ")
        limpar()

    elif comando == "3":
        gravar(dados)
        titulo("-.+ Encerrando o programa +.-")
        continua = input("Precione ENTER: ")
        on += 1
    


        
